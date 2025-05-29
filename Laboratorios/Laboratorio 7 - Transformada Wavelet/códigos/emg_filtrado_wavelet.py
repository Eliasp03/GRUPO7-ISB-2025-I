import numpy as np
import matplotlib.pyplot as plt
import pywt
import pandas as pd
from scipy.signal import freqz, filtfilt
from opensignalsreader import OpenSignalsReader

# Leer señal desde archivo OpenSignals
acq = OpenSignalsReader("max.txt")
emg_signal = acq.signal([1])  # 1 para EMG, 2 para ECG
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")
tiempo = np.linspace(0, len(emg_signal) / fs, len(emg_signal))

# --- Parámetros ---
wavelet = 'db4'
nivel = 5

def calcular_umbral(sig):
    sigma = np.median(np.abs(sig - np.median(sig))) / 0.6745
    n = len(sig)
    return sigma * np.sqrt(2 * np.log(n))

def wavelet_denoise(signal, method):
    coeffs = pywt.wavedec(signal, wavelet, level=nivel)
    thresholded_coeffs = [coeffs[0]]  # Coeficiente de aproximación sin cambios

    print(f"\n--- Método: {method.upper()} ---")
    for j, c in enumerate(coeffs[1:], start=1):
        th = calcular_umbral(c)
        print(f"  Nivel {j}: umbral = {th:.6f} (n = {len(c)})")
        if method == 'hard':
            c_new = pywt.threshold(c, th, mode='hard')
        elif method == 'soft':
            c_new = pywt.threshold(c, th, mode='soft')
        else:
            raise ValueError("Método no válido: 'soft' o 'hard'")
        thresholded_coeffs.append(c_new)

    return pywt.waverec(thresholded_coeffs, wavelet)

# Aplicar los métodos
emg_soft = wavelet_denoise(emg_signal, method='soft')
emg_hard = wavelet_denoise(emg_signal, method='hard')

# --- Gráficas comparativas ---
plt.figure()
plt.plot(tiempo, emg_signal, label='Original', color='black')
plt.title("Señal EMG Original")
plt.xlim(10,20)
plt.grid()

plt.figure()
plt.plot(tiempo, emg_soft, label='Soft Threshold', color='blue')
plt.title("Desnoisado con Umbral Suave (Soft)")
plt.xlim(10,20)
plt.grid()

plt.figure()
plt.plot(tiempo, emg_hard, label='Hard Threshold', color='green')
plt.title("Desnoisado con Umbral Duro (Hard)")
plt.xlim(10,20)
plt.grid()

plt.tight_layout()
plt.show()
