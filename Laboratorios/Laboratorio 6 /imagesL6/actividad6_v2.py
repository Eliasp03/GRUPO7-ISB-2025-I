import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import freqz, filtfilt
from opensignalsreader import OpenSignalsReader

# Leer señal desde archivo OpenSignals
acq = OpenSignalsReader("3derEjercicio.txt")
ecg_signal = acq.signal([2]) # 1 para EMG, 2 para ECG
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")
tiempo = np.linspace(0, len(ecg_signal) / fs, len(ecg_signal))

# Leer coeficientes de filtro desde archivo CSV exportado por PyFDA
df = pd.read_csv('filtro_pasabandas_iir_butterworth_n6.csv', header=None, sep=',')
b_pyfda = df[0].to_numpy()
a_pyfda = df[1].to_numpy()
print("Coeficientes b:", b_pyfda)
print("Coeficientes a:", a_pyfda)

# === Normalizar ganancia del filtro ===
w, h = freqz(b_pyfda, a_pyfda, worN=8000)
b_pyfda = b_pyfda / np.abs(h).max()

# Visualizar la respuesta en frecuencia del filtro
plt.figure()
plt.plot(w * fs / (2 * np.pi), 20 * np.log10(np.abs(h)))  # Convertir a Hz
plt.title("Respuesta en frecuencia del filtro IIR Butt")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Ganancia [dB]")
plt.grid(True)
plt.tight_layout()
#plt.savefig("respuesta_frecuencia_filtro.png")
#plt.show()

# Aplicar filtro FIR a la señal ECG o EMG
signal_filtrada = filtfilt(b_pyfda, a_pyfda, ecg_signal)

# === Escalamiento de la señal filtrada para mantener amplitud comparable ===
max_original = np.max(np.abs(ecg_signal))
max_filtrada = np.max(np.abs(signal_filtrada))
signal_filtrada *= max_original / max_filtrada

### === Graficar señal original ===
##plt.figure(figsize=(12, 4))
##plt.plot(tiempo, ecg_signal, label='Señal original', color='blue')
##plt.title("Señal original Ejercicio 3der")
##plt.xlabel("Tiempo (s)")
##plt.ylabel("Amplitud (mV)")
##plt.grid()
##plt.xlim(5, 10)
##plt.tight_layout()
##plt.savefig("ecg_señal_cruda_ejer3der.png")

# === Graficar señal filtrada ===
plt.figure(figsize=(12, 4))
plt.plot(tiempo, signal_filtrada, label='Señal filtrada', color='blue')
plt.title("Señal filtrada (Butter N=6) Ejercicio 3der")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid()
plt.xlim(5, 10)
plt.tight_layout()
plt.savefig("ecg_señal_filtrada_ejer3der_butt.png")
