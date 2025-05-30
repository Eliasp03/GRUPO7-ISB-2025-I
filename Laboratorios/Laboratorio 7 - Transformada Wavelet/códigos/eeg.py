import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.signal import find_peaks

eeg_signals = np.genfromtxt("lectura.txt", delimiter="\t",skip_header = 3, missing_values= 0)
# Extraemos la columna de la señal
chn = 5
eeg_signal = eeg_signals[:, chn]
eeg_signal = eeg_signal - np.mean(eeg_signal)
Fs_eeg = 1000
Ts_eeg = 1/Fs_eeg
n_eeg= len(eeg_signal)
t_eeg = np.arange(0,n_eeg*Ts_eeg,Ts_eeg)


## Ploteamos las señales sin filtrar

plt.figure(figsize=(10, 5))
plt.xlim(38,42)
plt.plot(t_eeg, eeg_signal, label="señal")      # graficamos la señal
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal - Original Lectura")
plt.show()

n_level = 5
eeg_coeffs = pywt.wavedec(eeg_signal, 'bior2.6', level=n_level)

threshold = 16
eeg_coeffs_thresh = [pywt.threshold(c, threshold, mode='soft') for c in eeg_coeffs]

filtered_eeg_signal = pywt.waverec(eeg_coeffs_thresh, 'bior2.6')

plt.figure(figsize=(10, 5))
plt.plot(t_eeg, filtered_eeg_signal)
plt.xlim(38,42)
plt.title('Señal EEG - Filtrada Lectura')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.tight_layout()
plt.show()
