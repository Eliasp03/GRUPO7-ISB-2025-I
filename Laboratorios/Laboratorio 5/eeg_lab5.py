import numpy as np
import matplotlib.pyplot as plt
import neurokit2 as nk

# Leer archivo y extraer la columna 6 (índice 5)
data = np.loadtxt('basal1.txt')
eeg_signal = data[:, 5]
eeg_signal = eeg_signal/100
print(eeg_signal)
# Parámetro de frecuencia de muestreo (ajústalo si es diferente)
sampling_rate = 1000  # Hz
tiempo = np.arange(len(eeg_signal)) / sampling_rate  # Eje temporal en segundos

# Señal cruda
plt.figure(figsize=(12, 4))
plt.plot(tiempo, eeg_signal)
plt.title("Señal EEG Cruda")
plt.xlabel("Tiempo (s)")
plt.ylabel("uV")
plt.grid(True)
plt.tight_layout()
plt.show()

# Espectro de magnitud de la señal cruda
plt.figure(figsize=(12, 4))
plt.magnitude_spectrum(eeg_signal, Fs=sampling_rate, scale='dB')
plt.title("Espectro de Magnitud - Señal Cruda")
plt.grid(True)
plt.tight_layout()
plt.show()

# Filtrado EEG (pasabanda 1–40 Hz)
eeg_filtrada = nk.signal_filter(eeg_signal, sampling_rate=sampling_rate,
                                lowcut=1, highcut=40, method='butterworth', order=5)

# Señal filtrada
plt.figure(figsize=(12, 4))
plt.plot(tiempo, eeg_filtrada)
plt.title("Señal EEG Filtrada (1-40 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("uV")
plt.grid(True)
plt.tight_layout()
plt.show()

# Espectro de magnitud de la señal filtrada
plt.figure(figsize=(12, 4))
plt.magnitude_spectrum(eeg_filtrada, Fs=sampling_rate, scale='dB')
plt.title("Espectro de Magnitud - Señal Filtrada")
plt.grid(True)
plt.tight_layout()
plt.show()

# -------- Welch PSD --------
frequencies, psd = welch(eeg_filtrada, fs=sampling_rate, nperseg=1024)

plt.figure(figsize=(12, 4))
plt.plot(frequencies, psd)
plt.title("PSD – Método de Welch (escala lineal)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia (uV²/Hz)")
plt.xlim(0, 50)
plt.grid(True)
plt.tight_layout()
plt.show()
