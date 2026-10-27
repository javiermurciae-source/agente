#!/usr/bin/env python3
import asyncio
import sys
import os
from androidtvremote2 import AndroidTVRemote

CERT_FILE = os.path.expanduser("~/.config/androidtv_cert.pem")
KEY_FILE = os.path.expanduser("~/.config/androidtv_key.pem")

async def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  tv_remote.py pair <IP>          -> Iniciar emparejamiento (muestra PIN en TV)")
        print("  tv_remote.py confirm <PIN>      -> Confirmar con el PIN")
        print("  tv_remote.py send <COMANDO>     -> Enviar tecla (DPAD_UP, DPAD_DOWN, HOME, BACK, ENTER, VOLUME_UP, etc.)")
        return

    cmd = sys.argv[1]

    if cmd == "pair":
        ip = sys.argv[2] if len(sys.argv) > 2 else "192.168.40.2"
        with open("/tmp/tv_ip.txt", "w") as f:
            f.write(ip)
        remote = AndroidTVRemote(
            client_name="Camilo PC Agent",
            certfile=CERT_FILE,
            keyfile=KEY_FILE,
            host=ip
        )
        print(f"[*] Solicitando emparejamiento con Android TV en {ip}...")
        await remote.async_start_pairing()
        print("[!] Revisa la pantalla de tu TV: debe aparecer un código PIN de 6 caracteres.")
        print("[!] Ejecuta: python3 scripts/tv_remote.py confirm <CODIGO_PIN>")

    elif cmd == "confirm":
        if len(sys.argv) < 3:
            print("Error: Falta el PIN. Uso: tv_remote.py confirm <PIN>")
            return
        pin = sys.argv[2].strip()
        with open("/tmp/tv_ip.txt") as f:
            ip = f.read().strip()
        remote = AndroidTVRemote(
            client_name="Camilo PC Agent",
            certfile=CERT_FILE,
            keyfile=KEY_FILE,
            host=ip
        )
        res = await remote.async_finish_pairing(pin)
        if res:
            print("[+] ¡Emparejamiento exitoso! Certificado guardado.")
        else:
            print("[-] Falló el emparejamiento. Verifica el PIN.")

    elif cmd == "send":
        key = sys.argv[2].upper() if len(sys.argv) > 2 else "HOME"
        with open("/tmp/tv_ip.txt") as f:
            ip = f.read().strip()
        remote = AndroidTVRemote(
            client_name="Camilo PC Agent",
            certfile=CERT_FILE,
            keyfile=KEY_FILE,
            host=ip
        )
        await remote.async_connect()
        await remote.async_send_key_command(key)
        print(f"[+] Comando '{key}' enviado al TV.")
        await remote.async_disconnect()

if __name__ == "__main__":
    asyncio.run(main())
