#!/usr/bin/env python3
import json
import base64
import requests

CACHE_TOKEN_PATH = "/home/rootkit/.cache/sz_admin_token.json"
BASE_URL = "https://api.nuvlyx.com/api/v1"
TENANT_SLUG = "stream-zone-6822"
STREAMING_CAT_ID = "d3f890b0-f962-46a1-9f10-13509e18800a"

def get_headers():
    with open(CACHE_TOKEN_PATH) as f:
        data = json.load(f)
    token = data.get("accessToken")
    return {
        "Authorization": f"Bearer {token}",
        "x-tenant-slug": TENANT_SLUG,
        "Content-Type": "application/json"
    }

def get_dramabox_image_uri():
    icon_path = "/home/rootkit/agente/vault/dramabox-legacy-src/res_out/resources/res/mipmap-xxxhdpi/ic_launcher.png"
    with open(icon_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

def create_product(product_data, variations):
    headers = get_headers()
    # 1. Crear producto base
    r = requests.post(f"{BASE_URL}/products", json=product_data, headers=headers, timeout=15)
    if r.status_code not in (200, 201):
        raise RuntimeError(f"Error creando producto {product_data['name']}: {r.text}")
    
    prod = r.json()
    prod_id = prod["id"]
    print(f"✅ Producto creado: {prod['name']} (ID: {prod_id})")
    
    # 2. Crear variaciones
    for var in variations:
        r_var = requests.post(f"{BASE_URL}/products/{prod_id}/variations", json=var, headers=headers, timeout=15)
        if r_var.status_code not in (200, 201):
            print(f"⚠️ Error creando variación {var['name']}: {r_var.text}")
        else:
            v_data = r_var.json()
            print(f"   ➕ Variación añadida: {v_data['name']} - ${v_data['price']} COP ({v_data.get('durationDays')} días)")
            
    return prod_id

def main():
    print("🚀 Subiendo nuevos productos APK al catálogo de Stream Zone en NuVlyx...\n")
    
    dramabox_img = get_dramabox_image_uri()
    yt_img = "https://pub-de9107cd4c42484e83aaa1aa94ba53f6.r2.dev/tenants/f6468836-aa5b-4c14-a359-1674d5830dc0/products/3a11982c-7e1a-4971-9dcf-875e91855b45.webp"
    
    # 1. DramaBox VIP
    dramabox_payload = {
        "name": "DramaBox VIP - APK Android",
        "shortDescription": "APK VIP desbloqueado sin anuncios ni límites de capítulos",
        "description": "🎬 Disfruta de todos los dramas cortos, series exclusivas y novelas asiáticas sin límites con acceso VIP total y cero publicidad. Formato exclusivo en APK para dispositivos Android.",
        "categoryId": STREAMING_CAT_ID,
        "coverImageUrl": dramabox_img,
        "status": "ACTIVE",
        "isVisible": True
    }
    dramabox_variations = [
        {"name": "1 mes", "price": "5000", "dependsOnStock": True, "isActive": True, "durationDays": 30},
        {"name": "3 meses", "price": "15000", "dependsOnStock": True, "isActive": True, "durationDays": 90},
        {"name": "6 meses", "price": "30000", "dependsOnStock": True, "isActive": True, "durationDays": 180}
    ]
    
    # 2. YouTube Premium
    yt_payload = {
        "name": "YouTube Premium - APK Android",
        "shortDescription": "APK YouTube Music + Segundo Plano + Sin Anuncios",
        "description": "🎵 Toda la experiencia de YouTube Premium en tu celular Android sin suscripciones oficiales de Google. Cero anuncios, reproducción en segundo plano y con pantalla apagada.",
        "categoryId": STREAMING_CAT_ID,
        "coverImageUrl": yt_img,
        "status": "ACTIVE",
        "isVisible": True
    }
    yt_variations = [
        {"name": "1 mes", "price": "5000", "dependsOnStock": True, "isActive": True, "durationDays": 30},
        {"name": "3 meses", "price": "15000", "dependsOnStock": True, "isActive": True, "durationDays": 90},
        {"name": "6 meses", "price": "30000", "dependsOnStock": True, "isActive": True, "durationDays": 180},
        {"name": "1 año", "price": "35000", "dependsOnStock": True, "isActive": True, "durationDays": 365}
    ]
    
    pid_db = create_product(dramabox_payload, dramabox_variations)
    print("")
    pid_yt = create_product(yt_payload, yt_variations)
    print("\n🎉 ¡Ambos productos subidos con éxito al catálogo activo de Stream Zone!")
    return pid_db, pid_yt

if __name__ == "__main__":
    main()
