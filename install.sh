#!/usr/bin/env bash
# ==============================================================================
# Script de Instalación y Recuperación Instantánea del Agente
# Entorno: CachyOS Linux (x86_64), Wayland (Niri), Fish/Kitty
# ==============================================================================

set -euo pipefail

AGENTE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_BIN="$HOME/.local/bin"

echo "========================================================"
echo "  🚀 Restaurando Agente Autónomo en: $AGENTE_DIR"
echo "========================================================"

mkdir -p "$LOCAL_BIN"
mkdir -p "$HOME/.cache"

# 1. Permisos de ejecución
echo "⚙️ Configurando permisos de ejecución..."
chmod +x "$AGENTE_DIR"/bin/* 2>/dev/null || true
find "$AGENTE_DIR/scripts" -type f \( -name "*.sh" -o -name "*.py" -o -name "*.js" \) -exec chmod +x {} + 2>/dev/null || true
chmod +x "$AGENTE_DIR/install.sh"

# 2. Enlaces simbólicos de binarios a ~/.local/bin
echo "🔗 Enlazando binarios del agente en $LOCAL_BIN..."
for bin_file in "$AGENTE_DIR/bin/"*; do
    if [ -f "$bin_file" ]; then
        bin_name="$(basename "$bin_file")"
        ln -sf "$bin_file" "$LOCAL_BIN/$bin_name"
    fi
done

# 3. Enlaces simbólicos para agentes de IA (~/.agents/skills)
echo "🧠 Enlazando skills y reglas maestras para el agente de IA..."
mkdir -p "$HOME/.agents"
ln -sfn "$AGENTE_DIR/skills" "$HOME/.agents/skills"

if [ "$AGENTE_DIR" != "$HOME" ]; then
    ln -sf "$AGENTE_DIR/AGENTS.md" "$HOME/AGENTS.md"
    ln -sf "$AGENTE_DIR/GEMINI.md" "$HOME/GEMINI.md"
fi

# 4. Instalación de RTK (Rust Token Killer) para optimización de tokens
if ! command -v rtk >/dev/null 2>&1; then
    echo "⚡ Instalando RTK (Rust Token Killer) para compresión de tokens..."
    curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh 2>/dev/null || true
else
    echo "   ✅ RTK ya instalado y disponible en PATH."
fi

# 5. Instalación de dependencias de WhatsApp (tools/wasend)

if [ -d "$AGENTE_DIR/tools/wasend" ]; then
    echo "📦 Verificando dependencias de tools/wasend..."
    if [ ! -d "$AGENTE_DIR/tools/wasend/node_modules" ]; then
        echo "   Instalando dependencias de Baileys..."
        if command -v bun >/dev/null 2>&1; then
            (cd "$AGENTE_DIR/tools/wasend" && bun install)
        elif command -v npm >/dev/null 2>&1; then
            (cd "$AGENTE_DIR/tools/wasend" && npm install)
        else
            echo "   ⚠️ Advertencia: Ni bun ni npm están disponibles. Instálalos para habilitar wasend."
        fi
    else
        echo "   ✅ node_modules ya presente en tools/wasend."
    fi
fi

echo "========================================================"
echo "  ✅ Agente completamente restaurado y operativo."
echo "  Recuerda asegurar que $LOCAL_BIN esté en tu \$PATH."
echo "========================================================"
