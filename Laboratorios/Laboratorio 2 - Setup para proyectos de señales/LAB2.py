# Load NeuroKit and other useful packages
import neurokit2 as nk
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simulación ECG
fs = 1000
duration = 8
ecg60 = nk.ecg_simulate(duration=duration, sampling_rate=fs, noise=0.08, heart_rate=60)
ecg120 = nk.ecg_simulate(duration=duration, sampling_rate=fs, noise=0.01, heart_rate=120)
t = np.linspace(0, duration, fs * duration)

# Función para convertir al dominio de la frecuencia
def fft(signal, fs):
    freqs = np.fft.fftfreq(len(signal), 1/fs)
    mag = np.abs(np.fft.fft(signal))
    return freqs[:len(signal)//2], mag[:len(signal)//2]

# FFT
f60, m60 = fft(ecg60, fs)
f120, m120 = fft(ecg120, fs)

# subplots 2x2
plt.figure(figsize=(12, 6))

# ECG 50 - Tiempo
plt.subplot(2, 2, 1)
plt.plot(t, ecg60, color="blue", label="ECG 60 BPM")
plt.title("ECG 60 BPM - Con ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

# ECG 50 - Frecuencia
plt.subplot(2, 2, 2)
plt.plot(f60, m60, color="red", label="ECG 60 BPM (Frecuencia)")
plt.title("ECG 60 BPM - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,80)
plt.ylabel("Magnitud")
plt.legend()

# ECG 100 - Tiempo
plt.subplot(2, 2, 3)
plt.plot(t, ecg120, color="green", label="ECG 120 BPM")
plt.title("ECG 120 BPM - Ruido reducido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

# ECG 100 - Frecuencia
plt.subplot(2, 2, 4)
plt.plot(f120, m120, color="orange", label="ECG 120 BPM (Frecuencia)")
plt.title("ECG 120 BPM - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,80)
plt.ylabel("Magnitud")
plt.legend()

plt.tight_layout()
plt.show()