import wfdb
import matplotlib.pyplot as plt
import os

# Ruta al archivo sin extensión (ajusta si cambias de sujeto)
ruta_base = "S01"  # Puedes cambiar a 'S2', 'S3', etc.

# Leer el archivo desde el directorio actual
record = wfdb.rdrecord(ruta_base)

# Mostrar información
print("Canales disponibles:")
for i, nombre in enumerate(record.sig_name):
    print(f"{i}: {nombre}")
print(f"\nFrecuencia de muestreo: {record.fs} Hz")
print(f"Número total de muestras: {record.p_signal.shape[0]}")

# Elegir canal EMG (ajusta el índice si quieres otro músculo)
canal_emg = 2
signal = record.p_signal[:, canal_emg]
fs = record.fs

# Graficar primeros 60 segundos
duracion_seg = 60
n_muestras = int(fs * duracion_seg)
tiempo = [i / fs for i in range(n_muestras)]

plt.figure(figsize=(12, 4))
plt.plot(tiempo, signal[:n_muestras])
plt.title(f"EMG - Canal {record.sig_name[canal_emg]} (primeros {duracion_seg} s)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [μV]")
plt.grid(True)
plt.tight_layout()
plt.show()
