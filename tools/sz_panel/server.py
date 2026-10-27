#!/usr/bin/env python3
"""
Stream Zone Management Panel (sz-panel)
Backend y Dashboard Localhost para control total de vencimientos, renovaciones,
reasignación de cuentas caídas y purga de cuentas muertas en NuVlyx.
"""

import sys
import os
import re
import json
import sqlite3
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import requests
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://api.nuvlyx.com/api/v1"
TENANT_SLUG = "stream-zone-6822"
CACHE_TOKEN_PATH = "/home/rootkit/.cache/sz_admin_token.json"
DB_PATH = "/home/rootkit/.cache/sz_panel_state.sqlite"
PORT = 5050

TZ_COLOMBIA = timezone(timedelta(hours=-5))

# ==============================================================================
# BASE DE DATOS LOCAL (PERSISTENCIA DE ACCIONES)
# ==============================================================================
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS actions (
                license_id TEXT PRIMARY KEY,
                order_id TEXT,
                order_number TEXT,
                client_name TEXT,
                client_phone TEXT,
                service_name TEXT,
                status TEXT, -- PENDING, NOTIFIED, RENEWED, REASSIGNED, NOT_RENEWED
                extended_until TEXT,
                reassigned_license_id TEXT,
                notes TEXT,
                updated_at TEXT
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_status ON actions(status)")
        conn.commit()

init_db()

# ==============================================================================
# AUTENTICACIÓN Y CONEXIÓN CON NUVLYX
# ==============================================================================
def get_auth_headers():
    token = None
    if os.path.exists(CACHE_TOKEN_PATH):
        try:
            with open(CACHE_TOKEN_PATH) as f:
                token = json.load(f).get("accessToken")
        except Exception:
            token = None
    if not token:
        # Re-login
        url = f"{BASE_URL}/auth/admin-login"
        payload = {
            "email": "jnsierra@jdc.edu.co",
            "password": "Stream_Zone*1",
            "rememberMe": True
        }
        r = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=12)
        if r.status_code in (200, 201):
            data = r.json()
            token = data["accessToken"]
            with open(CACHE_TOKEN_PATH, "w") as f:
                json.dump({"accessToken": token, "tenantSlug": TENANT_SLUG}, f, indent=2)
    return {
        "Authorization": f"Bearer {token}",
        "x-tenant-slug": TENANT_SLUG,
        "Content-Type": "application/json"
    }

# Cachés en memoria
CACHE_PRODUCTS = {}
CACHE_CLIENTS = {}
CACHE_CREDENTIALS = {}

def refresh_catalog():
    global CACHE_PRODUCTS
    headers = get_auth_headers()
    try:
        r = requests.get(f"{BASE_URL}/products", headers=headers, timeout=12)
        if r.status_code == 200:
            p_map = {}
            for p in r.json():
                for v in p.get("variations", []):
                    p_map[v["id"]] = {
                        "productId": p.get("id"),
                        "productName": p.get("name"),
                        "variationId": v.get("id"),
                        "variationName": v.get("name", "1 mes"),
                        "price": v.get("price"),
                        "durationDays": v.get("durationDays", 30),
                        "fullName": f"{p.get('name')} ({v.get('name', '1 mes')})"
                    }
            CACHE_PRODUCTS = p_map
    except Exception as e:
        print("Error refreshing catalog:", e)

refresh_catalog()

