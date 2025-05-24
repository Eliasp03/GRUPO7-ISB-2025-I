import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import freqz, filtfilt
from opensignalsreader import OpenSignalsReader

# Leer señal desde archivo OpenSignals
acq = OpenSignalsReader("1derRespiracion.txt")
ecg_signal = acq.signal([2]) # 1 para EMG, 2 para ECG
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")
tiempo = np.linspace(0, len(ecg_signal) / fs, len(ecg_signal))

### Grafica
plt.figure(figsize=(12, 4))
plt.plot(tiempo, ecg_signal, label='Señal original', color='blue')
plt.title("Señal original Respiración 1der")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid()
plt.xlim(5, 15)
plt.tight_layout()
plt.savefig("ecg_resp1der.png")