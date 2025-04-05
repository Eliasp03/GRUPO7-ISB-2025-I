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

# Señal EMG
fs = 1000
duration = 10
t2 = np.linspace(0, duration, fs * duration)
emg1 = nk.emg_simulate(duration=duration, sampling_rate=fs, burst_number=2, burst_duration=1.5)
emg2 = nk.emg_simulate(duration=duration, sampling_rate=fs, burst_number=4, burst_duration=1.5)
emg3 = nk.emg_simulate(duration=duration, sampling_rate=fs, burst_number=5, burst_duration=1.0)

# FFT
f1, m1 = fft(emg1, fs)
f2, m2 = fft(emg2, fs)
f3, m3 = fft(emg3, fs)

plt.figure(figsize=(12, 8))

plt.subplot(6, 1, 1) 
plt.plot(t2, emg1, color="blue") 
plt.title("EMG: 2 ráfagas, duración 1.5s") 
plt.xlabel("Tiempo (s)") 
plt.ylabel("Amplitud")

plt.subplot(6, 1, 2) 
plt.plot(f1, m1, color="blue", label="EMG 2 ráfagas")
plt.title("EMG: 2 ráfagas - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,500)
plt.ylabel("Magnitud")

plt.subplot(6, 1, 3) 
plt.plot(t2, emg2, color="red") 
plt.title("EMG: 4 ráfagas, duración 1.5s") 
plt.xlabel("Tiempo (s)") 
plt.ylabel("Amplitud")

plt.subplot(6, 1, 4) 
plt.plot(f2, m2, color="red", label="EMG 4 ráfagas")
plt.title("EMG: 4 ráfagas - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,500)
plt.ylabel("Magnitud")

plt.subplot(6, 1, 5) 
plt.plot(t2, emg3, color="yellow") 
plt.title("EMG: 5 ráfagas, duración 1s") 
plt.xlabel("Tiempo (s)") 
plt.ylabel("Amplitud")

plt.subplot(6, 1, 6) 
plt.plot(f3, m3, color="yellow", label="EMG 5 ráfagas")
plt.title("EMG: 5 ráfagas - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,500)
plt.ylabel("Magnitud")

plt.tight_layout()
plt.show()