def parse_credential_text(c_text):
    if not c_text:
        return "", "", "N/A", "N/A"
    m_email = re.search(r"(?:correo|usuario|user|email):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_pass = re.search(r"(?:contrase[ñn]a|clave|pass|password):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_prof = re.search(r"(?:perfil|profile):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_pin = re.search(r"(?:pin|c[oó]digo):\s*([^\s;]+)", c_text, re.IGNORECASE)
    
    c_email = m_email.group(1).strip() if m_email else ""
    c_pass = m_pass.group(1).strip() if m_pass else ""
    c_prof = m_prof.group(1).strip() if m_prof else ""
    c_pin = m_pin.group(1).strip() if m_pin else ""

    # Perfil con año: "Perfil: 1 (2022)" -> se conserva el año en la entrega
    m_prof_year = re.search(r"perfil:\s*(\d+)\s*\((\d{4})\)", c_text, re.IGNORECASE)
    if m_prof_year:
        c_prof = f"{m_prof_year.group(1)} ({m_prof_year.group(2)})"
    return c_email, c_pass, c_prof, c_pin

def acceso_line(c_pass):
    """Cuentas sin contraseña: la credencial trae un link, no una clave."""
    val = (c_pass or "").strip()
    if val.lower().startswith(("http://", "https://")):
        return f"🔗 *Enlace*: {val}"
    return f"🔑 *Contraseña*: {val or 'N/A'}"

# ==============================================================================
# API HELPER: OBTENER LISTA DE VENCIMIENTOS
# ==============================================================================
def get_vencimientos_data():
    headers = get_auth_headers()
    now_local = datetime.now(TZ_COLOMBIA)
    today = now_local.date()
    
    start_date = today - timedelta(days=2) # Incluye 2 días de vencidos recientes
    end_date = today + timedelta(days=4)   # Próximos 4 días
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")
    
    page = 1
    sold_items = []
    while True:
        try:
            r = requests.get(
                f"{BASE_URL}/inventory/licenses",
                headers=headers,
                params={"status": "SOLD", "page": page, "limit": 100},
                timeout=12
            )
            if r.status_code != 200:
                break
            res = r.json()
            items = res.get("data", [])
            if not items:
                break
            for it in items:
                exp = it.get("expiresAt")
                if exp:
                    d_str = exp[:10]
                    if start_str <= d_str <= end_str:
                        sold_items.append(it)
            if page >= res.get("meta", {}).get("totalPages", 1):
                break
            page += 1
        except Exception:
            break
            
    # Obtener credenciales y teléfonos en paralelo
    needed_creds = [it["id"] for it in sold_items if it["id"] not in CACHE_CREDENTIALS]
    needed_clients = set()
    for it in sold_items:
        cid = it.get("buyer", {}).get("clientId")
        if cid and cid not in CACHE_CLIENTS:
            needed_clients.add(cid)
            
    def fetch_cred(lid):
        try:
            r = requests.get(f"{BASE_URL}/inventory/licenses/{lid}/credential", headers=headers, timeout=8)
            if r.status_code == 200:
                CACHE_CREDENTIALS[lid] = r.json().get("credential", "")
        except Exception:
            pass

    def fetch_client(cid):
        try:
            r = requests.get(f"{BASE_URL}/users/{cid}", headers=headers, timeout=8)
            if r.status_code == 200:
                u = r.json()
                w = u.get("wallet") or {}
                b = w.get("balance") or 0
                try:
                    b_float = float(b)
                except Exception:
                    b_float = 0.0
                CACHE_CLIENTS[cid] = {
                    "id": cid,
                    "name": u.get("name") or "Cliente",
                    "phone": u.get("phoneNumber") or u.get("phone") or "",
                    "walletBalance": b_float,
                    "walletCurrency": w.get("currency") or "COP"
                }
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=16) as ex:
        ex.map(fetch_cred, needed_creds)
        ex.map(fetch_client, list(needed_clients))
        
    # Consultar base de datos local para estados guardados
    local_states = {}
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT license_id, status, extended_until, reassigned_license_id, notes FROM actions")
        for row in cursor.fetchall():
            local_states[row[0]] = {
                "status": row[1],
                "extended_until": row[2],
                "reassigned_license_id": row[3],
                "notes": row[4]
            }

    records = []
    for it in sold_items:
        lid = it.get("id")
        vid = it.get("variationId")
        p_info = CACHE_PRODUCTS.get(vid, {})
        service_name = p_info.get("fullName") or it.get("variation", {}).get("name") or "Servicio"
        
        buyer = it.get("buyer", {})
        cid = buyer.get("clientId")
        c_info = CACHE_CLIENTS.get(cid, {}) if cid else {}
        client_name = buyer.get("clientName") or c_info.get("name") or "Cliente"
        order_num = buyer.get("orderNumber") or "ORD-N/A"
        order_id = buyer.get("orderId") or (it.get("orderItems", [{}])[0].get("order", {}).get("id") if it.get("orderItems") else "")
        
        phone = c_info.get("phone") if c_info else ""
        if not phone:
            phone = buyer.get("clientEmail", "")
            
        wallet_balance = c_info.get("walletBalance", 0.0)
        wallet_currency = c_info.get("walletCurrency", "COP")
        price = p_info.get("price") or 0
        try:
            price_val = float(price)
        except Exception:
            price_val = 0.0

        raw_cred = CACHE_CREDENTIALS.get(lid, "")
        c_email, c_pass, c_prof, c_pin = parse_credential_text(raw_cred)
        if not c_email and it.get("accountEmail"):
            c_email = it["accountEmail"]
            
        exp_iso = it.get("expiresAt")
        exp_dt = datetime.fromisoformat(exp_iso.replace("Z", "+00:00")).astimezone(TZ_COLOMBIA)
        exp_date = exp_dt.date()
        fecha_corte_str = exp_date.strftime("%d/%m/%Y")
        
        diff_days = (exp_date - today).days
        if diff_days < 0:
            badge_label = f"Vencido ({abs(diff_days)}d)"
            badge_color = "red"
        elif diff_days == 0:
            badge_label = "Vence Hoy"
            badge_color = "rose"
        elif diff_days == 1:
            badge_label = "Vence Mañana"
            badge_color = "amber"
        else:
            badge_label = f"{diff_days} días restantes"
            badge_color = "blue"
            
        l_state = local_states.get(lid, {})
        current_status = l_state.get("status", "PENDING")
        
        records.append({
            "licenseId": lid,
            "clientId": cid,
            "walletBalance": wallet_balance,
            "walletCurrency": wallet_currency,
            "price": price_val,
            "orderId": order_id,
            "orderNumber": order_num,
            "variationId": vid,
            "serviceName": service_name,
            "clientName": client_name,
            "phone": phone,
            "email": c_email or "N/A",
            "password": c_pass or "N/A",
            "profile": c_prof or "Principal",
            "pin": c_pin or "N/A",
            "expiresAt": fecha_corte_str,
            "diffDays": diff_days,
            "badgeLabel": badge_label,
            "badgeColor": badge_color,
            "status": current_status,
            "extendedUntil": l_state.get("extended_until"),
            "reassignedLicenseId": l_state.get("reassigned_license_id"),
            "notes": l_state.get("notes", "")
        })
        
    records.sort(key=lambda r: (0 if r["status"] == "PENDING" else 1, r["diffDays"]))
    return records

# ==============================================================================
# SERVIDOR HTTP REST & SPA
# ==============================================================================
class SzPanelHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/vencimientos":
            data = get_vencimientos_data()
            self._send_json({"ok": True, "records": data, "total": len(data)})
            
        elif path == "/api/stats":
            records = get_vencimientos_data()
            active_records = [r for r in records if r["status"] not in ("RETURNED_TO_STOCK", "PURGED")]
            stats = {
                "total": len(active_records),
                "dueToday": len([r for r in active_records if r["diffDays"] == 0]),
                "dueTomorrow": len([r for r in active_records if r["diffDays"] == 1]),
                "expired": len([r for r in active_records if r["diffDays"] < 0]),
                "renewed": len([r for r in records if r["status"] == "RENEWED"]),
                "reassigned": len([r for r in records if r["status"] == "REASSIGNED"]),
                "returnedToStock": len([r for r in records if r["status"] == "RETURNED_TO_STOCK"]),
                "purged": len([r for r in records if r["status"] == "PURGED"]),
                "notRenewed": len([r for r in records if r["status"] in ("NOT_RENEWED", "RETURNED_TO_STOCK", "PURGED")]),
                "pending": len([r for r in active_records if r["status"] in ("PENDING", "NOTIFIED")])
            }
            self._send_json({"ok": True, "stats": stats})
            
        elif path == "/api/stock":
            headers = get_auth_headers()
            try:
                r = requests.get(f"{BASE_URL}/inventory/stock", headers=headers, timeout=10)
                self._send_json({"ok": True, "stock": r.json() if r.status_code == 200 else []})
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, 500)
                
        elif path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_UI.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length).decode("utf-8")) if length > 0 else {}
        headers = get_auth_headers()

        # 1. ACCIÓN: RENOVAR (EXTENDER +30 DÍAS)
        if path == "/api/renew":
            lid = body.get("licenseId")
            days = body.get("days", 30)
            client_id = body.get("clientId")
            price = body.get("price", 0)
            service_name = body.get("serviceName", "Servicio")
            order_num = body.get("orderNumber", "ORD-N/A")
            deduct_wallet = body.get("deductWallet", False)

            now_col = datetime.now(TZ_COLOMBIA)
            extended_date = (now_col + timedelta(days=days)).strftime("%d/%m/%Y")
            
            deducted = False
            wallet_note = ""
            if deduct_wallet and client_id and price > 0:
                try:
                    adj_payload = {
                        "amount": -float(price),
                        "note": f"Renovación {service_name} ({order_num}) - Stream Zone"
                    }
                    radj = requests.post(f"{BASE_URL}/wallet/clients/{client_id}/adjust", json=adj_payload, headers=headers, timeout=10)
                    if radj.status_code in (200, 201):
                        deducted = True
                        wallet_note = f"Descontados ${price:,.0f} de billetera web."
                        if client_id in CACHE_CLIENTS:
                            CACHE_CLIENTS[client_id]["walletBalance"] = max(0.0, CACHE_CLIENTS[client_id].get("walletBalance", 0.0) - float(price))
                except Exception as e:
                    print("Error adjusting wallet:", e)

            action_note = f"Renovado +{days}d." + (f" {wallet_note}" if wallet_note else "")
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("""
                    INSERT INTO actions (license_id, status, extended_until, notes, updated_at)
                    VALUES (?, 'RENEWED', ?, ?, ?)
                    ON CONFLICT(license_id) DO UPDATE SET
                    status='RENEWED', extended_until=?, notes=?, updated_at=?
                """, (lid, extended_date, action_note, now_col.isoformat(), extended_date, action_note, now_col.isoformat()))
                conn.commit()
                
            self._send_json({
                "ok": True,
                "status": "RENEWED",
                "extendedUntil": extended_date,
                "deducted": deducted,
                "deductedAmount": price if deducted else 0
            })

        # 2. ACCIÓN: REASIGNAR CUENTA CAÍDA (CUENTA MURIÓ)
        elif path == "/api/reassign":
            lid = body.get("licenseId")
            vid = body.get("variationId")
            order_id = body.get("orderId")
            client_name = body.get("clientName", "Cliente")
            client_phone = body.get("phone", "")
            service_name = body.get("serviceName", "Servicio")
            order_num = body.get("orderNumber", "ORD-N/A")
            
            # A. Buscar cuenta libre en stock para esa variación
            try:
                r_stock = requests.get(
                    f"{BASE_URL}/inventory/licenses",
                    headers=headers,
                    params={"variationId": vid, "status": "AVAILABLE", "limit": 1},
                    timeout=10
                )
                avail_items = r_stock.json().get("data", []) if r_stock.status_code == 200 else []
                if not avail_items:
                    self._send_json({
                        "ok": False,
                        "error": "NO_STOCK",
                        "message": f"⚠️ Sin stock disponible en NuVlyx para {service_name}. Por favor carga inventario."
                    }, 400)
                    return
                
                new_license = avail_items[0]
                new_lid = new_license["id"]
                
                # B. Obtener credenciales de la nueva cuenta
                r_cred = requests.get(f"{BASE_URL}/inventory/licenses/{new_lid}/credential", headers=headers, timeout=10)
                raw_cred = r_cred.json().get("credential", "") if r_cred.status_code == 200 else ""
                c_email, c_pass, c_prof, c_pin = parse_credential_text(raw_cred)
                if not c_email and new_license.get("accountEmail"):
                    c_email = new_license["accountEmail"]
                    
                # C. Si hay orderId, ejecutar warranty-replace en NuVlyx
                if order_id:
                    try:
                        r_ord = requests.get(f"{BASE_URL}/orders/{order_id}", headers=headers, timeout=10)
                        if r_ord.status_code == 200:
                            items = r_ord.json().get("items", [])
                            if items:
                                item_id = items[0]["id"]
                                w_payload = {
                                    "mode": "SELECT_EXISTING",
                                    "licenseId": new_lid,
                                    "reason": "Cuenta caída reemplazada desde Stream Zone Panel"
                                }
                                requests.post(f"{BASE_URL}/orders/{order_id}/items/{item_id}/warranty-replace", json=w_payload, headers=headers, timeout=12)
                    except Exception as e:
                        print("Warning executing warranty-replace in NuVlyx:", e)

                # D. Redactar mensaje tipo reasignación en el orden solicitado:
                # Correo, Contraseña, Orden, PIN (y Perfil)
                new_exp = (datetime.now(TZ_COLOMBIA) + timedelta(days=30)).strftime("%d/%m/%Y")
                wa_message = (
                    f"👋 ¡Hola {client_name}! Te saludamos desde *Stream Zone*.\n\n"
                    f"⚡ *Actualización de tu cuenta / Reasignación*:\n"
                    f"Te entregamos tus nuevos datos de acceso para que continúes disfrutando de tu servicio sin interrupciones:\n\n"
                    f"✨ *Datos de tu servicio*:\n"
                    f"📌 *Servicio*: {service_name}\n"
                    f"📧 *Correo*: {c_email or 'N/A'}\n"
                    f"{acceso_line(c_pass)}\n"
                    f"🧾 *Nº de Orden*: {order_num}\n"
                    f"👤 *Perfil*: {c_prof or 'Principal'}\n"
                    f"🔒 *PIN*: {c_pin or 'N/A'}\n"
                    f"📅 *Fecha de Vencimiento*: {new_exp}\n\n"
                    f"💡 Recuerda no modificar la información ajena a tu perfil. ¡Gracias por confiar en nosotros! 🙌"
                )

                # E. Guardar en base de datos local
                now_str = datetime.now(TZ_COLOMBIA).isoformat()
                with sqlite3.connect(DB_PATH) as conn:
                    conn.execute("""
                        INSERT INTO actions (license_id, status, reassigned_license_id, notes, updated_at)
                        VALUES (?, 'REASSIGNED', ?, ?, ?)
                        ON CONFLICT(license_id) DO UPDATE SET
                        status='REASSIGNED', reassigned_license_id=?, notes=?, updated_at=?
                    """, (lid, new_lid, f"Reemplazado por {c_email}", now_str, new_lid, f"Reemplazado por {c_email}", now_str))
                    conn.commit()

                self._send_json({
                    "ok": True,
                    "status": "REASSIGNED",
                    "newLicenseId": new_lid,
                    "message": wa_message,
                    "credential": {
                        "email": c_email,
                        "password": c_pass,
                        "profile": c_prof,
                        "pin": c_pin
                    }
                })
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, 500)

        # 3. ACCIÓN: NO RENOVÓ -> VOLVER CUENTA VIVA A STOCK EN NUVLYX
        elif path == "/api/not-renewed-stock":
            lid = body.get("licenseId")
            vid = body.get("variationId")
            now_str = datetime.now(TZ_COLOMBIA).isoformat()
            
            raw_cred = CACHE_CREDENTIALS.get(lid)
            if not raw_cred:
                try:
                    r_cred = requests.get(f"{BASE_URL}/inventory/licenses/{lid}/credential", headers=headers, timeout=8)
                    if r_cred.status_code == 200:
                        raw_cred = r_cred.json().get("credential", "")
                except Exception:
                    pass
            
            # Subir de nuevo como AVAILABLE a NuVlyx para nueva venta
            if raw_cred and vid:
                try:
                    requests.post(f"{BASE_URL}/inventory/licenses", json={"variationId": vid, "credentialData": raw_cred}, headers=headers, timeout=10)
                except Exception as e:
                    print("Error returning license to stock:", e)
            
            # Revocar la vieja licencia vendida para no duplicar
            try:
                requests.patch(f"{BASE_URL}/inventory/licenses/{lid}", json={"status": "REVOKED"}, headers=headers, timeout=8)
            except Exception:
                pass
                
            notes = "Cliente no renovó. Pantalla/cuenta viva devuelta al stock de NuVlyx para nueva venta."
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("""
                    INSERT INTO actions (license_id, status, notes, updated_at)
                    VALUES (?, 'RETURNED_TO_STOCK', ?, ?)
                    ON CONFLICT(license_id) DO UPDATE SET
                    status='RETURNED_TO_STOCK', notes=?, updated_at=?
                """, (lid, notes, now_str, notes, now_str))
                conn.commit()

            self._send_json({"ok": True, "status": "RETURNED_TO_STOCK", "notes": notes})

        # 4. ACCIÓN: SOLO PURGAR (LA CUENTA MURIÓ / SE CAYÓ)
        elif path == "/api/purge-single":
            lid = body.get("licenseId")
            now_str = datetime.now(TZ_COLOMBIA).isoformat()
            
            try:
                requests.patch(f"{BASE_URL}/inventory/licenses/{lid}", json={"status": "REVOKED"}, headers=headers, timeout=10)
            except Exception:
                pass
                
            notes = "Cuenta caída/muerta purgada y revocada de NuVlyx."
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("""
                    INSERT INTO actions (license_id, status, notes, updated_at)
                    VALUES (?, 'PURGED', ?, ?)
                    ON CONFLICT(license_id) DO UPDATE SET
                    status='PURGED', notes=?, updated_at=?
                """, (lid, notes, now_str, notes, now_str))
                conn.commit()

            self._send_json({"ok": True, "status": "PURGED", "notes": notes})

        # 4. ACCIÓN: ENVIAR WHATSAPP (DIRECTO CON WASEND)
        elif path == "/api/send-wa":
            phone = body.get("phone", "").replace("+", "").replace(" ", "").replace("-", "")
            msg = body.get("message", "")
            lid = body.get("licenseId")
            
            if not phone:
                self._send_json({"ok": False, "error": "Teléfono inválido"}, 400)
                return

            try:
                import subprocess
                cmd = ["wasend", "--to", phone, "--msg", msg]
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                
                if lid:
                    now_str = datetime.now(TZ_COLOMBIA).isoformat()
                    with sqlite3.connect(DB_PATH) as conn:
                        conn.execute("""
                            INSERT INTO actions (license_id, status, notes, updated_at)
                            VALUES (?, 'NOTIFIED', 'Aviso de cobro enviado por WhatsApp', ?)
                            ON CONFLICT(license_id) DO UPDATE SET
                            status='NOTIFIED', notes='Aviso de cobro enviado por WhatsApp', updated_at=?
                        """, (lid, now_str, now_str))
                        conn.commit()

                self._send_json({"ok": True, "output": res.stdout[:200]})
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, 500)

        # 5. ACCIÓN: PURGA MASIVA DE CUENTAS MUERTAS (> 7 DÍAS VENCIDAS)
        elif path == "/api/purge-dead":
            try:
                # Consultar licencias vencidas hace más de 7 días
                dead_date = (datetime.now(TZ_COLOMBIA) - timedelta(days=7)).strftime("%Y-%m-%d")
                r = requests.get(
                    f"{BASE_URL}/inventory/licenses",
                    headers=headers,
                    params={"status": "SOLD", "limit": 100},
                    timeout=12
                )
                purged_count = 0
                if r.status_code == 200:
                    for it in r.json().get("data", []):
                        exp = it.get("expiresAt", "")[:10]
                        if exp and exp < dead_date:
                            requests.patch(f"{BASE_URL}/inventory/licenses/{it['id']}", json={"status": "REVOKED"}, headers=headers, timeout=5)
                            purged_count += 1
                self._send_json({"ok": True, "purgedCount": purged_count})
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, 500)
        else:
            self.send_response(404)
            self.end_headers()

