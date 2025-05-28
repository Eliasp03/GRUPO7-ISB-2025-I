import numpy as np
import matplotlib.pyplot as plt
import pywt
from opensignalsreader import OpenSignalsReader

# -------- señal ECG --------
archivo = "1derinhaLarga.txt"
acq = OpenSignalsReader(archivo)
ecg_signal = acq.signal([2])  # ECG en canal 2
fs = acq.sampling_rate
print(f"Frecuencia de muestreo: {fs} Hz")

# -------- tiempo --------
tiempo = np.linspace(0, len(ecg_signal) / fs, len(ecg_signal))

# -------- Filtrado Wavelet (Coiflet 3) --------
wavelet = 'coif3'
niveles = 7           # Segun literatura
umbral = 0.2          # Ajustable según el ruido

# Descomposición
coeficientes = pywt.wavedec(ecg_signal, wavelet, level=niveles)

# Umbralización suave
coef_filtrados = [pywt.threshold(c, umbral, mode='soft') for c in coeficientes]

# Reconstrucción
ecg_filtrada = pywt.waverec(coef_filtrados, wavelet)
ecg_filtrada = ecg_filtrada[:len(ecg_signal)]  # Ajustar longitud

# -------- PLOT --------
plt.figure(figsize=(12, 5))
#plt.plot(tiempo, ecg_signal, label='ECG original', color='blue', alpha=0.6)
plt.plot(tiempo, ecg_filtrada, label='ECG filtrada (coif3)', color='black', alpha=0.8)
plt.title("Filtrado de señal ECG con Wavelet Coiflet 3 - Respiracion prolongada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
#plt.legend()
plt.xlim(5, 15)
plt.tight_layout()
plt.savefig("coif3_ecg_respLarga1der_lvl7.png")
plt.show()