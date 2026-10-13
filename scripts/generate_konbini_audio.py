import wave
import math
import struct
import random
import os

SAMPLE_RATE = 44100
DURATION = 15.0  # seconds
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

left_channel = [0.0] * TOTAL_SAMPLES
right_channel = [0.0] * TOTAL_SAMPLES

def clamp(val, low=-1.0, high=1.0):
    return max(low, min(high, val))

# -------------------------------------------------------------------------
# 1. AMBIENTE CONTINUO DE LLUVIA (Ruido rosa filtrado + estéreo espacial)
# -------------------------------------------------------------------------
# Algoritmo de Paul Kellet para ruido rosa suave
b0_l, b1_l, b2_l, b3_l, b4_l, b5_l = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
b0_r, b1_r, b2_r, b3_r, b4_r, b5_r = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

random.seed(42) # Determinista

# Filtro IIR simple de paso bajo para lluvia exterior
lp_l = 0.0
lp_r = 0.0
lp_alpha = 0.22 # corte alrededor de 1.5kHz

for i in range(TOTAL_SAMPLES):
    t = i / SAMPLE_RATE
    
    # Canal izquierdo
    white_l = random.uniform(-1.0, 1.0)
    b0_l = 0.99886 * b0_l + white_l * 0.0555179
    b1_l = 0.99332 * b1_l + white_l * 0.0750759
    b2_l = 0.96900 * b2_l + white_l * 0.1538520
    b3_l = 0.86650 * b3_l + white_l * 0.3104856
    b4_l = 0.55000 * b4_l + white_l * 0.5329522
    b5_l = -0.7616 * b5_l - white_l * 0.0168980
    pink_l = (b0_l + b1_l + b2_l + b3_l + b4_l + b5_l + white_l * 0.5362) * 0.05
    lp_l += lp_alpha * (pink_l - lp_l)
    
    # Canal derecho (generador independiente)
    white_r = random.uniform(-1.0, 1.0)
    b0_r = 0.99886 * b0_r + white_r * 0.0555179
    b1_r = 0.99332 * b1_r + white_r * 0.0750759
    b2_r = 0.96900 * b2_r + white_r * 0.1538520
    b3_r = 0.86650 * b3_r + white_r * 0.3104856
    b4_r = 0.55000 * b4_r + white_r * 0.5329522
    b5_r = -0.7616 * b5_r - white_r * 0.0168980
    pink_r = (b0_r + b1_r + b2_r + b3_r + b4_r + b5_r + white_r * 0.5362) * 0.05
    lp_r += lp_alpha * (pink_r - lp_r)
    
    # Onda sutil de viento/distancia
    gust = 1.0 + 0.12 * math.sin(2 * math.pi * 0.18 * t)
    
    left_channel[i] += lp_l * 0.42 * gust
    right_channel[i] += lp_r * 0.42 * gust

