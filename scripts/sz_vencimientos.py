#!/usr/bin/env python3
import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_URL = "https://api.nuvlyx.com/api/v1"
TENANT_SLUG = "stream-zone-6822"
CACHE_TOKEN_PATH = "/home/rootkit/.cache/sz_admin_token.json"
TARGET_VARIATION_ID = "2692898b-c80d-4b76-9e11-a31420f397cc"

# Hora Colombia (UTC-5)
TZ_COLOMBIA = timezone(timedelta(hours=-5))
NOW_LOCAL = datetime.now(TZ_COLOMBIA)
TODAY = NOW_LOCAL.date()

def login_nuvlyx():
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
        tenant = data.get("user", {}).get("tenantSlug", TENANT_SLUG)
        cache_data = {
            "accessToken": token,
            "tenantSlug": tenant,
            "user": data.get("user"),
            "email": "jnsierra@jdc.edu.co"
        }
        os.makedirs(os.path.dirname(CACHE_TOKEN_PATH), exist_ok=True)
        with open(CACHE_TOKEN_PATH, "w") as f:
            json.dump(cache_data, f, indent=2)
        return token
    raise RuntimeError(f"Error al autenticar en NuVlyx: {r.text}")

def get_auth_headers():
    token = None
    if os.path.exists(CACHE_TOKEN_PATH):
        try:
            with open(CACHE_TOKEN_PATH) as f:
                token = json.load(f).get("accessToken")
        except Exception:
            token = None
    if not token:
        token = login_nuvlyx()
        
    return {
        "Authorization": f"Bearer {token}",
        "x-tenant-slug": TENANT_SLUG,
        "Content-Type": "application/json"
    }

headers = get_auth_headers()

# 1. Catálogo de productos
print("📦 [1/5] Obteniendo catálogo de productos en tiempo real...")
r_prod = requests.get(f"{BASE_URL}/products", headers=headers, timeout=15)
if r_prod.status_code == 401:
    print("   🔄 Token expirado, renovando sesión automáticamente...")
    login_nuvlyx()
    headers = get_auth_headers()
    r_prod = requests.get(f"{BASE_URL}/products", headers=headers, timeout=15)

products_data = r_prod.json()
variations_map = {}
for p in products_data:
    for v in p.get("variations", []):
        variations_map[v["id"]] = {
            "product_id": p.get("id"),
            "product_name": p.get("name"),
            "variation_name": v.get("name", "1 mes"),
            "full_name": f"{p.get('name')} ({v.get('name', '1 mes')})"
        }

print(f"   Catálogo mapeado: {len(products_data)} productos activos.")

# 2. Paginación de licencias SOLD
# Rango dinámico: desde ayer (vencidos recientes) hasta hoy + 4 días
START_DATE = TODAY - timedelta(days=1)
END_DATE = TODAY + timedelta(days=4)
start_str = START_DATE.strftime("%Y-%m-%d")
end_str = END_DATE.strftime("%Y-%m-%d")

print(f"🔍 [2/5] Filtrando suscripciones vendidas con corte entre {start_str} y {end_str}...")
page = 1
all_sold = []

while True:
    r = requests.get(
        f"{BASE_URL}/inventory/licenses",
        headers=headers,
        params={"status": "SOLD", "page": page, "limit": 100},
        timeout=15
    )
    if r.status_code != 200:
        break
    data = r.json()
    items = data.get("data", [])
    if not items:
        break
    
    for it in items:
        exp = it.get("expiresAt")
        if exp:
            d_str = exp[:10]
            if start_str <= d_str <= end_str:
                all_sold.append(it)
    
    meta = data.get("meta", {})
    if page >= meta.get("totalPages", 1):
        break
    page += 1

print(f"   Suscripciones en ventana de corte (0 a 4 días): {len(all_sold)}")

# 3. Descarga concurrente de credenciales y perfiles de clientes
print("⚡ [3/5] Descargando credenciales y teléfonos de clientes en paralelo...")

