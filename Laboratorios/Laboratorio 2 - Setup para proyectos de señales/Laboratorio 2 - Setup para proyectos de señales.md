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
   
## Simulación de señales fisiológicas artificiales (ECG y EMG)

## 🧰 Herramientas utilizadas
- Python 3.12
- Librerías: `neurokit2`, `matplotlib`, `scipy`, `numpy`
- Git y GitHub
- Entorno virtual (`venv`)

### 1. Activar entorno virtual

Desde Git Bash o CMD, ejecutar:

```bash
C:\ISB\mi_entorno2\Scripts\activate
```
### 2. Instalar librerías necesarias
```bash
pip install neurokit2 matplotlib scipy
```
O bien, instalar desde el archivo requirements.txt, para ello deberas descargarlo.
```bash
pip install -r requirements.txt
```
### 3. Crear el archivo de simulación
Puedes crear un archivo .py directamente desde la terminal:
```bash
notepad signals_plot.py
```
Esto abrirá el Bloc de notas. Allí puedes pegar tu código Python y guardarlo con extensión .py.
⚠️ Asegúrate de estar en la misma carpeta donde deseas guardar el archivo

### 4.  Simulación de señales fisiológicas con NeuroKit2
El archivo signals_plot.py debe contener el código para generar 4 señales:
- 2 señales ECG usando nk.ecg_simulate() con diferentes frecuencias cardíacas.
- 2 señales EMG usando nk.emg_simulate() con distintos patrones de bursts.

A continuación se presenta el código utilizado para simular dos señales ECG diferentes con distintos niveles de ruido, junto con su visualización en el dominio del tiempo y de la frecuencia:
#### Paso 1. Se importa las librerías previamente instaladas
```python
# Importar paquetes
import neurokit2 as nk
import matplotlib
matplotlib.use("Agg") #para evitar errores de interfaz gráfica en Windows
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
```
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
```

### Señales ECG

A continuación se presenta el código utilizado para simular dos señales EMG diferentes.

```python
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
