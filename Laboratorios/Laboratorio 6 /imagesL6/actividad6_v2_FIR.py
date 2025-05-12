import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import freqz, filtfilt
from opensignalsreader import OpenSignalsReader

# Leer señal desde archivo OpenSignals
acq = OpenSignalsReader("3derEjercicio.txt")
ecg_signal = acq.signal([2])  # 1 para EMG, 2 para ECG
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")
tiempo = np.linspace(0, len(ecg_signal) / fs, len(ecg_signal))

# Leer coeficientes FIR desde archivo CSV exportado por PyFDA
df = pd.read_csv('filtro_pasabandas_fir_blackman_n96.csv', header=None)
b_pyfda = df[0].to_numpy()
a_pyfda = 1  # FIR: coeficientes a = 1

# Visualizar la respuesta en frecuencia del filtro
w, h = freqz(b_pyfda, worN=8000, fs=fs)
plt.figure()
plt.plot(w, 20 * np.log10(np.abs(h)))
plt.title("Respuesta en frecuencia del filtro FIR")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Ganancia [dB]")
plt.grid(True)
plt.tight_layout()
#plt.show()

# Aplicar filtro FIR
signal_filtrada = filtfilt(b_pyfda, a_pyfda, ecg_signal)

# Escalar para mantener amplitud comparable
max_original = np.max(np.abs(ecg_signal))
max_filtrada = np.max(np.abs(signal_filtrada))
signal_filtrada *= max_original / max_filtrada

# Graficar señal filtrada
plt.figure(figsize=(12, 4))
plt.plot(tiempo, signal_filtrada, label='Señal filtrada', color='blue')
plt.title("Señal filtrada (FIR Blackman N=96) Ejercicio 3der")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid()
plt.xlim(5, 10)
plt.tight_layout()
plt.savefig("ecg_señal_filtrada_ejer3der_fir_black.png")
