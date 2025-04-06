# Importar paquetes
import neurokit2 as nk
import matplotlib
matplotlib.use("Agg") #para evitar errores de interfaz gráfica en Windows
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np

# -------- ECG 1 --------
duration_ecg = 10
fs = 1000
ecg1 = nk.ecg_simulate(duration=duration_ecg, sampling_rate=fs, heart_rate=70)
tiempo_ecg1 = np.linspace(0, duration_ecg, len(ecg1))

plt.figure(figsize=(10, 3))
plt.plot(tiempo_ecg1, ecg1)
plt.title("ECG 1 - HR 70 bpm (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("ecg1_time.png", bbox_inches="tight")
plt.close()

plt.figure()
f1, Pxx1 = signal.welch(ecg1, fs=fs)
plt.semilogy(f1, Pxx1)
plt.title("ECG 1 - Espectro de frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia")
plt.xlim(0, 1000)
plt.grid(True)
plt.savefig("ecg1_freq.png", bbox_inches="tight")
plt.close()

# -------- ECG 2 --------
ecg2 = nk.ecg_simulate(duration=duration_ecg, sampling_rate=fs, heart_rate=90)
tiempo_ecg2 = np.linspace(0, duration_ecg, len(ecg2))

plt.figure(figsize=(10, 3))
plt.plot(tiempo_ecg2, ecg2, color='red')
plt.title("ECG 2 - HR 90 bpm (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("ecg2_time.png", bbox_inches="tight")
plt.close()

plt.figure()
f2, Pxx2 = signal.welch(ecg2, fs=fs)
plt.semilogy(f2, Pxx2)
plt.title("ECG 2 - Espectro de frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia")
plt.xlim(0, 1000)
plt.grid(True)
plt.savefig("ecg2_freq.png", bbox_inches="tight")
plt.close()

# -------- EMG 1 --------
duration_emg = 5
emg1 = nk.emg_simulate(duration=duration_emg, sampling_rate=fs, burst_number=2)
tiempo_emg1 = np.linspace(0, duration_emg, len(emg1))

plt.figure(figsize=(10, 3))
plt.plot(tiempo_emg1, emg1)
plt.title("EMG 1 - 2 bursts (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("emg1_time.png", bbox_inches="tight")
plt.close()

plt.figure()
f3, Pxx3 = signal.welch(emg1, fs=fs)
plt.semilogy(f3, Pxx3)
plt.title("EMG 1 - Espectro de frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia")
plt.xlim(0, 600)
plt.grid(True)
plt.savefig("emg1_freq.png", bbox_inches="tight")
plt.close()

# -------- EMG 2 --------
emg2 = nk.emg_simulate(duration=duration_emg, sampling_rate=fs, burst_number=4)
tiempo_emg2 = np.linspace(0, duration_emg, len(emg2))

plt.figure(figsize=(10, 3))
plt.plot(tiempo_emg2, emg2, color='purple')
plt.title("EMG 2 - 4 bursts (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("emg2_time.png", bbox_inches="tight")
plt.close()

plt.figure()
f4, Pxx4 = signal.welch(emg2, fs=fs)
plt.semilogy(f4, Pxx4)
plt.title("EMG 2 - Espectro de frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia")
plt.xlim(0, 600)
plt.grid(True)
plt.savefig("emg2_freq.png", bbox_inches="tight")
plt.close()