def parse_credential_text(c_text):
    if not c_text:
        return "", "", "N/A", "N/A"
    m_email = re.search(r"(?:correo|usuario|user|email):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_pass = re.search(r"(?:contrase[ñn]a|clave|pass|password):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_prof = re.search(r"(?:perfil|profile):\s*([^\s;]+)", c_text, re.IGNORECASE)
    m_pin = re.search(r"(?:pin|c[oó]digo):\s*([^\s;]+)", c_text, re.IGNORECASE)
    
    c_email = m_email.group(1).strip() if m_email else ""
    c_pass = m_pass.group(1).strip() if m_pass else ""
    c_prof = m_prof.group(1).strip() if m_prof else "N/A"
    c_pin = m_pin.group(1).strip() if m_pin else "N/A"
    return c_email, c_pass, c_prof, c_pin

credentials_cache = {}
def fetch_credential(lic_id):
    try:
        rc = requests.get(f"{BASE_URL}/inventory/licenses/{lic_id}/credential", headers=headers, timeout=10)
        if rc.status_code == 200:
            return lic_id, rc.json().get("credential", "")
    except Exception:
        pass
    return lic_id, ""

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(fetch_credential, it["id"]) for it in all_sold]
    for fut in as_completed(futures):
        lid, c_raw = fut.result()
        credentials_cache[lid] = c_raw

unique_client_ids = set(it.get("buyer", {}).get("clientId") for it in all_sold if it.get("buyer", {}).get("clientId"))
client_phone_cache = {}
def fetch_client_phone(cid):
    try:
        ru = requests.get(f"{BASE_URL}/users/{cid}", headers=headers, timeout=10)
        if ru.status_code == 200:
            u = ru.json()
            return cid, u.get("phone") or "", u.get("name") or "", u.get("email") or ""
    except Exception:
        pass
    return cid, "", "", ""

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(fetch_client_phone, cid) for cid in unique_client_ids]
    for fut in as_completed(futures):
        cid, phone, name, email = fut.result()
        client_phone_cache[cid] = {"phone": phone, "name": name, "email": email}

