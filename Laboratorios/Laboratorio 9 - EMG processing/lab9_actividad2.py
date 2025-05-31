import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.stats import linregress

# 1. Simular señales de 3 segmentos
segmentos = []
duracion_segmento = 10  # en segundos
sampling_rate = 1000

# Patrones de fatiga: menos ráfagas, más amplitud
burst_nums = [10, 7, 4]
amplitudes = [1.0, 1.5, 2.0]

for bursts, amp in zip(burst_nums, amplitudes):
    seg = nk.emg_simulate(duration=duracion_segmento, sampling_rate=sampling_rate,
                          burst_number=bursts, noise=0.01)
    seg *= amp
    segmentos.append(seg)

# Concatenar señal completa de 30s
emg_total = np.concatenate(segmentos)

# 2. Limpieza y envolvente
emg_clean = nk.emg_clean(emg_total, sampling_rate=sampling_rate)
emg_envelope = nk.emg_amplitude(emg_clean)

# 3. Ventanas de 1 segundo (1000 muestras)
ventana = 1000
rms_values = []
fmed_values = []
tiempos = []

for i in range(0, len(emg_envelope), ventana):
    ventana_signal = emg_envelope[i:i+ventana]
    
    if len(ventana_signal) < ventana:
        continue  # descartar incompleto al final

    # RMS
    rms = np.sqrt(np.mean(ventana_signal**2))
    rms_values.append(rms)

    # Frecuencia mediana usando Welch
    freqs, psd = welch(ventana_signal, fs=sampling_rate)
    cumsum_psd = np.cumsum(psd)
    total_power = cumsum_psd[-1]
    fmed = freqs[np.where(cumsum_psd >= total_power / 2)[0][0]]
    fmed_values.append(fmed)

    # Tiempo central de la ventana
    tiempos.append((i + ventana/2) / sampling_rate)

# 4. Regresiones lineales
rms_slope, _, _, _, _ = linregress(tiempos, rms_values)
fmed_slope, _, _, _, _ = linregress(tiempos, fmed_values)

# 5. Graficar resultados
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(tiempos, rms_values, marker='o', label=f'Slope = {rms_slope:.4f}')
plt.xlabel("Tiempo (s)")
plt.ylabel("RMS")
plt.title("RMS vs Tiempo")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(tiempos, fmed_values, marker='o', color='orange', label=f'Slope = {fmed_slope:.4f}')
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia mediana (Hz)")
plt.title("Frecuencia Mediana vs Tiempo")
plt.legend()

plt.tight_layout()
plt.show()

# Imprimir resultados
print(f"Pendiente RMS: {rms_slope:.4f}")
print(f"Pendiente Frecuencia Mediana: {fmed_slope:.4f}")
