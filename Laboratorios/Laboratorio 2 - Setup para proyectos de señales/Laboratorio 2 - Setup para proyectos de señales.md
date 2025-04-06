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

### 1.	Abrimos Git Bash y navegamos hasta la carpeta donde deseamos crear el repositorio.

   ![abrir git bash](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen1.png)

### 2. Verificamos que Python esté instalado en el sistema y, a continuación, procedemos a crear el entorno virtual.
   
   ![python](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen2.png)
### 3. Podemos activar y desactivar el entorno según sea necesario
   
   ![entorno1](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen3.png)
   ![entorno2](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen4.png)
   
### 4. Instalamos las librerías requeridas para el proyecto dentro del entorno recién creado.

   ![entorno3](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen5.png)
   
### 5. Verificamos las librerías y dependencias que se han instalado correctamente durante el proceso.

   ![entorno4](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen6.png)
   
### 6. Guardamos la lista de dependencias instaladas en un archivo .txt, el cual se almacenará en la ubicación del entorno virtual. Esto puede ser útil para reusar las mismas dependencias en el futuro.

![entorno5](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen7.png)
   ![entorno6](https://github.com/Eliasp03/GRUPO7-ISB-2025-I/blob/main/Laboratorios/Laboratorio%202%20-%20Setup%20para%20proyectos%20de%20se%C3%B1ales/Images%20L2/Imagen8.png)
   
### 7. ¡Listo! Ya tenemos el entorno con todas sus dependencias instaladas. Ahora podemos agregar el archivo requirements.txt a nuestro repositorio de GitHub, lo que permitirá que otros colaboradores reproduzcan el entorno fácilmente.
   
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
#### Paso 2. Se simula la primera señal ECG
```python
# -------- ECG 1 --------
duration_ecg = 10
fs = 1000
ecg1 = nk.ecg_simulate(duration=duration_ecg, sampling_rate=fs, heart_rate=70)
tiempo_ecg1 = np.linspace(0, duration_ecg, len(ecg1))
```
#### Paso 3. Se procede a guardar la gráfica de la primera señal ECG en el dominio del tiempo y frecuencia
```python
plt.figure(figsize=(10, 3))
plt.plot(tiempo_ecg1, ecg1)
plt.title("ECG 1 - HR 70 bpm (Tiempo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.savefig("ecg1_time.png", bbox_inches="tight") # Comando encargado de guardar en la carpeta, "tight" sirve para centrar la imagen
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
```
##### Gráfica obtenida:

**ECG 1 – Dominio del tiempo**

![ECG 1 Tiempo](./Images%20L2/ecg1_time.png)

**ECG 1 – Dominio de la frecuencia**

![ECG 1 Frecuencia](./Images%20L2/ecg1_freq.png)

#### Paso 4. Se simula la segunda señal ECG
```python
# -------- ECG 2 --------
ecg2 = nk.ecg_simulate(duration=duration_ecg, sampling_rate=fs, heart_rate=90)
tiempo_ecg2 = np.linspace(0, duration_ecg, len(ecg2))
```
#### Paso 5. Se procede a guardar la gráfica de la segunda señal ECG en el dominio del tiempo y frecuencia
```python
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
```
##### Gráfica obtenida:

**ECG 2 – Dominio del tiempo**

![ECG 2 Tiempo](./Images%20L2/ecg2_time.png)

**ECG 2 – Dominio de la frecuencia**

![ECG 2 Frecuencia](./Images%20L2/ecg2_freq.png)

#### Paso 6. Se simula la primera señal EMG
```python
# -------- EMG 1 --------
duration_emg = 5
emg1 = nk.emg_simulate(duration=duration_emg, sampling_rate=fs, burst_number=2)
tiempo_emg1 = np.linspace(0, duration_emg, len(emg1))
```
#### Paso 7. Se procede a guardar la gráfica de la primera señal EMG en el dominio del tiempo y frecuencia 
```python
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
```
##### Gráfica obtenida:

**EMG 1 – Dominio del tiempo**

![EMG_1 Tiempo](./Images%20L2/emg1_time.png)

**EMG 1 – Dominio de la frecuencia**

![EMG_1 Frecuencia](./Images%20L2/emg1_freq.png)

#### Paso 8. Se simula la segunda señal EMG
```python
# -------- EMG 2 --------
emg2 = nk.emg_simulate(duration=duration_emg, sampling_rate=fs, burst_number=4)
tiempo_emg2 = np.linspace(0, duration_emg, len(emg2))
```
#### Paso 9. Se procede a guardar la gráfica de la segunda señal EMG en el dominio del tiempo y frecuencia 
```python
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
```
##### Gráfica obtenida:

**EMG 2 – Dominio del tiempo**

![EMG 2 Tiempo](./Images%20L2/emg2_time.png)

**EMG 2 – Dominio de la frecuencia**

![EMG 2 Frecuencia](./Images%20L2/emg2_freq.png)

#### Dato adicional: El archivo .py lo puedes encontrar como 'signals_plot.py' ubicado dentro de la carpeta 'Laboratorio 2 -Setup para proyectos de señales'