# 4. Formatear registros completos
records = []
for it in all_sold:
    lid = it["id"]
    vid = it.get("variationId")
    var_info = variations_map.get(vid, {
        "product_name": "Servicio Digital",
        "variation_name": "1 mes",
        "full_name": "Servicio Digital"
    })
    service_name = var_info["full_name"]
    
    buyer = it.get("buyer", {})
    client_id = buyer.get("clientId")
    client_name = buyer.get("clientName") or (client_phone_cache.get(client_id, {}).get("name") if client_id else "Cliente")
    order_num = buyer.get("orderNumber") or "ORD-N/A"
    
    phone = client_phone_cache.get(client_id, {}).get("phone") if client_id else ""
    if not phone:
        phone = "+573000000000"
    
    raw_cred = credentials_cache.get(lid, "")
    c_email, c_pass, c_prof, c_pin = parse_credential_text(raw_cred)
    if not c_email and it.get("accountEmail"):
        c_email = it["accountEmail"]
    
    exp_iso = it.get("expiresAt")
    exp_dt = datetime.fromisoformat(exp_iso.replace("Z", "+00:00")).astimezone(TZ_COLOMBIA)
    exp_date = exp_dt.date()
    fecha_corte_str = exp_date.strftime("%d/%m/%Y")
    
    diff_days = (exp_date - TODAY).days
    if diff_days < 0:
        dias_texto = f"⛔ Vencido ({abs(diff_days)} d)"
        estado_alerta = "VENCIDO"
        msg_tiempo = f"🚨 Tu suscripción *venció el {fecha_corte_str}*"
    elif diff_days == 0:
        dias_texto = "🚨 Vence Hoy"
        estado_alerta = "HOY"
        msg_tiempo = "🚨 Tu servicio *vence hoy*"
    elif diff_days == 1:
        dias_texto = "⚠️ 1 día (Mañana)"
        estado_alerta = "1_DIA"
        msg_tiempo = f"⚠️ Te queda *1 día* de servicio (Vence mañana {fecha_corte_str})"
    else:
        dias_texto = f"⏳ {diff_days} días"
        estado_alerta = f"{diff_days}_DIAS"
        msg_tiempo = f"⏳ Le quedan *{diff_days} días* a tu suscripción (Corte: {fecha_corte_str})"
    
    email_val = c_email if c_email else (it.get("accountEmail") or "N/A")
    pass_val = c_pass if c_pass else "N/A"
    prof_val = c_prof if (c_prof and c_prof != "N/A") else "Principal / Completa"
    pin_val = c_pin if (c_pin and c_pin != "N/A") else "N/A"
    
    plantilla_wa = (
        f"👋 ¡Hola {client_name}! Esperamos que estés disfrutando de tu servicio.\n\n"
        f"⚡ Te informamos desde *Stream Zone* sobre el estado de tu cuenta:\n"
        f"{msg_tiempo}.\n\n"
        f"✨ *Detalles de tu servicio*:\n"
        f"📌 *Servicio / Plan*: {service_name}\n"
        f"🧾 *Nº de Orden*: {order_num}\n"
        f"📧 *Correo / Cuenta*: {email_val}\n"
        f"🔑 *Contraseña*: {pass_val}\n"
        f"👤 *Perfil*: {prof_val}\n"
        f"🔒 *PIN*: {pin_val}\n"
        f"⏳ *Días restantes*: {dias_texto}\n"
        f"📅 *Fecha de Vencimiento*: {fecha_corte_str}\n\n"
        f"💡 Si deseas renovar tu acceso sin interrupciones o tienes alguna duda, responde a este mensaje y con gusto te asistimos. ¡Muchas gracias por tu preferencia! 🙌"
    )
    
    records.append({
        "order_num": order_num,
        "client_name": client_name,
        "phone": phone,
        "service_name": service_name,
        "fecha_corte": fecha_corte_str,
        "exp_date": exp_date,
        "diff_days": diff_days,
        "dias_texto": dias_texto,
        "estado_alerta": estado_alerta,
        "cuenta_email": c_email,
        "clave": c_pass,
        "perfil": c_prof,
        "pin": c_pin,
        "estado_cobro": "Por Renovar",
        "plantilla_wa": plantilla_wa,
        "variation_id": vid,
        "license_id": lid
    })

records.sort(key=lambda r: (r["diff_days"], r["order_num"]))

# 5. Compilar Libro Excel Corporativo Oficial (13 columnas)
print("📊 [4/5] Compilando reporte oficial en Excel con plantilla azul Stream Zone...")
wb = openpyxl.Workbook()
wb.remove(wb.active)

FONT_TITLE = Font(name="Calibri", size=15, bold=True, color="FFFFFF")
FONT_SUB = Font(name="Calibri", size=10, italic=True, color="B0BEC5")
FONT_HEADER = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
FONT_DATA = Font(name="Calibri", size=9.5, color="1E293B")
FONT_CLIENT = Font(name="Calibri", size=9.5, bold=True, color="0F172A")
FONT_PROFILE = Font(name="Calibri", size=10, bold=True, color="1D4ED8")
FONT_TOTAL = Font(name="Calibri", size=10, bold=True, color="FFFFFF")

FILL_TITLE = PatternFill(start_color="0D233A", end_color="0D233A", fill_type="solid")
FILL_SUB = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
FILL_HEADER = PatternFill(start_color="1E40AF", end_color="1E40AF", fill_type="solid")
FILL_ROW_WHITE = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
FILL_ROW_ZEBRA = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

