# Laboratorio 2 - Setup para proyectos de señales
Este es un tutorial para usar Git y Github.
Veremos como crear un entorno virtual para mantener tu proyecto organizado con todas sus dependencias y posteriormente simular señales fisiológicas.


## Crear un entorno en GitBash

### Configuración inicial
```bash
# Inicializar repositorio Git
git init

# Configurar usuario (solo primera vez)
git config --global user.name "TuNombre"
git config --global user.email "tu@email.com"
```

1.	Abrimos Git Bash y navegamos hasta la carpeta donde deseamos crear el repositorio.

![abrir git bash](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen1.png)

2. Verificamos que Python esté instalado en el sistema y, a continuación, procedemos a crear el entorno virtual.
   
   ![python](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen2.png)
3. Podemos activar y desactivar el entorno según sea necesario
   
   ![entorno1](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen3.png)
   ![entorno2](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen4.png)
   
4. Instalamos las librerías requeridas para el proyecto dentro del entorno recién creado.

   ![entorno3](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen5.png)
   
5. Verificamos las librerías y dependencias que se han instalado correctamente durante el proceso.

   ![entorno4](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen6.png)
   
6. Guardamos la lista de dependencias instaladas en un archivo .txt, el cual se almacenará en la ubicación del entorno virtual. Esto puede ser útil para reusar las mismas dependencias en el futuro.

![entorno5](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen7.png)
   ![entorno6](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen8.png)
   
7. ¡Listo! Ya tenemos el entorno con todas sus dependencias instaladas. Ahora podemos agregar el archivo requirements.txt a nuestro repositorio de GitHub, lo que permitirá que otros colaboradores reproduzcan el entorno fácilmente.
   
## Simular señales fisiológicas artificiales

1. Si aún no tenemos las dependencias necesarias, podemos utilizar el archivo requirements.txt para instalarlas en nuestro entorno local. Simplemente ejecutamos el siguiente comando:
```bash
# Instalar dependencias 
pip install -r requirements.txt
```
### Señales ECG

A continuación se presenta el código utilizado para simular dos señales ECG diferentes (60 y 120 BPM) con distintos niveles de ruido, junto con su visualización en el dominio del tiempo y de la frecuencia (FFT):

```python
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

# ECG 60 - Tiempo
plt.subplot(2, 2, 1)
plt.plot(t, ecg60, color="blue", label="ECG 60 BPM")
plt.title("ECG 60 BPM - Con ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

# ECG 60 - Frecuencia
plt.subplot(2, 2, 2)
plt.plot(f60, m60, color="red", label="ECG 60 BPM (Frecuencia)")
plt.title("ECG 60 BPM - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,80)
plt.ylabel("Magnitud")
plt.legend()

# ECG 120 - Tiempo
plt.subplot(2, 2, 3)
plt.plot(t, ecg120, color="green", label="ECG 120 BPM")
plt.title("ECG 120 BPM - Ruido reducido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

# ECG 120 - Frecuencia
plt.subplot(2, 2, 4)
plt.plot(f120, m120, color="orange", label="ECG 120 BPM (Frecuencia)")
plt.title("ECG 120 BPM - Dominio de la Frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(0,80)
plt.ylabel("Magnitud")
plt.legend()

plt.tight_layout()
plt.show()

