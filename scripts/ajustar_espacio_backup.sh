#!/usr/bin/env bash
# ==============================================================================
# Script para ejecutar desde el Live USB de CachyOS
# Ajusta la partición de Backup a ~180 GB exactos y deja ~296 GB para el Sistema
# ==============================================================================

set -euo pipefail

if [ "$EUID" -ne 0 ]; then
  echo "❌ Ejecuta este script con sudo: sudo bash $0"
  exit 1
fi

DISK="/dev/nvme0n1"
PART_BACKUP="${DISK}p2"
MOUNT_DIR="/mnt/temp_btrfs"

echo "========================================================"
echo "  🚀 Ajustando partición de Backup a tamaño exacto (~180 GB)"
echo "  y liberando ~296 GB para tu nuevo CachyOS..."
echo "========================================================"

mkdir -p "$MOUNT_DIR"
mount -o subvolid=5 "$PART_BACKUP" "$MOUNT_DIR"

echo "🗑️ Eliminando subvolúmenes viejos del sistema anterior..."
btrfs subvolume delete "$MOUNT_DIR/@cache" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@log" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@tmp" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@srv" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@root" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@/var/lib/portables" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@/var/lib/machines" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@" 2>/dev/null || true
btrfs subvolume delete "$MOUNT_DIR/@home" 2>/dev/null || true

echo "📏 Redimensionando filesystem Btrfs de backup a 180 GiB..."
btrfs filesystem resize 180G "$MOUNT_DIR"
umount "$MOUNT_DIR"

echo "✂️ Ajustando particiones físicas en el disco..."
# Eliminar partición 3 vieja si existe
parted -s "$DISK" rm 3 2>/dev/null || true

# Redimensionar partición 2 a 180 GiB
parted -s "$DISK" resizepart 2 181GiB

udevadm settle
partprobe "$DISK" || true

echo "✨ Creando partición para el SISTEMA REAL con los ~296 GB restantes..."
parted -s "$DISK" mkpart "cachyos_system" btrfs 181GiB 100%

udevadm settle
partprobe "$DISK" || true
sleep 1

mkfs.btrfs -f -L "cachyos_root" "${DISK}p3"

echo "========================================================"
echo "  ✅ ¡LISTO! Distribución final del disco:"
lsblk -o NAME,SIZE,FSTYPE,LABEL "$DISK"
echo "========================================================"
echo "  👉 ${DISK}p2 (180 GB): Tu backup exclusivo (Juegos, Proyectos, Agente)."
echo "  👉 ${DISK}p3 (~296 GB): Tu nuevo sistema real CachyOS con espacio de sobra."
echo "========================================================"