FILL_BADGE_RED = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
FONT_BADGE_RED = Font(name="Calibri", size=9.5, bold=True, color="991B1B")
FILL_BADGE_YELLOW = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
FONT_BADGE_YELLOW = Font(name="Calibri", size=9.5, bold=True, color="B45309")
FILL_BADGE_GREEN = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
FONT_BADGE_GREEN = Font(name="Calibri", size=9.5, bold=True, color="15803D")

ALIGN_CENTER = Alignment(horizontal="center", vertical="center")
ALIGN_LEFT = Alignment(horizontal="left", vertical="center", indent=1)

BORDER_THIN = Border(
    left=Side(style="thin", color="E2E8F0"),
    right=Side(style="thin", color="E2E8F0"),
    top=Side(style="thin", color="E2E8F0"),
    bottom=Side(style="thin", color="E2E8F0")
)
BORDER_HEADER = Border(
    left=Side(style="thin", color="2563EB"),
    right=Side(style="thin", color="2563EB"),
    top=Side(style="medium", color="0D233A"),
    bottom=Side(style="medium", color="0D233A")
)

HEADERS = [
    ("#", 5, ALIGN_CENTER),
    ("Nº ORDEN", 13, ALIGN_CENTER),
    ("CLIENTE", 26, ALIGN_LEFT),
    ("TELÉFONO WHATSAPP", 19, ALIGN_CENTER),
    ("SERVICIO / PLAN", 32, ALIGN_LEFT),
    ("FECHA CORTE", 13, ALIGN_CENTER),
    ("DÍAS RESTANTES", 18, ALIGN_CENTER),
    ("CUENTA / USUARIO", 30, ALIGN_LEFT),
    ("CONTRASEÑA", 18, ALIGN_LEFT),
    ("PERFIL", 9, ALIGN_CENTER),
    ("PIN", 9, ALIGN_CENTER),
    ("ESTADO COBRO", 15, ALIGN_CENTER),
    ("PLANTILLA NOTIFICACIÓN WHATSAPP", 55, ALIGN_LEFT)
]

def build_sheet(ws, title_text, sheet_records):
    ws.merge_cells("A1:M1")
    t_cell = ws["A1"]
    t_cell.value = title_text
    t_cell.font = FONT_TITLE
    t_cell.alignment = ALIGN_CENTER
    t_cell.fill = FILL_TITLE
    ws.row_dimensions[1].height = 36
    
    ws.merge_cells("A2:M2")
    s_cell = ws["A2"]
    s_cell.value = f"Reporte oficial de clientes con vencimiento próximo (0-4 días) • Generado: {TODAY.strftime('%d/%m/%Y')} {NOW_LOCAL.strftime('%H:%M')}"
    s_cell.font = FONT_SUB
    s_cell.alignment = ALIGN_CENTER
    s_cell.fill = FILL_SUB
    ws.row_dimensions[2].height = 20
    ws.row_dimensions[3].height = 8
    
    ws.row_dimensions[4].height = 26
    for col_idx, (h_title, col_width, _) in enumerate(HEADERS, 1):
        cell = ws.cell(row=4, column=col_idx, value=h_title)
        cell.font = FONT_HEADER
        cell.alignment = ALIGN_CENTER
        cell.fill = FILL_HEADER
        cell.border = BORDER_HEADER
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width
    
    for r_idx, rec in enumerate(sheet_records, 5):
        ws.row_dimensions[r_idx].height = 22
        fill_row = FILL_ROW_ZEBRA if (r_idx % 2 == 0) else FILL_ROW_WHITE
        
        row_vals = [
            r_idx - 4,
            rec["order_num"],
            rec["client_name"],
            rec["phone"],
            rec["service_name"],
            rec["fecha_corte"],
            rec["dias_texto"],
            rec["cuenta_email"],
            rec["clave"],
            rec["perfil"],
            rec["pin"],
            rec["estado_cobro"],
            rec["plantilla_wa"].replace("\n", "  ")
        ]
        
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = FONT_DATA
            cell.fill = fill_row
            cell.border = BORDER_THIN
            cell.alignment = HEADERS[c_idx - 1][2]
            
            if c_idx == 3:
                cell.font = FONT_CLIENT
            elif c_idx == 7:
                if rec["diff_days"] <= 0:
                    cell.fill = FILL_BADGE_RED
                    cell.font = FONT_BADGE_RED
                elif rec["diff_days"] == 1:
                    cell.fill = FILL_BADGE_YELLOW
                    cell.font = FONT_BADGE_YELLOW
                else:
                    cell.fill = FILL_BADGE_GREEN
                    cell.font = FONT_BADGE_GREEN
            elif c_idx == 10:
                cell.font = FONT_PROFILE
            elif c_idx == 12:
                cell.fill = FILL_BADGE_YELLOW
                cell.font = FONT_BADGE_YELLOW
    
    tot_row = len(sheet_records) + 6
    ws.row_dimensions[tot_row].height = 24
    ws.merge_cells(f"A{tot_row}:E{tot_row}")
    t_tot = ws.cell(row=tot_row, column=1, value=f"TOTAL DE CUENTAS / ACCESOS EN CORTE: {len(sheet_records)}")
    t_tot.font = FONT_TOTAL
    t_tot.fill = FILL_TITLE
    t_tot.alignment = ALIGN_CENTER
    
    uniq_clients = len(set(r["phone"] for r in sheet_records))
    ws.merge_cells(f"F{tot_row}:M{tot_row}")
    s_tot = ws.cell(row=tot_row, column=6, value=f"Clientes únicos: {uniq_clients} | Rango: {start_str} al {end_str}")
    s_tot.font = FONT_TOTAL
    s_tot.fill = FILL_HEADER
    s_tot.alignment = ALIGN_CENTER

