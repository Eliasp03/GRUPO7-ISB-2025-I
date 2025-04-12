import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import neurokit2 as nk
from opensignalsreader import OpenSignalsReader
from scipy.signal import butter, filtfilt

# Leer archivo de OpenSignals
acq = OpenSignalsReader("LeveBiceps3.txt")

# Imprimir canales disponibles
print("Canales disponibles:", acq.channels)

emg_signal = acq.signal([1])  # seleccionamos el canal del sensor

# Obtener frecuencia de muestreo automáticamente del archivo
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")

# Crear eje de tiempo
tiempo = np.linspace(0, len(emg_signal) / fs, len(emg_signal))

# Graficar señal cruda
plt.figure(figsize=(10, 4))
plt.plot(tiempo, emg_signal, label="EMG cruda")
plt.title("Señal EMG cruda – Bíceps")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("emg_cruda.png")
plt.show()

# Procesar señal con NeuroKit2
signals, info = nk.emg_process(emg_signal, sampling_rate=fs, method="threshold", threshold=0.01)

# Graficar señal procesada
nk.emg_plot(signals,info)
plt.tight_layout()
plt.savefig("emg_procesada.png")
plt.show()

# Parámetros
N = 2**10           # Número de puntos para FFT (resolución)

# FFT - Magnitud
signal_fft = np.fft.fft(emg_signal, N)
signal_fft = np.round(np.abs(signal_fft), 3)[0:N//2]  # Tomar mitad (simetría)
signal_aux = signal_fft / signal_fft.max()            # Escala normalizada

# FFT - Escala logarítmica (dB)
with np.errstate(divide='ignore'):
    signal_fft_db = 10 * np.log10(signal_aux)

# Eje de frecuencia
F_list = np.linspace(0, fs / 2, N // 2)

# Frecuencia dominante
F = np.round(F_list[np.argmax(signal_fft_db)], 1)

# Gráfico del dominio de la frecuencia
plt.figure(figsize=(10, 4))
plt.plot(F_list, signal_fft_db, label="FFT EMG")
plt.text(F, signal_fft_db[np.argmax(signal_fft_db)], f"{F} Hz", fontsize=10, color='red')  # marcar pico
plt.grid(linestyle=":")
plt.ylabel("Magnitud (dB)")
plt.xlabel("Frecuencia (Hz)")
plt.title("Espectro de Frecuencia – FFT en Decibelios")
plt.xlim([0, 200])
plt.xticks(np.arange(0, 201, 10))
plt.legend()
plt.tight_layout()
plt.savefig("emg_fft1.png")
plt.show()

# Definir filtro pasa banda (10-450 Hz) típico para EMG
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype="band")
    return b, a

def apply_bandpass_filter(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Aplicar el filtro
emg_filtered = apply_bandpass_filter(emg_signal, lowcut=20, highcut=450, fs=fs)

# Graficar señal EMG filtrada
plt.figure(figsize=(10, 4))
plt.plot(tiempo, emg_filtered, label="EMG filtrada", color='purple')
plt.title("Señal EMG Filtrada – Pasa banda (20–450 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("emg_signal_filtered.png")
plt.show()

# FFT de la señal EMG filtrada
signal_fft_filt = np.fft.fft(emg_filtered, N)
signal_fft_filt = np.round(np.abs(signal_fft_filt), 3)[0:N//2]
signal_aux_filt = signal_fft_filt / signal_fft_filt.max()

with np.errstate(divide='ignore'):
    signal_fft_db_filt = 10 * np.log10(signal_aux_filt)

F_filt = np.round(F_list[np.argmax(signal_fft_db_filt)], 1)

# Gráfico FFT filtrada
plt.figure(figsize=(10, 4))
plt.plot(F_list, signal_fft_db_filt, label="FFT EMG Filtrada", color="green")
plt.text(F_filt, signal_fft_db_filt[np.argmax(signal_fft_db_filt)], f"{F_filt} Hz", fontsize=10, color='red')
plt.grid(linestyle=":")
plt.ylabel("Magnitud (dB)")
plt.xlabel("Frecuencia (Hz)")
plt.title("Espectro de Frecuencia – EMG Filtrada")
plt.xlim([0, 200])
plt.xticks(np.arange(0, 201, 10))
plt.legend()
plt.tight_layout()
plt.savefig("emg_fft_filtered.png")
#plt.show()