# ==============================================================================
# FRONTEND SPA (HTML5 + TAILWIND + LUCIDE)
# ==============================================================================
HTML_UI = """<!DOCTYPE html>
<html lang="es" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stream Zone • Panel de Control y Vencimientos</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            sz: {
              dark: '#0B0F19',
              card: '#111827',
              border: '#1F2937',
              blue: '#2563EB',
              cyan: '#06B6D4',
              emerald: '#10B981',
              rose: '#F43F5E',
              amber: '#F59E0B'
            }
          }
        }
      }
    }
  </script>
  <style>
    body { background-color: #0B0F19; color: #F3F4F6; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: #111827; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #374151; border-radius: 4px; }
  </style>
</head>
<body class="min-h-screen flex flex-col font-sans antialiased custom-scroll">

  <!-- TOP NAV -->
  <header class="border-b border-sz-border bg-sz-card/80 backdrop-blur sticky top-0 z-40 px-6 py-3 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-cyan-500 flex items-center justify-center font-extrabold text-white shadow-lg shadow-blue-500/20">
        SZ
      </div>
      <div>
        <h1 class="text-base font-bold text-white flex items-center gap-2">
          Stream Zone • Centro de Vencimientos
          <span class="text-xs px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-mono">NuVlyx Sync</span>
        </h1>
        <p class="text-xs text-gray-400">Control de renovaciones, cuentas caídas y purga de inventario</p>
      </div>
    </div>

    <!-- Acciones Globales -->
    <div class="flex items-center gap-3">
      <button onclick="toggleBatchNotify()" id="btn-batch-notify" class="text-xs font-bold px-3.5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white shadow-md shadow-emerald-600/30 flex items-center gap-1.5 transition">
        <i data-lucide="send" class="w-3.5 h-3.5"></i>
        <span>Avisar a Todos</span>
      </button>
      <button onclick="purgeDeadAccounts()" class="text-xs font-semibold px-3 py-2 rounded-lg bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/30 flex items-center gap-1.5 transition">
        <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
        Purgar Cuentas Muertas (>7d)
      </button>
      <button onclick="loadData()" class="text-xs font-semibold px-3.5 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-600/30 flex items-center gap-1.5 transition">
        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
        Actualizar Datos
      </button>
    </div>

  </header>

  <!-- CONTENEDOR PRINCIPAL -->
  <main class="flex-1 p-6 max-w-7xl mx-auto w-full space-y-6">

    <!-- KPI CARDS -->
    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-2.5" id="kpi-container">
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-gray-400">En Ventana</div>
        <div class="text-lg font-extrabold text-white mt-1" id="kpi-total">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-rose-400 flex items-center gap-1">
          <i data-lucide="alert-circle" class="w-3 h-3"></i> Vence Hoy
        </div>
        <div class="text-lg font-extrabold text-rose-400 mt-1" id="kpi-dueToday">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-amber-400 flex items-center gap-1">
          <i data-lucide="clock" class="w-3 h-3"></i> Mañana
        </div>
        <div class="text-lg font-extrabold text-amber-400 mt-1" id="kpi-dueTomorrow">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-red-500">Vencidos</div>
        <div class="text-lg font-extrabold text-red-500 mt-1" id="kpi-expired">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-emerald-400 flex items-center gap-1">
          <i data-lucide="check-circle" class="w-3 h-3"></i> Renovados
        </div>
        <div class="text-lg font-extrabold text-emerald-400 mt-1" id="kpi-renewed">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-indigo-400 flex items-center gap-1">
          <i data-lucide="corner-down-left" class="w-3 h-3"></i> A Stock
        </div>
        <div class="text-lg font-extrabold text-indigo-300 mt-1" id="kpi-returnedToStock">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-cyan-400 flex items-center gap-1">
          <i data-lucide="repeat" class="w-3 h-3"></i> Reasignados
        </div>
        <div class="text-lg font-extrabold text-cyan-400 mt-1" id="kpi-reassigned">0</div>
      </div>
      <div class="p-3 rounded-xl bg-sz-card border border-sz-border">
        <div class="text-[11px] font-medium text-red-400 flex items-center gap-1">
          <i data-lucide="trash-2" class="w-3 h-3"></i> Purgadas
        </div>
        <div class="text-lg font-extrabold text-red-400 mt-1" id="kpi-purged">0</div>
      </div>
    </div>

    <!-- BARRA DE BÚSQUEDA Y FILTROS -->
    <div class="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3 bg-sz-card p-3 rounded-xl border border-sz-border">
      <!-- Buscador -->
      <div class="relative flex-1">
        <i data-lucide="search" class="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
        <input type="text" id="search-input" oninput="filterRecords()" placeholder="Buscar por cliente, teléfono, servicio, correo u orden..." class="w-full bg-sz-dark border border-sz-border rounded-lg pl-9 pr-4 py-2 text-sm text-gray-200 placeholder-gray-500 focus:outline-none focus:border-blue-500 transition">
      </div>

      <!-- Filtros de Pestañas -->
      <div class="flex items-center gap-1 overflow-x-auto pb-1 md:pb-0" id="filter-tabs">
        <button onclick="setFilter('ALL')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-semibold bg-blue-600 text-white transition" data-filter="ALL">Todos</button>
        <button onclick="setFilter('TODAY')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="TODAY">🚨 Vence Hoy</button>
        <button onclick="setFilter('TOMORROW')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="TOMORROW">⚠️ Mañana</button>
        <button onclick="setFilter('PENDING')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="PENDING">⏳ Pendientes</button>
        <button onclick="setFilter('RENEWED')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="RENEWED">✅ Renovados</button>
        <button onclick="setFilter('STOCK')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="STOCK">📦 A Stock</button>
        <button onclick="setFilter('REASSIGNED')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="REASSIGNED">🔄 Reasignados</button>
        <button onclick="setFilter('PURGED')" class="filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition" data-filter="PURGED">🗑️ Purgadas</button>
      </div>
    </div>

    <!-- TABLA PRINCIPAL DE VENCIMIENTOS -->
    <div class="bg-sz-card rounded-xl border border-sz-border overflow-hidden shadow-xl">
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-sz-border bg-sz-dark/50 text-gray-400 font-semibold uppercase tracking-wider text-[11px]">
              <th class="py-3 px-4">Cliente & Contacto</th>
              <th class="py-3 px-4">Servicio & Orden</th>
              <th class="py-3 px-4">Credenciales (NuVlyx)</th>
              <th class="py-3 px-4">Corte & Estado</th>
              <th class="py-3 px-4 text-right">Acciones Rápidas</th>
            </tr>
          </thead>
          <tbody id="records-table-body" class="divide-y divide-sz-border">
            <!-- Renderizado dinámico -->
          </tbody>
        </table>
      </div>

      <!-- Estado vacío -->
      <div id="empty-state" class="hidden py-16 text-center text-gray-400">
        <i data-lucide="inbox" class="w-10 h-10 mx-auto text-gray-600 mb-2"></i>
        <p class="font-medium">No hay suscripciones en este filtro</p>
      </div>
    </div>

  </main>

  <!-- MODAL: ENVIAR MENSAJE WHATSAPP / REASIGNACIÓN -->
  <div id="wa-modal" class="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-sz-card border border-sz-border rounded-2xl max-w-lg w-full p-6 shadow-2xl space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-sz-border">
        <h3 class="font-bold text-white text-base flex items-center gap-2" id="modal-title">
          <i data-lucide="message-square" class="w-5 h-5 text-emerald-400"></i> Despacho WhatsApp
        </h3>
        <button onclick="closeModal()" class="text-gray-400 hover:text-white">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div>
        <label class="text-xs font-semibold text-gray-400">Destinatario:</label>
        <div class="text-sm font-bold text-white mt-0.5" id="modal-recipient">+57 000 0000000</div>
      </div>

      <div>
        <label class="text-xs font-semibold text-gray-400">Mensaje a enviar:</label>
        <textarea id="modal-message-text" rows="8" class="w-full bg-sz-dark border border-sz-border rounded-xl p-3 text-xs font-mono text-gray-200 mt-1 focus:outline-none focus:border-blue-500"></textarea>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2">
        <button onclick="closeModal()" class="px-4 py-2 rounded-xl text-xs font-semibold text-gray-400 hover:text-white bg-sz-dark">Cancelar</button>
        <button onclick="sendWaFromModal()" class="px-4 py-2 rounded-xl text-xs font-bold text-white bg-emerald-600 hover:bg-emerald-500 flex items-center gap-1.5 shadow-lg shadow-emerald-600/30">
          <i data-lucide="send" class="w-3.5 h-3.5"></i> Enviar por wasend
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toast" class="fixed bottom-5 right-5 z-50 hidden px-4 py-3 rounded-xl shadow-2xl text-xs font-bold flex items-center gap-2 border"></div>

  <script>
    let allRecords = [];
    let currentFilter = 'ALL';
    let activeModalLid = null;

    async function loadData() {
      showToast('Cargando datos en vivo de NuVlyx...', 'blue');
      try {
        const res = await fetch('/api/vencimientos');
        const data = await res.json();
        if (data.ok) {
          allRecords = data.records;
          filterRecords();
          loadStats();
          showToast('Sincronización completada', 'emerald');
        }
      } catch (e) {
        showToast('Error cargando datos: ' + e.message, 'rose');
      }
    }

    async function loadStats() {
      try {
        const res = await fetch('/api/stats');
        const data = await res.json();
        if (data.ok) {
          const s = data.stats;
          document.getElementById('kpi-total').innerText = s.total;
          document.getElementById('kpi-dueToday').innerText = s.dueToday;
          document.getElementById('kpi-dueTomorrow').innerText = s.dueTomorrow;
          document.getElementById('kpi-expired').innerText = s.expired;
          document.getElementById('kpi-renewed').innerText = s.renewed;
          document.getElementById('kpi-returnedToStock').innerText = s.returnedToStock || 0;
          document.getElementById('kpi-reassigned').innerText = s.reassigned;
          document.getElementById('kpi-purged').innerText = s.purged || 0;
        }
      } catch (e) {}
    }

    function setFilter(filter) {
      currentFilter = filter;
      document.querySelectorAll('.filter-tab').forEach(el => {
        if (el.getAttribute('data-filter') === filter) {
          el.className = 'filter-tab px-3 py-1.5 rounded-lg text-xs font-semibold bg-blue-600 text-white transition';
        } else {
          el.className = 'filter-tab px-3 py-1.5 rounded-lg text-xs font-medium text-gray-400 hover:text-white hover:bg-sz-dark transition';
        }
      });
      filterRecords();
    }

    function filterRecords() {
      const q = document.getElementById('search-input').value.toLowerCase().trim();
      const filtered = allRecords.filter(r => {
        // Filtro de búsqueda
        const matchQ = !q || (
          r.clientName.toLowerCase().includes(q) ||
          r.phone.toLowerCase().includes(q) ||
          r.serviceName.toLowerCase().includes(q) ||
          r.orderNumber.toLowerCase().includes(q) ||
          r.email.toLowerCase().includes(q)
        );

        // Si está en stock o purgada, se considera archivada/resuelta y desaparece de la lista activa
        const isResolved = r.status === 'RETURNED_TO_STOCK' || r.status === 'PURGED';

        // Filtro de pestaña
        let matchTab = true;
        if (currentFilter === 'ALL') matchTab = !isResolved;
        else if (currentFilter === 'TODAY') matchTab = r.diffDays === 0 && !isResolved;
        else if (currentFilter === 'TOMORROW') matchTab = r.diffDays === 1 && !isResolved;
        else if (currentFilter === 'PENDING') matchTab = (r.status === 'PENDING' || r.status === 'NOTIFIED') && !isResolved;
        else if (currentFilter === 'RENEWED') matchTab = r.status === 'RENEWED';
        else if (currentFilter === 'STOCK') matchTab = r.status === 'RETURNED_TO_STOCK';
        else if (currentFilter === 'REASSIGNED') matchTab = r.status === 'REASSIGNED';
        else if (currentFilter === 'PURGED') matchTab = r.status === 'PURGED';
        else if (currentFilter === 'NOT_RENEWED') matchTab = isResolved || r.status === 'NOT_RENEWED';

        return matchQ && matchTab;
      });

      renderTable(filtered);
    }

    function renderTable(records) {
      const tbody = document.getElementById('records-table-body');
      const empty = document.getElementById('empty-state');
      tbody.innerHTML = '';

      if (records.length === 0) {
        empty.classList.remove('hidden');
        return;
      }
      empty.classList.add('hidden');

      records.forEach(r => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-sz-dark/40 transition group';

        // Badge de estado local
        let statusBadge = '';
        if (r.status === 'RENEWED') {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold"><i data-lucide="check" class="w-3 h-3"></i> Renovado</span>`;
        } else if (r.status === 'RETURNED_TO_STOCK') {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-bold"><i data-lucide="corner-down-left" class="w-3 h-3"></i> En Stock (Viva)</span>`;
        } else if (r.status === 'REASSIGNED') {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 font-bold"><i data-lucide="repeat" class="w-3 h-3"></i> Reasignado</span>`;
        } else if (r.status === 'PURGED') {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-red-500/10 text-red-400 border border-red-500/20 font-bold"><i data-lucide="trash-2" class="w-3 h-3"></i> Purgada (Muerta)</span>`;
        } else if (r.status === 'NOTIFIED') {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-bold"><i data-lucide="send" class="w-3 h-3"></i> Avisado</span>`;
        } else {
          statusBadge = `<span class="inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-400 border border-amber-500/20 font-bold"><i data-lucide="clock" class="w-3 h-3"></i> Pendiente</span>`;
        }

        // Color badge corte
        let badgeClass = 'bg-blue-500/10 text-blue-400 border-blue-500/20';
        if (r.badgeColor === 'red') badgeClass = 'bg-red-500/10 text-red-400 border-red-500/20';
        if (r.badgeColor === 'rose') badgeClass = 'bg-rose-500/10 text-rose-400 border-rose-500/20 font-bold animate-pulse';
        if (r.badgeColor === 'amber') badgeClass = 'bg-amber-500/10 text-amber-400 border-amber-500/20 font-bold';

        tr.innerHTML = `
          <!-- Cliente -->
          <td class="py-3.5 px-4">
            <div class="font-bold text-white text-sm flex items-center gap-1.5">
              ${r.clientName}
            </div>
            <div class="text-gray-400 font-mono text-[11px] mt-0.5 flex items-center gap-2">
              <span>+${r.phone}</span>
              ${r.phone ? `<a href="https://wa.me/${r.phone.replace(/[^0-9]/g, '')}" target="_blank" class="text-emerald-400 hover:underline flex items-center gap-0.5"><i data-lucide="external-link" class="w-3 h-3"></i> Chat</a>` : ''}
            </div>
            ${r.walletBalance > 0 ? `
              <div class="mt-1.5 inline-flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full ${r.walletBalance >= r.price && r.price > 0 ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 font-semibold' : 'bg-amber-500/10 text-amber-300 border border-amber-500/20'}">
                <i data-lucide="wallet" class="w-2.5 h-2.5"></i>
                Saldo: $${Number(r.walletBalance).toLocaleString('es-CO')} ${r.walletBalance >= r.price && r.price > 0 ? '✓ (Recargado)' : ''}
              </div>
            ` : `
              <div class="mt-1 text-[10px] text-gray-500 flex items-center gap-1">
                <i data-lucide="wallet" class="w-2.5 h-2.5"></i> Saldo: $0
              </div>
            `}
          </td>

          <!-- Servicio & Orden -->
          <td class="py-3.5 px-4">
            <div class="font-bold text-gray-200 text-xs">${r.serviceName}</div>
            <div class="text-[11px] text-gray-400 font-mono mt-0.5 flex items-center gap-2">
              <span>${r.orderNumber}</span>
              ${r.price > 0 ? `<span class="text-blue-400 font-semibold">$${Number(r.price).toLocaleString('es-CO')}</span>` : ''}
            </div>
          </td>

          <!-- Credenciales -->
          <td class="py-3.5 px-4 font-mono text-[11px]">
            <div class="text-gray-300 truncate max-w-[200px]" title="${r.email}">${r.email}</div>
            <div class="text-gray-400 flex items-center gap-2 mt-0.5">
              <span>${/^https?:\\/\\//i.test(r.password||'') ? 'Link' : 'Pass'}: <strong class="text-gray-200">${r.password}</strong></span>
              <span>P: <strong class="text-gray-200">${r.profile}</strong></span>
              <span>PIN: <strong class="text-gray-200">${r.pin}</strong></span>
            </div>
          </td>

          <!-- Corte & Días -->
          <td class="py-3.5 px-4">
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full text-[11px] border ${badgeClass}">
                ${r.badgeLabel}
              </span>
              ${statusBadge}
            </div>
            <div class="text-gray-400 text-[11px] font-mono mt-1">Corte: ${r.expiresAt}</div>
          </td>

          <!-- Acciones Rápidas -->
          <td class="py-3.5 px-4 text-right">
            <div class="flex items-center justify-end gap-1.5">
              <!-- 1. Avisar Cobro -->
              <button onclick="openNotifyModal('${r.licenseId}')" title="Enviar cobro por WhatsApp" class="p-1.5 rounded-lg bg-sz-dark hover:bg-sz-border text-gray-300 hover:text-white border border-sz-border transition">
                <i data-lucide="message-square" class="w-4 h-4"></i>
              </button>

              <!-- 2. Renovó (Cuenta viva: Extender +30d) -->
              <button onclick="actionRenew('${r.licenseId}')" title="Renovó (Cuenta viva: Extender +30 días en NuVlyx)" class="px-2 py-1.5 rounded-lg bg-emerald-600/20 hover:bg-emerald-600/40 text-emerald-400 border border-emerald-600/30 text-xs font-bold flex items-center gap-1 transition">
                <i data-lucide="check" class="w-3.5 h-3.5"></i> Renovó
              </button>

              <!-- 3. No Renovó -> Vuelve a Stock (Cuenta viva) -->
              <button onclick="actionNoRenovoStock('${r.licenseId}')" title="No renovó (Cuenta viva: Devolver a stock de NuVlyx para nueva venta)" class="px-2 py-1.5 rounded-lg bg-indigo-600/20 hover:bg-indigo-600/40 text-indigo-400 border border-indigo-600/30 text-xs font-bold flex items-center gap-1 transition">
                <i data-lucide="corner-down-left" class="w-3.5 h-3.5"></i> A Stock
              </button>

              <!-- 4. Purgar y Reasignar (Cuenta murió) -->
              <button onclick="actionReassign('${r.licenseId}')" title="Cuenta cayó/murió: Purgar y Reasignar una nueva de stock" class="px-2 py-1.5 rounded-lg bg-cyan-600/20 hover:bg-cyan-600/40 text-cyan-400 border border-cyan-600/30 text-xs font-bold flex items-center gap-1 transition">
                <i data-lucide="repeat" class="w-3.5 h-3.5"></i> Reasignar
              </button>

              <!-- 5. Solo Purgar (Cuenta murió) -->
              <button onclick="actionSoloPurgar('${r.licenseId}')" title="Cuenta cayó/murió: Solo purgar/revocar en NuVlyx" class="p-1.5 rounded-lg bg-red-600/10 hover:bg-red-600/30 text-red-400 border border-red-600/30 transition">
                <i data-lucide="trash-2" class="w-4 h-4"></i>
              </button>
            </div>
          </td>
        `;

        tbody.appendChild(tr);
      });
      lucide.createIcons();
    }

    // ==========================================
    // ACCIONES
    // ==========================================
    async function actionRenew(lid) {
      const rec = allRecords.find(r => r.licenseId === lid);
      const hasBalance = rec.walletBalance >= rec.price && rec.price > 0;
      
      let confirmMsg = `¿Confirmar renovación de ${rec.clientName} (${rec.serviceName})? Se extenderá +30 días.\\n\\n`;
      if (hasBalance) {
        confirmMsg += `💰 CLIENTE TIENE SALDO:\\nSaldo disponible: $${Number(rec.walletBalance).toLocaleString('es-CO')}\\nPrecio servicio: $${Number(rec.price).toLocaleString('es-CO')}\\n\\n¿Deseas descontar automáticamente $${Number(rec.price).toLocaleString('es-CO')} de su billetera web?`;
      } else if (rec.price > 0) {
        confirmMsg += `⚠️ Saldo web insuficiente: $${Number(rec.walletBalance).toLocaleString('es-CO')} (Precio: $${Number(rec.price).toLocaleString('es-CO')}).\\n¿Deseas renovar y registrar la extensión sin descuento de saldo?`;
      } else {
        confirmMsg += `¿Continuar con la extensión?`;
      }

      if (!confirm(confirmMsg)) return;

      showToast('Procesando renovación...', 'blue');
      try {
        const res = await fetch('/api/renew', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            licenseId: lid,
            clientId: rec.clientId,
            price: rec.price,
            serviceName: rec.serviceName,
            orderNumber: rec.orderNumber,
            days: 30,
            deductWallet: hasBalance
          })
        });
        const data = await res.json();
        if (data.ok) {
          rec.status = 'RENEWED';
          rec.extendedUntil = data.extendedUntil;
          if (data.deducted) {
            rec.walletBalance = Math.max(0, rec.walletBalance - data.deductedAmount);
          }
          filterRecords();
          loadStats();
          const walletMsg = data.deducted ? ` y descontados $${Number(data.deductedAmount).toLocaleString('es-CO')} de billetera web` : '';
          showToast(`✅ Renovado exitosamente hasta el ${data.extendedUntil}${walletMsg}`, 'emerald');
        } else {
          showToast(data.message || 'Error renovando', 'rose');
        }
      } catch (e) {
        showToast('Error: ' + e.message, 'rose');
      }
    }

    async function actionNoRenovoStock(lid) {
      const rec = allRecords.find(r => r.licenseId === lid);
      if (!confirm(`¿Confirmar que ${rec.clientName} NO RENOVÓ?\\n\\nLa cuenta está VIVA. Se devolverá al stock disponible de NuVlyx para venderse a otro cliente.`)) return;

      showToast('Devolviendo cuenta viva a stock en NuVlyx...', 'indigo');
      try {
        const res = await fetch('/api/not-renewed-stock', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ licenseId: lid, variationId: rec.variationId })
        });
        const data = await res.json();
        if (data.ok) {
          rec.status = 'RETURNED_TO_STOCK';
          filterRecords();
          loadStats();
          showToast(`📦 Cuenta devuelta al stock de NuVlyx con éxito`, 'emerald');
        } else {
          showToast(data.message || 'Error devolviendo a stock', 'rose');
        }
      } catch (e) {
        showToast('Error: ' + e.message, 'rose');
      }
    }

    async function actionSoloPurgar(lid) {
      const rec = allRecords.find(r => r.licenseId === lid);
      if (!confirm(`¿PURGAR cuenta de ${rec.clientName}?\\n\\nLa cuenta MURIÓ / CAYÓ. Se marcará como REVOCADA en NuVlyx (solo purga, sin reasignar).`)) return;

      showToast('Purgando y revocando cuenta en NuVlyx...', 'rose');
      try {
        const res = await fetch('/api/purge-single', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ licenseId: lid })
        });
        const data = await res.json();
        if (data.ok) {
          rec.status = 'PURGED';
          filterRecords();
          loadStats();
          showToast(`🗑️ Cuenta muerta purgada en NuVlyx`, 'emerald');
        } else {
          showToast(data.message || 'Error purgando cuenta', 'rose');
        }
      } catch (e) {
        showToast('Error: ' + e.message, 'rose');
      }
    }

    async function actionReassign(lid) {
      const rec = allRecords.find(r => r.licenseId === lid);
      if (!confirm(`¿Reasignar cuenta para ${rec.clientName}? Se tomará una cuenta nueva de stock en NuVlyx para ${rec.serviceName}.`)) return;

      showToast('Consultando stock y reasignando cuenta...', 'cyan');
      try {
        const res = await fetch('/api/reassign', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            licenseId: lid,
            variationId: rec.variationId,
            orderId: rec.orderId,
            orderNumber: rec.orderNumber,
            clientName: rec.clientName,
            phone: rec.phone,
            serviceName: rec.serviceName
          })
        });
        const data = await res.json();
        if (data.ok) {
          rec.status = 'REASSIGNED';
          filterRecords();
          loadStats();
          // Abrir modal con el mensaje formateado en el orden pedido
          activeModalLid = lid;
          document.getElementById('modal-title').innerHTML = '<i data-lucide="repeat" class="w-5 h-5 text-cyan-400"></i> Despacho de Reasignación';
          document.getElementById('modal-recipient').innerText = `${rec.clientName} (+${rec.phone})`;
          document.getElementById('modal-message-text').value = data.message;
          document.getElementById('wa-modal').classList.remove('hidden');
          lucide.createIcons();
          showToast('✅ Cuenta reasignada con éxito. Revisa el mensaje antes de enviar.', 'emerald');
        } else {
          showToast(data.message || 'Error en reasignación', 'rose');
        }
      } catch (e) {
        showToast('Error: ' + e.message, 'rose');
      }
    }

    function openNotifyModal(lid) {
      const rec = allRecords.find(r => r.licenseId === lid);
      activeModalLid = lid;
      const priceStr = rec.price > 0 ? ` ($${Number(rec.price).toLocaleString('es-CO')})` : '';
      const msg = 
        `👋 ¡Hola ${rec.clientName}! Esperamos que estés disfrutando de tu servicio.\\n\\n` +
        `⚡ Te informamos desde *Stream Zone* sobre el estado de tu cuenta:\\n` +
        `⏳ Días restantes: *${rec.badgeLabel}* (Corte: ${rec.expiresAt}).\\n\\n` +
        `✨ *Detalles de tu servicio*:\\n` +
        `📌 *Servicio*: ${rec.serviceName}\\n` +
        `📧 *Correo*: ${rec.email}\\n` +
        `${/^https?:\\/\\//i.test(rec.password || '') ? '🔗 *Enlace*' : '🔑 *Contraseña*'}: ${rec.password || 'N/A'}\\n` +
        `🧾 *Nº de Orden*: ${rec.orderNumber}\\n` +
        `👤 *Perfil*: ${rec.profile}\\n` +
        `🔒 *PIN*: ${rec.pin}\\n` +
        `📅 *Fecha de Vencimiento*: ${rec.expiresAt}\\n\\n` +
        `💡 *¿Cómo renovar?*:\\n` +
        `Si deseas renovar tu cuenta, por favor recarga el valor exacto${priceStr} directamente en tu cuenta de la página web y confírmanos por aquí para procesar tu renovación y aplicar el descuento.\\n\\n` +
        `⚠️ *(Ten presente que no responder o no confirmar a tiempo se tomará como no renovación y se procederá al corte habitual).*\\n\\n` +
        `¡Muchas gracias por tu preferencia! 🙌`;

      document.getElementById('modal-title').innerHTML = '<i data-lucide="message-square" class="w-5 h-5 text-emerald-400"></i> Despacho de Cobro';
      document.getElementById('modal-recipient').innerText = `${rec.clientName} (+${rec.phone})`;
      document.getElementById('modal-message-text').value = msg;
      document.getElementById('wa-modal').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeModal() {
      document.getElementById('wa-modal').classList.add('hidden');
      activeModalLid = null;
    }

    async function sendWaFromModal() {
      const rec = allRecords.find(r => r.licenseId === activeModalLid);
      const text = document.getElementById('modal-message-text').value;
      showToast('Enviando mensaje con wasend...', 'blue');
      closeModal();
      
      try {
        const res = await fetch('/api/send-wa', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ phone: rec.phone, message: text, licenseId: rec.licenseId })
        });
        const data = await res.json();
        if (data.ok) {
          rec.status = 'NOTIFIED';
          filterRecords();
          loadStats();
          showToast(`✅ Mensaje despachado a +${rec.phone}`, 'emerald');
        } else {
          showToast('Error enviando mensaje: ' + (data.error || 'falló wasend'), 'rose');
        }
      } catch (e) {
        showToast('Error: ' + e.message, 'rose');
      }
    }

    let isBatchRunning = false;
    let shouldStopBatch = false;

    async function toggleBatchNotify() {
      if (isBatchRunning) {
        shouldStopBatch = true;
        showToast('Deteniendo envío masivo...', 'amber');
        return;
      }

      // Filtrar clientes pendientes según la vista actual
      const pending = allRecords.filter(r => {
        const isMatch = (
          (currentFilter === 'ALL') ||
          (currentFilter === 'TODAY' && r.diffDays === 0) ||
          (currentFilter === 'TOMORROW' && r.diffDays === 1) ||
          (currentFilter === 'PENDING')
        );
        return isMatch && r.status === 'PENDING' && r.phone;
      });

      if (pending.length === 0) {
        showToast('No hay clientes pendientes por avisar en esta vista', 'amber');
        return;
      }

      if (!confirm(`¿Deseas enviar avisos de cobro por WhatsApp a los ${pending.length} clientes pendientes?\\n\\nSe enviará 1 mensaje cada 4 segundos con protección anti-spam.`)) {
        return;
      }

      isBatchRunning = true;
      shouldStopBatch = false;
      const btn = document.getElementById('btn-batch-notify');
      const originalHTML = btn.innerHTML;

      let sentCount = 0;
      let errorCount = 0;

      for (let i = 0; i < pending.length; i++) {
        if (shouldStopBatch) {
          showToast(`Envío detenido. Se enviaron ${sentCount} avisos.`, 'amber');
          break;
        }

        const rec = pending[i];
        btn.innerHTML = `<i data-lucide="loader-2" class="w-3.5 h-3.5 animate-spin"></i> <span>[Detener] (${i + 1}/${pending.length})</span>`;
        lucide.createIcons();

        const priceStr = rec.price > 0 ? ` ($${Number(rec.price).toLocaleString('es-CO')})` : '';
        const msg = 
          `👋 ¡Hola ${rec.clientName}! Esperamos que estés disfrutando de tu servicio.\\n\\n` +
          `⚡ Te informamos desde *Stream Zone* sobre el estado de tu cuenta:\\n` +
          `⏳ Días restantes: *${rec.badgeLabel}* (Corte: ${rec.expiresAt}).\\n\\n` +
          `✨ *Detalles de tu servicio*:\\n` +
          `📌 *Servicio*: ${rec.serviceName}\\n` +
          `📧 *Correo*: ${rec.email}\\n` +
          `${/^https?:\\/\\//i.test(rec.password || '') ? '🔗 *Enlace*' : '🔑 *Contraseña*'}: ${rec.password || 'N/A'}\\n` +
          `🧾 *Nº de Orden*: ${rec.orderNumber}\\n` +
          `👤 *Perfil*: ${rec.profile}\\n` +
          `🔒 *PIN*: ${rec.pin}\\n` +
          `📅 *Fecha de Vencimiento*: ${rec.expiresAt}\\n\\n` +
          `💡 *¿Cómo renovar?*:\\n` +
          `Si deseas renovar tu cuenta, por favor recarga el valor exacto${priceStr} directamente en tu cuenta de la página web y confírmanos por aquí para procesar tu renovación y aplicar el descuento.\\n\\n` +
          `⚠️ *(Ten presente que no responder o no confirmar a tiempo se tomará como no renovación y se procederá al corte habitual).*\\n\\n` +
          `¡Muchas gracias por tu preferencia! 🙌`;

        try {
          const res = await fetch('/api/send-wa', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ phone: rec.phone, message: msg, licenseId: rec.licenseId })
          });
          const data = await res.json();
          if (data.ok) {
            rec.status = 'NOTIFIED';
            sentCount++;
            filterRecords();
            loadStats();
          } else {
            errorCount++;
          }
        } catch (e) {
          errorCount++;
        }

        if (i < pending.length - 1 && !shouldStopBatch) {
          await new Promise(r => setTimeout(r, 4000));
        }
      }

      isBatchRunning = false;
      btn.innerHTML = originalHTML;
      lucide.createIcons();

      if (!shouldStopBatch) {
        showToast(`🎉 ¡Lote finalizado! ${sentCount} avisados, ${errorCount} fallidos.`, 'emerald');
      }
    }

    async function purgeDeadAccounts() {
      if (!confirm('¿Deseas purgar y revocar todas las cuentas vencidas hace más de 7 días para limpiar el inventario en NuVlyx?')) return;
      showToast('Purgando cuentas muertas en NuVlyx...', 'amber');
      try {
        const res = await fetch('/api/purge-dead', { method: 'POST' });
        const data = await res.json();
        if (data.ok) {
          showToast(`🧹 Purga finalizada: ${data.purgedCount} cuentas revocadas y limpiadas.`, 'emerald');
          loadData();
        }
      } catch (e) {
        showToast('Error en purga: ' + e.message, 'rose');
      }
    }

    function showToast(text, color = 'blue') {
      const t = document.getElementById('toast');
      t.innerText = text;
      let colorClass = 'bg-blue-600 text-white border-blue-500';
      if (color === 'emerald') colorClass = 'bg-emerald-600 text-white border-emerald-500';
      if (color === 'rose') colorClass = 'bg-rose-600 text-white border-rose-500';
      if (color === 'amber') colorClass = 'bg-amber-600 text-white border-amber-500';
      if (color === 'cyan') colorClass = 'bg-cyan-600 text-white border-cyan-500';
      t.className = `fixed bottom-5 right-5 z-50 px-4 py-3 rounded-xl shadow-2xl text-xs font-bold flex items-center gap-2 border ${colorClass}`;
      t.classList.remove('hidden');
      setTimeout(() => t.classList.add('hidden'), 4000);
    }

    // Inicializar
    document.addEventListener('DOMContentLoaded', () => {
      loadData();
      lucide.createIcons();
    });
  </script>
</body>
</html>
"""

def main():
    print(f"🚀 Iniciando Stream Zone Panel en http://localhost:{PORT}")
    server = ThreadingHTTPServer(("0.0.0.0", PORT), SzPanelHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido.")

if __name__ == "__main__":
    main()
