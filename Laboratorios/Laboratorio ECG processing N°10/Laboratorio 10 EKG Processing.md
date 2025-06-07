# Laboratorio 10 - EKG processing
## Contenido
1. [Actividad 1](#id1)
2. [Actividad 2](#id2)
3. [Actividad 3](#id3)
4. [Actividad 4](#id4)
5. [Actividad para casa](#id5)
6. [Referencias](#id6)


## 1. Actividad 1 <a name="id1"></a>

### Objetivo: 
- Generar 2 señales EKG de duración 20 s
- Gráfica de forma independiente estas señales

### Desarrollo:

1. Importamos las librerías necesarias para su desarrollo:
```bash
import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np
```
2. Definimos los parámetros acorde a lo solicitado:
```bash
duration = 20  # segundos
sampling_rate = 1000  # Hz
heart_rate_1 = 70
heart_rate_2 = 90
```
3. Simulamos la señal ECG mediante la función ecg_simulate() de neurokit v.2:
```bash
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
```
4. Creamos el vector tiempo para realizar la gráfica:
```bash
time = np.linspace(0, duration, duration * sampling_rate)
```
5. Finalmente, graficamos mediante el uso de la librería matplotlib:
```bash
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
```
### Resultados:

![Señales ECG1](./imagenesL10/imagen_actividad1.png)

![Señales ECG2](./imagenesL10/imagen_actividad1_2.png)

## 2. Actividad 2 <a name="id2"></a>

### Objetivo: 
- Para cada señal simulada, extraer las características básicas

### Desarrollo:
1. Importamos las librerías necesarias para su desarrollo:
```bash
import neurokit2 as nk
import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew
import matplotlib.pyplot as plt
```
2. Se mantiene todo el código de la actividad 1, pero se añade para la obtención de los valores:
```bash
signals = [ecg1, ecg2]
labels = ["ECG 1", "ECG 2"]

# Extraer valores específicos
def extract_features(ecg_signal):
    return {
        "Mean": np.mean(ecg_signal),
        "Median": np.median(ecg_signal),
        "STD": np.std(ecg_signal),
        "Kurtosis": kurtosis(ecg_signal),
        "Skewness": skew(ecg_signal),
        "Energy": np.sum(ecg_signal**2)
    }

features = []
for i, ecg in enumerate(signals):
    feats = extract_features(ecg)
    feats["Label"] = labels[i]
    features.append(feats)

df_features = pd.DataFrame(features)
```
3. Finalmente, se imprime los valores en una tabla mediante Pandas:
```bash
print("\n=== Tabla de características estadísticas ===")
print(df_features)
```

### Resultado:
asdsdads

## 3. Actividad 3 <a name="id3"></a>

### Objetivo: 
- Extraer caracteristicas de 3 señasl EKG, reducir la dimensionalidad con PCA y graficas el scatterplot

### Desarrollo:
1. Importamos las librerías necesarias para su desarrollo:
```bash
import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.stats import linregress
```
2. Realizamos la configuración de los segmentos de simulación:
```bash
segmentos = []
duracion_segmento = 10  # en segundos
sampling_rate = 1000
burst_nums = [10, 7, 4]
amplitudes = [1.0, 1.5, 2.0]
```
3. Simulamos cada segmento EMG:
```bash
for bursts, amp in zip(burst_nums, amplitudes):
    seg = nk.emg_simulate(duration=duracion_segmento, sampling_rate=sampling_rate,
                          burst_number=bursts, noise=0.01)
    seg *= amp
    segmentos.append(seg)
```

### Resultado:
asdasda

## 4. Actividad 4 <a name="id4"></a>

### Objetivo: 
- De las 3 señales EKG creada, creado 3 mas adicionales con las mismas caracteristicas de estas 3 iniciales.
- Extrae sus caracteristicas y ponlos en una tabla en pandas, luego etiqueta estas señales. ejemplo: 0,1,2.
- Reduce las dimensionalidad a 2 y grafica si existe separabilidad.

### Desarrollo:
1. Importamos las librerías necesarias para su desarrollo:
```bash
import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.stats import linregress
```
2. Realizamos la configuración de los segmentos de simulación:
```bash
segmentos = []
duracion_segmento = 10  # en segundos
sampling_rate = 1000
burst_nums = [10, 7, 4]
amplitudes = [1.0, 1.5, 2.0]
```
3. Simulamos cada segmento EMG:
```bash
for bursts, amp in zip(burst_nums, amplitudes):
    seg = nk.emg_simulate(duration=duracion_segmento, sampling_rate=sampling_rate,
                          burst_number=bursts, noise=0.01)
    seg *= amp
    segmentos.append(seg)
```

### Resultado:
asdasdasd

## 5. Actividad para casa <a name="id5"></a>

### Objetivo: 
- Continuar con la actividad de clase pero incluir los coeficientes de DWT.

### Desarrollo:
1. Importamos las librerías necesarias para su desarrollo:
```bash
import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.stats import linregress
```
2. Realizamos la configuración de los segmentos de simulación:
```bash
segmentos = []
duracion_segmento = 10  # en segundos
sampling_rate = 1000
burst_nums = [10, 7, 4]
amplitudes = [1.0, 1.5, 2.0]
```
3. Simulamos cada segmento EMG:
```bash
for bursts, amp in zip(burst_nums, amplitudes):
    seg = nk.emg_simulate(duration=duracion_segmento, sampling_rate=sampling_rate,
                          burst_number=bursts, noise=0.01)
    seg *= amp
    segmentos.append(seg)
```

### Resultado:
asdas


## 3. Bibliografía <a name="id6"></a>

[1] (https://neuropsychology.github.io/NeuroKit/)

[2] N. Nazmi et al., “A Review of Classification Techniques of EMG Signals during Isotonic and Isometric Contractions,” Sensors, vol. 16, no. 8, p. 1304, 2016. [En línea]. Disponible en: https://doi.org/10.3390/s16081304

[3] M. B. I. Raez, M. S. Hussain y F. Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications,” Biological Procedures Online, vol. 8, pp. 11–35, 2006. [En línea]. Disponible en: https://doi.org/10.1251/bpo115

[4] NeuroKit2 Documentation, “EMG Signal Processing,” [En línea]. Disponible en: https://neurokit2.readthedocs.io/en/latest/functions/emg.html

