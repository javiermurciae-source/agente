import asyncio
import os
import sys
from androidtvremote2 import AndroidTVRemote

CERT_FILE = os.path.expanduser("~/.config/androidtv_cert.pem")
KEY_FILE = os.path.expanduser("~/.config/androidtv_key.pem")

async def main():
    remote = AndroidTVRemote("Camilo TV Remote", CERT_FILE, KEY_FILE, "192.168.40.2")
    print("[*] Conectando con Android TV (192.168.40.2)...")
    await remote.async_start_pairing()
    print("[!] Solicitud enviada. El socket está ABIERTO esperando el PIN.")
    print("Por favor introduce el PIN de 6 caracteres que aparece en pantalla: ", end="", flush=True)
    pin = sys.stdin.readline().strip()
    if not pin:
        print("PIN vacío, cancelando.")
        return
    success = await remote.async_finish_pairing(pin)
    if success:
        print("[+] ¡EMPAREJAMIENTO COMPLETADO CON ÉXITO!")
        print("[*] Probando botón HOME...")
        await remote.async_connect()
        await remote.async_send_key_command("HOME")
        print("[+] ¡Botón HOME enviado con éxito!")
        await remote.async_disconnect()
    else:
        print("[-] Error: El PIN no fue aceptado por el televisor.")

if __name__ == "__main__":
    asyncio.run(main())