ws_all = wb.create_sheet(title="Vencimientos (0-4 Días)")
build_sheet(ws_all, f"🎬 STREAM ZONE — DESGLOSE OFICIAL DE VENCIMIENTOS ({start_str} AL {end_str})", records)

hbo_records = [r for r in records if r["variation_id"] == TARGET_VARIATION_ID]
ws_hbo = wb.create_sheet(title="HBO Max Estándar (Variación)")
build_sheet(ws_hbo, f"🎬 STREAM ZONE — HBO MAX ESTÁNDAR PANTALLA ({start_str} AL {end_str})", hbo_records)

date_slug = TODAY.strftime("%Y_%m_%d")
out_dir_downloads = "/home/rootkit/Descargas"
out_dir_sz = f"/home/rootkit/StreamZone/proyectos/corte_{date_slug}"
os.makedirs(out_dir_downloads, exist_ok=True)
os.makedirs(out_dir_sz, exist_ok=True)

excel_path_dl = os.path.join(out_dir_downloads, f"reporte_vencimientos_4_dias_{date_slug}.xlsx")
excel_path_sz = os.path.join(out_dir_sz, "reporte_vencimientos_4_dias.xlsx")

wb.save(excel_path_dl)
wb.save(excel_path_sz)

# 6. Preparar lotes de WhatsApp (individual y consolidado con todos los campos)
print("📱 [5/5] Preparando lotes de notificación WhatsApp (individuales y consolidados)...")
tasks_list = []
for r in records:
    tasks_list.append({
        "order": r["order_num"],
        "name": r["client_name"],
        "phone": r["phone"].replace("+", "").strip(),
        "service": r["service_name"],
        "expiry": r["fecha_corte"],
        "days": r["diff_days"],
        "accountEmail": r["cuenta_email"],
        "password": r["clave"],
        "profile": r["perfil"],
        "pin": r["pin"],
        "message": r["plantilla_wa"]
    })

from collections import defaultdict
grouped = defaultdict(list)
for r in records:
    grouped[r["phone"].replace("+", "").strip()].append(r)

