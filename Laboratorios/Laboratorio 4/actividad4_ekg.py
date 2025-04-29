import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import neurokit2 as nk
from opensignalsreader import OpenSignalsReader
from scipy.signal import butter, filtfilt

# Leer archivo de OpenSignals
acq = OpenSignalsReader("3derinhaLarga2.txt")

# Imprimir canales disponibles
print("Canales disponibles:", acq.channels)

ecg_signal = acq.signal([2])  # seleccionamos el canal del sensor

# Obtener frecuencia de muestreo automáticamente del archivo
fs = acq.sampling_rate
print("Frecuencia de muestreo:", fs, "Hz")

# Crear eje de tiempo
tiempo = np.linspace(0, len(ecg_signal) / fs, len(ecg_signal))

# Graficar señal cruda
plt.figure(figsize=(10, 4))
plt.plot(tiempo, ecg_signal, label="ECG cruda")
plt.title("Señal ECG cruda 3ra derivada Inhalación Larga")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
plt.legend()
plt.xlim(5, 10)
plt.tight_layout()
plt.savefig("ecg_cruda_3der_inha.png")
plt.show()

# Procesar señal con NeuroKit2
signals, info = nk.ecg_process(ecg_signal, sampling_rate=fs)

# Graficar señal procesada
nk.ecg_plot(signals,info)
plt.tight_layout()
plt.title("Señal ECG procesada neurokit – 3ra derivada Inhalación Larga)")
plt.savefig("ecg_procesada_3der_inha.png", bbox_inches="tight")
#plt.show()

# Parámetros
N = 2**10           # Número de puntos para FFT (resolución)

# FFT - Magnitud
signal_fft = np.fft.fft(ecg_signal, N)
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
plt.plot(F_list, signal_fft_db, label="FFT ECG")
plt.text(F, signal_fft_db[np.argmax(signal_fft_db)], f"{F} Hz", fontsize=10, color='red')
plt.grid(linestyle=":")
plt.ylabel("Magnitud (dB)")
plt.xlabel("Frecuencia (Hz)")
plt.title("Espectro de Frecuencia – FFT[dB] ECG Cruda 3ra derivada Inhalación Larga")
plt.xlim([0, 200])
plt.xticks(np.arange(0, 201, 10))
plt.legend()
plt.tight_layout()
plt.savefig("ecg_fft_cruda_3der_inha.png")
#plt.show()

# Definir filtro pasa banda (entre 0.5 Hz y 40 Hz) típico para ECG
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
ecg_filtered = apply_bandpass_filter(ecg_signal, lowcut=0.5, highcut=40, fs=fs)

# Graficar señal ECG filtrada
plt.figure(figsize=(10, 4))
plt.plot(tiempo, ecg_filtered, label="ECG Filtrada", color='purple')
plt.title("Señal ECG Filtrada – Pasa banda (0.5–40 Hz) 3ra derivada Inhalación Larga")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid(True)
plt.legend()
plt.xlim(5, 10)
plt.tight_layout()
plt.savefig("ecg_signal_filtered_3der_inha.png")
#plt.show()

# FFT de la señal ECG filtrada
signal_fft_filt = np.fft.fft(ecg_filtered, N)
signal_fft_filt = np.round(np.abs(signal_fft_filt), 3)[0:N//2]
signal_aux_filt = signal_fft_filt / signal_fft_filt.max()

with np.errstate(divide='ignore'):
    signal_fft_db_filt = 10 * np.log10(signal_aux_filt)

F_filt = np.round(F_list[np.argmax(signal_fft_db_filt)], 1)

# Gráfico FFT filtrada
plt.figure(figsize=(10, 4))
plt.plot(F_list, signal_fft_db_filt, label="FFT ECG Filtrada", color="green")
plt.text(F_filt, signal_fft_db_filt[np.argmax(signal_fft_db_filt)], f"{F_filt} Hz", fontsize=10, color='red')
plt.grid(linestyle=":")
plt.ylabel("Magnitud (dB)")
plt.xlabel("Frecuencia (Hz)")
plt.title("Espectro de Frecuencia – ECG Filtrada 3ra derivada Inhalación Larga")
plt.xlim([0, 200])
plt.xticks(np.arange(0, 201, 10))
plt.legend()
plt.tight_layout()
plt.savefig("ecg_fft_filtered_3der_inha.png")
#plt.show()