# -------------------------------------------------------------------------
# 2. GOTEO Y GOTAS EN CHARCOS / PARAGUAS (Plops y pings cristalinos)
# -------------------------------------------------------------------------
def add_water_drip(t_start, f_start=1800, dur=0.06, amp=0.18, pan=0.0):
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(dur * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        norm = t / dur
        env = math.exp(-norm * 7.5) * (1.0 - math.exp(-norm * 30.0))
        freq = f_start * (1.0 - 0.45 * norm)
        val = amp * math.sin(2 * math.pi * freq * t) * env
        
        l_factor = math.sqrt(0.5 * (1.0 - pan))
        r_factor = math.sqrt(0.5 * (1.0 + pan))
        left_channel[idx] += val * l_factor
        right_channel[idx] += val * r_factor

# 70 gotas dispersas por toda la pista
for _ in range(70):
    t_drip = random.uniform(0.1, 14.8)
    f_drip = random.uniform(1100, 2600)
    amp_drip = random.uniform(0.06, 0.22)
    pan_drip = random.uniform(-0.85, 0.85)
    add_water_drip(t_drip, f_start=f_drip, dur=random.uniform(0.04, 0.08), amp=amp_drip, pan=pan_drip)

# -------------------------------------------------------------------------
# 3. ZUMBIDO CÁLIDO INTERIOR (Nevera de bebidas & Luces fluorescentes)
# -------------------------------------------------------------------------
# El zumbido se hace más presente cuando se abren las puertas (t = 4.0s a 7.5s)
for i in range(TOTAL_SAMPLES):
    t = i / SAMPLE_RATE
    
    # Envolvente de proximidad de puertas abiertas
    if 3.8 <= t <= 7.8:
        door_boost = 1.0 + 1.8 * math.sin(math.pi * ((t - 3.8) / 4.0))
    else:
        door_boost = 1.0
        
    hum_60 = 0.035 * math.sin(2 * math.pi * 60 * t)
    hum_120 = 0.022 * math.sin(2 * math.pi * 120 * t)
    hum_240 = 0.008 * math.sin(2 * math.pi * 240 * t)
    tot_hum = (hum_60 + hum_120 + hum_240) * door_boost
    
    left_channel[i] += tot_hum
    right_channel[i] += tot_hum

# -------------------------------------------------------------------------
# 4. APERTURA Y CIERRE DE PUERTAS AUTOMÁTICAS (Susurro neumático)
# -------------------------------------------------------------------------
def add_door_slide(t_start, dur=0.6, amp=0.18):
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(dur * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        norm = t / dur
        env = math.sin(math.pi * norm)
        # Ruido blanco filtrado en barrido
        white = random.uniform(-1.0, 1.0)
        freq = 600 - 250 * norm
        val = amp * white * math.sin(2 * math.pi * freq * t) * env
        left_channel[idx] += val * 0.9
        right_channel[idx] += val * 1.1

add_door_slide(3.7, dur=0.65, amp=0.16) # Apertura
add_door_slide(7.4, dur=0.65, amp=0.14) # Cierre

# -------------------------------------------------------------------------
# 5. CAMPANILLA ICÓNICA DE TIENDA DE CONVENIENCIA JAPONESA (FamilyMart Chime)
# -------------------------------------------------------------------------
# Melodía de bienvenida cuando se abren las puertas
# Tono: Piano eléctrico FM / campanillas cálidas japonesas
def add_fm_chime_note(t_start, freq, dur=0.28, amp=0.45, pan=0.0):
    idx_start = int(t_start * SAMPLE_RATE)
    samples = int(dur * 1.8 * SAMPLE_RATE) # Decay resonante largo
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        
        # Envolvente: ataque suave percusivo (5ms) y caída exponencial
        attack = min(1.0, t / 0.006)
        decay = math.exp(-t * 4.2)
        env = attack * decay
        
        # Modulación FM sutil para sonido de carillón de tienda
        mod = 0.25 * math.sin(2 * math.pi * (freq * 2.0) * t) * math.exp(-t * 8.0)
        carrier = math.sin(2 * math.pi * freq * t + mod)
        
        # Armónicos cristalinos cálidos
        harm2 = 0.35 * math.sin(2 * math.pi * (freq * 2.0) * t) * math.exp(-t * 6.0)
        harm3 = 0.12 * math.sin(2 * math.pi * (freq * 3.0) * t) * math.exp(-t * 9.0)
        harm4 = 0.05 * math.sin(2 * math.pi * (freq * 4.0) * t) * math.exp(-t * 12.0)
        
        val = amp * (carrier + harm2 + harm3 + harm4) * env
        
        l_factor = math.sqrt(0.5 * (1.0 - pan))
        r_factor = math.sqrt(0.5 * (1.0 + pan))
        left_channel[idx] += val * l_factor
        right_channel[idx] += val * r_factor

# Melodía oficial Konbini en Re Mayor (D major):
# Frase 1: F#5 -> D5 -> A4 -> D5 -> E5 -> A5 (largo)
# Frase 2: E5 -> F#5 -> E5 -> A4 -> D5 (resolución)
konbini_melody = [
    # (tiempo, frecuencia, duración, ganancia, pan)
    (4.15, 739.99, 0.24, 0.42, -0.15), # F#5
    (4.39, 587.33, 0.24, 0.40, -0.10), # D5
    (4.63, 440.00, 0.24, 0.38, -0.05), # A4
    (4.87, 587.33, 0.24, 0.40,  0.00), # D5
    (5.11, 659.25, 0.24, 0.42,  0.05), # E5
    (5.35, 880.00, 0.55, 0.46,  0.10), # A5 (nota larga brillante)
    
    # Pausa corta
    (6.05, 659.25, 0.24, 0.42,  0.08), # E5
    (6.29, 739.99, 0.24, 0.42,  0.04), # F#5
    (6.53, 659.25, 0.24, 0.40,  0.00), # E5
    (6.77, 440.00, 0.24, 0.38, -0.04), # A4
    (7.01, 587.33, 0.70, 0.45, -0.08), # D5 (resolución final dulce)
]

for t_n, f_n, dur_n, amp_n, pan_n in konbini_melody:
    add_fm_chime_note(t_n, f_n, dur=dur_n, amp=amp_n, pan=pan_n)

# -------------------------------------------------------------------------
# 6. MÁQUINA EXPENDEDORA: CLINK METÁLICO A t = 9.8s
# -------------------------------------------------------------------------
def add_vending_clink(t_start):
    idx_start = int(t_start * SAMPLE_RATE)
    # Golpe mecánico de lata cayendo
    samples = int(0.15 * SAMPLE_RATE)
    for i in range(samples):
        idx = idx_start + i
        if idx >= TOTAL_SAMPLES:
            break
        t = i / SAMPLE_RATE
        env = math.exp(-t * 28.0)
        val = 0.22 * (math.sin(2 * math.pi * 840 * t) + 0.5 * math.sin(2 * math.pi * 1420 * t)) * env
        left_channel[idx] += val * 0.3
        right_channel[idx] += val * 0.7 # Más a la derecha

add_vending_clink(9.85)

# -------------------------------------------------------------------------
# 7. EXPORTAR A WAV ESTÉREO 16-BIT PCM
# -------------------------------------------------------------------------
out_dir = "/home/rootkit/Proyectos/konbini-diorama"
os.makedirs(out_dir, exist_ok=True)
wav_path = os.path.join(out_dir, "konbini_rain_soundtrack.wav")

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

print(f"Audio Konbini generado exitosamente: {wav_path} ({len(frames_data)} bytes)")