consolidated_list = []
for phone, items in grouped.items():
    name = items[0]["client_name"]
    items.sort(key=lambda x: x["diff_days"])
    
    if len(items) == 1:
        it = items[0]
        msg = it["plantilla_wa"]
    else:
        acc_blocks = []
        for it in items:
            c_email = it['cuenta_email'] if it['cuenta_email'] else "N/A"
            c_pass = it['clave'] if it['clave'] else "N/A"
            c_prof = it['perfil'] if (it['perfil'] and it['perfil'] != 'N/A') else "Principal / Completa"
            c_pin = it['pin'] if (it['pin'] and it['pin'] != 'N/A') else "N/A"
            
            acc_blocks.append(
                f"📌 *{it['service_name']}*\n"
                f"   • 🧾 *Orden*: {it['order_num']} | ⏳ *Días*: {it['dias_texto']} | 📅 *Corte*: {it['fecha_corte']}\n"
                f"   • 📧 *Correo*: {c_email}\n"
                f"   • 🔑 *Contraseña*: {c_pass}\n"
                f"   • 👤 *Perfil*: {c_prof} | 🔒 *PIN*: {c_pin}"
            )
        accounts_text = "\n\n".join(acc_blocks)
        msg = (
            f"👋 ¡Hola {name}! Esperamos que estés disfrutando de tus servicios.\n\n"
            f"⚡ Te informamos desde *Stream Zone* sobre el estado de tus cuentas con corte próximo:\n\n"
            f"{accounts_text}\n\n"
            f"💡 Si deseas renovar tus accesos sin interrupciones o tienes alguna duda con alguna cuenta, responde a este mensaje y con gusto te asistimos. ¡Muchas gracias por tu preferencia! 🙌"
        )
    
    consolidated_list.append({
        "order": items[0]["order_num"],
        "name": name,
        "phone": phone,
        "count": len(items),
        "message": msg
    })

tasks_path_tmp = "/tmp/pending_notifications.json"
tasks_path_sz = os.path.join(out_dir_sz, "pending_notifications.json")
with open(tasks_path_tmp, "w", encoding="utf-8") as f:
    json.dump(tasks_list, f, ensure_ascii=False, indent=2)
with open(tasks_path_sz, "w", encoding="utf-8") as f:
    json.dump(tasks_list, f, ensure_ascii=False, indent=2)

cons_path_tmp = "/tmp/consolidated_notifications.json"
cons_path_sz = os.path.join(out_dir_sz, "consolidated_notifications.json")
with open(cons_path_tmp, "w", encoding="utf-8") as f:
    json.dump(consolidated_list, f, ensure_ascii=False, indent=2)
with open(cons_path_sz, "w", encoding="utf-8") as f:
    json.dump(consolidated_list, f, ensure_ascii=False, indent=2)

# Archivo de metadatos de ejecución para wrappers bash
metadata = {
    "excel_path": excel_path_dl,
    "excel_sz_path": excel_path_sz,
    "total_records": len(records),
    "unique_clients": len(consolidated_list),
    "hbo_records": len(hbo_records),
    "start_str": START_DATE.strftime("%d/%m/%Y"),
    "end_str": END_DATE.strftime("%d/%m/%Y"),
    "tasks_path": tasks_path_tmp,
    "consolidated_path": cons_path_tmp,
    "generated_at": NOW_LOCAL.isoformat()
}
with open("/tmp/sz_last_report.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print("\n" + "="*70)
print(f"🎬 PIPELINE DE VENCIMIENTOS COMPLETADO (STREAM ZONE)")
print("="*70)
print(f"• Total suscripciones en corte: {len(records)}")
print(f"• Clientes únicos a notificar: {len(consolidated_list)}")
print(f"• Reporte Excel: {excel_path_dl}")
print(f"• Tareas preparadas con correo, clave, orden, perfil y pin.")
print("="*70)
