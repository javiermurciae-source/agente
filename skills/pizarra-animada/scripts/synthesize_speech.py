#!/usr/bin/env python3
"""
Sintetizador de voz offline con Kokoro TTS para clases y lecciones de pizarra animada.
Uso:
    python synthesize_speech.py --text "Hola mundo" --voice em_alex --output salida.wav
"""

import argparse
import json
import os
import sys
import kokoro_onnx
import soundfile as sf

MODEL_PATH = "/home/rootkit/.cache/hyperframes/tts/models/kokoro-v1.0.onnx"
VOICES_PATH = "/home/rootkit/.cache/hyperframes/tts/voices/voices-v1.0.bin"

def main():
    parser = argparse.ArgumentParser(description="Kokoro TTS Generator")
    parser.add_argument("--text", required=True, help="Texto a sintetizar")
    parser.add_argument("--voice", default="em_alex", help="Voz (em_alex, ef_dora, em_santa)")
    parser.add_argument("--speed", type=float, default=1.05, help="Velocidad de habla")
    parser.add_argument("--lang", default="es", help="Idioma")
    parser.add_argument("--output", required=True, help="Ruta del archivo WAV de salida")
    args = parser.parse_args()

    if not os.path.exists(MODEL_PATH) or not os.path.exists(VOICES_PATH):
        print(f"Error: Modelos de Kokoro no encontrados en {MODEL_PATH}", file=sys.stderr)
        sys.exit(1)

    tts = kokoro_onnx.Kokoro(MODEL_PATH, VOICES_PATH)
    samples, rate = tts.create(args.text, voice=args.voice, speed=args.speed, lang=args.lang)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    sf.write(args.output, samples, rate)

    duration = len(samples) / rate
    result = {
        "output": args.output,
        "sample_rate": rate,
        "duration_seconds": round(duration, 3),
        "voice": args.voice
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
