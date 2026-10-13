import wave
import math
import struct
import os

SAMPLE_RATE = 44100
DURATION = 15.0  # seconds
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

# Buffer estéreo (izq, der)
left_channel = [0.0] * TOTAL_SAMPLES
right_channel = [0.0] * TOTAL_SAMPLES

def clamp(val, low=-1.0, high=1.0):
    return max(low, min(high, val))

# 1. GENERAR BEAT ELECTRÓNICO MINIMALISTA (120 BPM -> 1 beat = 0.5s)
bpm = 120
beat_len = 60.0 / bpm  # 0.5s
num_beats = int(DURATION / beat_len)

for b in range(num_beats):
    t_beat = b * beat_len
    idx_start = int(t_beat * SAMPLE_RATE)
    
    # KICK (Sub-kick minimalista elegante, estilo Apple / Teenage Engineering)
    # Frecuencia cae de 140Hz a 45Hz rápidamente
    kick_samples = int(0.18 * SAMPLE_RATE)
    for i in range(kick_samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 22)  # Decay rápido
        freq = 45 + 95 * math.exp(-t * 35)
        val = 0.35 * math.sin(2 * math.pi * freq * t) * env
        left_channel[idx] += val
        right_channel[idx] += val

    # HI-HAT / CLICK MECÁNICO EN OFF-BEAT (cada 0.25s)
    idx_hat = idx_start + int(0.25 * SAMPLE_RATE)
    hat_samples = int(0.04 * SAMPLE_RATE)
    for i in range(hat_samples):
        idx = idx_hat + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 90)
        # Ruido filtrado / tono metálico sutil
        val = 0.12 * (math.sin(2 * math.pi * 3200 * t) + math.sin(2 * math.pi * 5400 * t)) * env
        left_channel[idx] += val * 0.9
        right_channel[idx] += val * 1.1

# 2. SFX SINCRONIZADOS DE DISEÑO DE MOVIMIENTO

def add_click(t_start, freq=2400, amp=0.55):
    """Click háptico de UI extremadamente nítido"""
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(0.03 * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 120)
        val = amp * math.sin(2 * math.pi * freq * t) * env
        left_channel[idx] += val
        right_channel[idx] += val

def add_whoosh(t_start, dur, f_start, f_end, amp=0.35):
    """Barrido de aire cinético / whoosh suave"""
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(dur * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        norm = t / dur
        # Envelope en campana
        env = math.sin(math.pi * norm)
        freq = f_start + (f_end - f_start) * norm
        val = amp * math.sin(2 * math.pi * freq * t) * env
        left_channel[idx] += val * (1.0 - norm * 0.4)
        right_channel[idx] += val * (0.6 + norm * 0.4)

def add_spring_bounce(t_start, dur=1.8, f_base=280, amp=0.45):
    """Sonido acústico de resorte con oscilación armónica amortiguada"""
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(dur * SAMPLE_RATE)
    zeta = 0.42
    omega = 16.0
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        # Desplazamiento del resorte
        decay = math.exp(-zeta * omega * t)
        osc = math.sin(omega * t)
        freq = f_base * (1.0 + 0.5 * osc * decay)
        val = amp * decay * math.sin(2 * math.pi * freq * t)
        left_channel[idx] += val * 0.8
        right_channel[idx] += val * 1.0

def add_chime(t_start, freq=1200, amp=0.4):
    """Campana / ping cristalino de asentamiento"""
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(0.5 * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 8)
        val = amp * math.sin(2 * math.pi * freq * t) * env
        # Armónico suave
        val += (amp * 0.4) * math.sin(2 * math.pi * (freq * 2.05) * t) * math.exp(-t * 14)
        left_channel[idx] += val * 1.0
        right_channel[idx] += val * 0.85

def add_bass_drop(t_start, amp=0.5):
    """Sub-bass profundo cinemático para la tarjeta final"""
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(1.2 * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 3.5)
        freq = 65 * math.exp(-t * 1.5)
        val = amp * math.sin(2 * math.pi * freq * t) * env
        left_channel[idx] += val
        right_channel[idx] += val

# --- DISPARAR EVENTOS SINCRONIZADOS ---
# 1. Apertura: Click del cursor en el toggle naranja a t = 0.8s
add_click(0.8, freq=2800, amp=0.6)

# 2. Letras doblándose y colapsando a t = 1.3s - 1.8s
add_whoosh(1.2, dur=0.6, f_start=600, f_end=180, amp=0.25)
add_click(1.9, freq=1600, amp=0.35)  # El punto naranja aterriza en la 'i'

# 3. El punto salta de la 'i' y aterriza en el gráfico a t = 2.4s
add_whoosh(2.3, dur=0.4, f_start=300, f_end=750, amp=0.3)
add_spring_bounce(2.7, dur=1.8, f_base=220, amp=0.4)

# 4. Asentamiento en el pico de +22% a t = 4.2s
add_chime(4.2, freq=1480, amp=0.35)

# 5. El punto corre por la línea y se expande en círculo naranja a t = 5.0s
add_whoosh(5.0, dur=0.7, f_start=150, f_end=600, amp=0.35)

# 6. Rotación del cuadrado y estiramiento en píldora a t = 6.2s
add_click(6.2, freq=900, amp=0.3)
add_whoosh(6.3, dur=0.5, f_start=400, f_end=200, amp=0.25)

# 7. Contracción elástica en un solo punto a t = 7.4s
add_whoosh(7.3, dur=0.3, f_start=500, f_end=150, amp=0.35)
add_click(7.6, freq=3200, amp=0.5)

# 8. Anillo de palabras dispersándose en semitono a t = 8.8s
add_whoosh(8.6, dur=0.6, f_start=300, f_end=1100, amp=0.3)
# Ráfaga de micro-ticks
for offset in [0.0, 0.04, 0.08, 0.12, 0.16]:
    add_click(9.0 + offset, freq=3500 + offset*2000, amp=0.15)

# 9. Descubrimiento de la tarjeta final a t = 10.6s
add_bass_drop(10.6, amp=0.55)
add_chime(10.8, freq=1050, amp=0.4)

# 10. Retorno del punto hacia el inicio a t = 13.5s
add_whoosh(13.5, dur=0.8, f_start=180, f_end=550, amp=0.3)
# 11. Cierre del bucle (clic de retorno) a t = 14.8s
add_click(14.8, freq=2800, amp=0.4)

# Guardar a archivo WAV 16-bit PCM estéreo
out_dir = "/home/rootkit/Proyectos/bichirol-video/public"
os.makedirs(out_dir, exist_ok=True)
wav_path = os.path.join(out_dir, "motion_soundtrack.wav")

with wave.open(wav_path, "w") as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(SAMPLE_RATE)
    
    frames_data = bytearray()
    for i in range(TOTAL_SAMPLES):
        l = int(clamp(left_channel[i]) * 32767)
        r = int(clamp(right_channel[i]) * 32767)
        frames_data.extend(struct.pack("<hh", l, r))
    
    wav_file.writeframes(frames_data)

print(f"WAV generado con éxito en: {wav_path} ({len(frames_data)} bytes)")
