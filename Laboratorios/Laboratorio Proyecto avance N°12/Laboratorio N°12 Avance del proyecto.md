# Laboratorio 12 - Avance del proyecto

## Proyecto: Análisis de señales EMG para detección de patrones de fatiga muscular en miembro inferior

## 🎯 Objetivo

Desarrollar un pipeline en Python que permita analizar señales electromiográficas (EMG) de miembros inferiores para identificar posibles patrones de fatiga muscular, basándose en características extraídas del dominio temporal y su evolución durante caminatas prolongadas.

## Contenido
1. [Origen de los datos](#id1)
2. [Procedimiento de preprocesamiento](#id2)
3. [Extracción de características](#id3)
   - [Características basadas en energía de bandas](#id4)
   - [Características basadas en Wavelet](#id5) 
4. [Organización del proyecto](#id6)

---

## 1. Origen de los datos <a name="id1"></a>

Se utilizará la base de datos pública:

**📚 Nombre:**  
*Surface electromyographic signals collected during long-lasting ground walking of young able-bodied subjects*

**🔗 Enlace:**  
[PhysioNet - semg/1.0.1](https://physionet.org/content/semg/1.0.1/)

**Descripción:**

- Señales **sEMG** obtenidas de **10 músculos del miembro inferior** (5 por pierna) y separados por canales dentro del archivo .hea:
- 
| Canal | Etiqueta del canal | Músculo                 | Lado      |
| :---: | ------------------ | ----------------------- | --------- |
|   2   | `semg LT TIB.A`    | Tibialis anterior       | Izquierdo |
|   3   | `semg LT LAT.G`    | Gastrocnemius lateralis | Izquierdo |
|   4   | `semg LT REC.F`    | Rectus femoris          | Izquierdo |
|   5   | `semg LT HAM`      | Hamstrings              | Izquierdo |
|   6   | `semg LT LAT.V`    | Vastus lateralis        | Izquierdo |
|   9   | `semg RT TIB.A`    | Tibialis anterior       | Derecho   |
|   10  | `semg RT LAT.G`    | Gastrocnemius lateralis | Derecho   |
|   11  | `semg RT REC.F`    | Rectus femoris          | Derecho   |
|   12  | `semg RT HAM`      | Hamstrings              | Derecho   |
|   13  | `semg RT LAT.V`    | Vastus lateralis        | Derecho   |
  
- Datos de **31 sujetos sanos** (20–30 años), caminando durante **~5 minutos** por una ruta en forma de “8” (curvas + tramos rectos).
- Registro simultáneo de:  
  - sEMG (μV)  
  - Footswitch (V)  
  - Electrogoniometría (°)
- Formato de archivo: `.dat` y `.hea` (compatible con `wfdb` en Python)
- Frecuencia de muestreo: **2000 Hz**  
- Resolución: **12 bits**  
- Alta fidelidad (CMRR > 126 dB, ruido < 1 µV rms)

**Justificación de uso:**  

Aunque no se indujo fatiga muscular intencionadamente, la duración de la caminata permite explorar la **variabilidad intra-sujeto** a lo largo del tiempo. Esto hace posible identificar **patrones progresivos relacionados con fatiga local o ajustes neuromusculares**.

---

## 2. Procedimiento de preprocesamiento <a name="id2"></a>

1. **Lectura y visualización inicial**:  
   Carga de los archivos con la librería `wfdb`.

2. **Filtrado de señales EMG**:  
   - Pasa banda Butterworth (20–450 Hz)  
   - Filtro notch (50/60 Hz) si es necesario  

3. **Rectificación**:  
   Conversión a valores absolutos.

4. **Segmentación temporal**:  
   División de la señal en bloques para observar evolución de características.

5. **Normalización**:  
   - Z-score u otra estrategia si se requiere para comparación intersujeto.

---

## 3. Extracción de características <a name="id3"></a>

Por cada ventana de tiempo, se calcularán las siguientes métricas EMG en el dominio temporal:

| Característica | Interpretación |
|----------------|----------------|
| **RMS** (Root Mean Square) | Medida de la energía muscular |
| **MAV** (Mean Absolute Value) | Actividad promedio |
| **ZC** (Zero Crossings) | Complejidad / frecuencia del contenido |
| **SSC** (Slope Sign Changes) | Variabilidad / oscilaciones |
| **WL** (Waveform Length) | Longitud del contorno de señal |

Estas métricas serán analizadas en función del tiempo para identificar **tendencias relacionadas con la aparición de fatiga**.

---

## 4. 🗺️ Organización del proyecto <a name="id6"></a>
⚙️ Tecnologías utilizadas

|Tecnología	| Descripción |
|----------------|----------------|
|PyQt5	| Diseño de la interfaz gráfica (ventanas, botones, formularios)| 
|WFDB	 | Lectura de archivos .dat y .hea de PhysioNet|
|Matplotlib	|Visualización de señales y exportación a PDF|
|Scipy.signal		|Filtros digitales para procesamiento de la señal|
|NumPy	|Cálculos matemáticos eficientes|
|PyPDF	|Exportación de análisis a PDF|

### Desarrollo: 

🔹 Paso 1: Se importa las librerías necesarias a utilizar para el proyecto y fines del mismo:
```bash
import sys
import re
import wfdb
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pywt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QStackedWidget,
    QFormLayout, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument
```

🔹 Paso 2: Interfaz de ingreso de datos del paciente:

Se implementó un formulario para ingresar y validar la información del paciente antes del análisis.

```bash
# Fragmento
form.addRow("<b>Nombre:</b>", self.name_input)
form.addRow("<b>Edad:</b>", self.age_input)
form.addRow("<b>DNI:</b>", self.dni_input)
form.addRow("<b>Correo electrónico:</b>", self.email_input)
```
Validaciones: Edad numérica, DNI con 8 dígitos, formato de email válido.
Se obtiene lo siguiente en la aplicación:
![](L12_images/output1.png)

🔹 Paso 3: Carga del archivo .hea:
Al presionar el botón "Seleccionar archivo", el usuario elige el archivo .hea correspondiente a un sujeto del estudio. Aquí se usan funciones de la librería wfdb para importar la señal y obtener metadatos.
```bash
path, _ = QFileDialog.getOpenFileName(self, "Cargar .hea", "", "*.hea")
record = wfdb.rdrecord(path.replace(".hea", ""))
```
Se obtiene lo siguiente en la aplicación:
![](L12_images/output2.png)
![](L12_images/output2_2.png)
![](L12_images/output2_3.png)

🔹 Paso 4: Filtrado y rectificación de la señal EMG:
Una vez cargada, se selecciona un canal EMG y se aplica un filtro Butterworth pasa banda (20–450 Hz) seguido de rectificación. Este paso elimina ruido y transforma la señal en forma positiva para análisis.
```bash
b, a = signal.butter(4, [20/(fs/2), 450/(fs/2)], btype='band')
filtered = signal.filtfilt(b, a, emg_signal)
rectified = np.abs(filtered)
```
Se obtiene lo siguiente en la aplicación:
![](L12_images/output3.png)

🔹 Paso 5: Cálculo de características del dominio temporal:
Se implementan las métricas estándar de análisis EMG sobre la señal rectificada. Estas características permiten cuantificar actividad, complejidad y fatiga muscular.
```bash
rms = np.sqrt(np.mean(rectified**2))
mav = np.mean(rectified)
zc = np.sum(np.diff(np.sign(rectified)) != 0)
ssc = np.sum(np.diff(np.sign(np.diff(rectified))) != 0)
wl = np.sum(np.abs(np.diff(rectified)))
```
Se obtiene lo siguiente en la aplicación:
![](L12_images/output4.png)

🔹 Paso 6: Exportación a PDF del análisis:
Los resultados y gráficos se integran en un documento PDF personalizado para cada paciente. Esto nos permite generar informes clínicos o reportes de laboratorio de forma automática.
```bash
with PdfPages(file_path) as pdf:
    self.figure.suptitle(f"Paciente: {self.user_info['name']}, DNI: {self.user_info['dni']}", fontsize=12)
    pdf.savefig(self.figure, bbox_inches='tight')
```
Se obtiene lo siguiente en la aplicación:
![](L12_images/output5.png)
![](L12_images/output5_2.png)
![](L12_images/output5_3.png)
