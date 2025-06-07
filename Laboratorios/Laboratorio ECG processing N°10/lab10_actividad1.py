import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np

# Parámetros
duration = 20  # segundos
sampling_rate = 1000  # Hz
heart_rate_1 = 70
heart_rate_2 = 90

# Señal 1: ECG con HR = 70 bpm
ecg1 = nk.ecg_simulate(duration=duration, 
                       sampling_rate=sampling_rate, 
                       heart_rate=heart_rate_1, 
                       method='ecgsyn')

# Señal 2: ECG con HR = 90 bpm
ecg2 = nk.ecg_simulate(duration=duration, 
                       sampling_rate=sampling_rate, 
                       heart_rate=heart_rate_2, 
                       method='ecgsyn')

# Crear vector de tiempo
time = np.linspace(0, duration, duration * sampling_rate)

# Graficar ECG 1
plt.figure(figsize=(12, 4))
plt.plot(time, ecg1)
plt.title("ECG Simulado 1 - HR 70 bpm")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Graficar ECG 2
plt.figure(figsize=(12, 4))
plt.plot(time, ecg2, color='orange')
plt.title("ECG Simulado 2 - HR 90 bpm")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()
