#!/usr/bin/env bash
# ==============================================================================
# Script de Preparación de Partición CachyOS (Plan A)
# Elimina particiones de Windows (p3 y p4) y crea nueva partición Btrfs limpia
# ==============================================================================

set -euo pipefail

if [ "$EUID" -ne 0 ]; then
  echo "❌ Este script debe ejecutarse con privilegios de root (sudo)."
  exit 1
fi

DISK="/dev/nvme0n1"

echo "========================================================"
echo "  🛠️  Eliminando particiones de Windows en $DISK..."
echo "========================================================"

# Verificar que el disco existe
if [ ! -b "$DISK" ]; then
  echo "❌ Error: Disco $DISK no encontrado."
  exit 1
fi

# Desmontar p3 y p4 si estuvieran montadas por alguna razón
umount "${DISK}p3" 2>/dev/null || true
umount "${DISK}p4" 2>/dev/null || true

# Eliminar partición 3 y 4 usando parted / sfdisk de forma segura y quirúrgica
echo "🗑️ Eliminando partición 3 (Microsoft reserved) y partición 4 (Windows NTFS)..."
parted -s "$DISK" rm 4
parted -s "$DISK" rm 3

# Esperar a que el kernel actualice la tabla de particiones
udevadm settle
partprobe "$DISK" || true

echo "✨ Creando nueva partición Btrfs en el espacio liberado..."
# Crear nueva partición primaria desde el fin de p2 hasta el 100% del disco
parted -s "$DISK" mkpart "cachyos_system" btrfs 327GiB 100%

udevadm settle
partprobe "$DISK" || true
sleep 1

# Determinar el nombre de la nueva partición (debe ser nvme0n1p3)
NEW_PART="${DISK}p3"

if [ ! -b "$NEW_PART" ]; then
  echo "⚠️ Verificando nombre de la nueva partición..."
  NEW_PART=$(lsblk -ln -o NAME "$DISK" | tail -n 1)
  NEW_PART="/dev/$NEW_PART"
fi

echo "📦 Formateando $NEW_PART en Btrfs (Label: cachyos_new)..."
mkfs.btrfs -f -L "cachyos_new" "$NEW_PART"

echo "========================================================"
echo "  ✅ ¡Listo! Partición preparada con éxito:"
lsblk -o NAME,SIZE,FSTYPE,LABEL,MOUNTPOINTS "$DISK"
echo "========================================================"
echo "  👉 Cuando inicies el instalador de CachyOS:"
echo "     1. Selecciona 'Particionado manual'."
echo "     2. Elige $NEW_PART (150 GB) como partición raíz (/) para formatear."
echo "     3. Deja ${DISK}p2 (326 GB) INTACTA (sin formatear) para tus juegos."
echo "========================================================"
