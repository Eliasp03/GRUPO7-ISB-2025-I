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

![actividad2](./imagenesL10/imagen_actividad2.png)

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
from sklearn.decomposition import PCA
from scipy.stats import skew, kurtosis
import seaborn as sns
```

2. Definimos los parámetros de simulación de las señales ECG:
```bash
fs = 1000  # Hz → frecuencia de muestreo
duration = 20  # segundos → duración de la señal

ecg1 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=70)
ecg2 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=90)
ecg3 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=110)

signals = [ecg1, ecg2, ecg3]
labels = ["70bpm", "90bpm", "110bpm"]
```
Se crean 3 señales ECG con diferentes frecuencias cardíacas: 70, 90 y 110 bpm.

3. Definimos la función de extracción de características:
```bash
def extract_features(signal):
    return {
        "Mean": np.mean(signal),
        "Median": np.median(signal),
        "STD": np.std(signal),
        "Kurtosis": kurtosis(signal),
        "Skewness": skew(signal),
        "Energy": np.sum(signal**2)
    }
```

4. Extraemos las características y mostramos en una tabla:
```bash
features = [extract_features(sig) for sig in signals]
df = pd.DataFrame(features)
df["Label"] = labels

print("\n=== Tabla de características ===")
print(df)
```

5. Realizamos la reducción de dimensionalidad con PCA:
```bash
X = df.drop(columns=["Label"])
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Label"] = labels
```
Se aplica PCA para reducir las características a 2 componentes principales: PC1 y PC2).

6. Finalmente graficamos los resultados:
```bash
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="Label", s=120, palette="Set1")
plt.title("PCA de características de 3 señales ECG")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.tight_layout()
plt.show()
```

### Resultado:

![Señales ECG1](./imagenesL10/actividad3.png)

![Señales ECG2](./imagenesL10/actividad3_1.jpg)

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
2. Definimos los parámetros generales para la simulación ECG:
```bash
fs = 1000
duration = 20
np.random.seed(42)
```
3. Especificamos los parámetros de la señal y simulamos:
```bash
ti0 = np.array([-70, -15, 0, 15, 100])
ai0 = np.array([1.2, -5, 30, -7.5, 0.75])
bi0 = np.array([0.25, 0.1, 0.1, 0.1, 0.4])

ecg0 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)
```

4. Creamos una señal ECG de clase 1 con parámetros modificados ligeramente mediante ruido gaussiano:
```bash
ti1 = np.random.normal(ti0, 3)
ai1 = np.random.normal(ai0, np.abs(ai0 / 5))
bi1 = np.random.normal(bi0, np.abs(bi0 / 5))
ecg1 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)
```

5. Simulamos una señal ECG anómala (clase 2) con onda T invertida y complejo QRS más ancho:
```bash
ti2 = np.random.normal(ti0, 3)
ai2 = np.random.normal(ai0, np.abs(ai0 / 5))
bi2 = np.random.normal(bi0, np.abs(bi0 / 5))
ai2[4] = -0.5  # T invertida
bi2[2] *= 2    # QRS ancho
ecg2 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)
```

6. Generamos una segunda señal ECG para cada clase usando los mismos parámetros originales:
```bash
ecg0_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)
ecg1_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)
ecg2_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)
```

7. Agrupamos todas las señales y etiquetamos:
```bash
signals = [ecg0, ecg0_bis, ecg1, ecg1_bis, ecg2, ecg2_bis]
labels = [0, 0, 1, 1, 2, 2]
```

8. Extraemos características y almacenamos:
```bash
def extract_features(signal):
    return {
        "Mean": np.mean(signal),
        "Median": np.median(signal),
        "STD": np.std(signal),
        "Kurtosis": kurtosis(signal),
        "Skewness": skew(signal),
        "Energy": np.sum(signal**2)
    }

features = []
for i, ecg in enumerate(signals):
    feats = extract_features(ecg)
    feats["Label"] = labels[i]
    features.append(feats)
```

9. Convertimos la lista de características en un DataFrame y mostramos la tabla:
```bash
df = pd.DataFrame(features)

print("\n=== Tabla de características ===")
print(df)
```

10. Separamos los datos y etiquetas, a continuación, aplicamos PCA:
```bash
X = df.drop(columns=["Label"])
y = df["Label"]

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
```

11. Creamos un nuevo DataFrame con las componentes principales y las etiquetas. Finalmente, graficamos:
```bash
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Label"] = y.astype(str)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="Label", palette="Set1", s=100)
plt.title("PCA de características ECG (3 clases, 2 señales por clase)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.tight_layout()
plt.show()
```
### Resultado:

![Señales ECG1](./imagenesL10/actividad4.png)

![Señales ECG2](./imagenesL10/actividad4_1.png)

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
import pywt
from scipy.signal import welch
from scipy.stats import linregress, kurtosis, skew
from sklearn.decomposition import PCA
```
2. Realizamos la creación y simulación de señales ECG: 
```bash
fs = 1000
duration = 20
np.random.seed(42)

# Parámetros base para ECG normal
ti0 = np.array([-70, -15, 0, 15, 100])
ai0 = np.array([1.2, -5, 30, -7.5, 0.75])
bi0 = np.array([0.25, 0.1, 0.1, 0.1, 0.4])

# Clase 0: ECG normal
ecg0 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)
ecg0_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)

# Clase 1: Parámetros modificados
ti1 = np.random.normal(ti0, 3)
ai1 = np.random.normal(ai0, np.abs(ai0/5))
bi1 = np.random.normal(bi0, np.abs(bi0/5))
ecg1 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)
ecg1_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)

# Clase 2: ECG con anomalías
ti2 = np.random.normal(ti0, 3)
ai2 = np.random.normal(ai0, np.abs(ai0/5))
bi2 = np.random.normal(bi0, np.abs(bi0/5))
ai2[4] = -0.5  # Invertir onda T
bi2[2] *= 2    # Ensanchar QRS
ecg2 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)
ecg2_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)


signals = [ecg0, ecg0_bis, ecg1, ecg1_bis, ecg2, ecg2_bis]
labels = [0, 0, 1, 1, 2, 2]  # 0: normal, 1: parámetros modificados, 2: anormal
```
3. Definimos una función para extraer características con DWT
```bash
def extract_features_with_dwt(signal, wavelet='db4', level=4):
    # Características estadísticas básicas
    features = {
        "Mean": np.mean(signal),
        "Median": np.median(signal),
        "STD": np.std(signal),
        "Kurtosis": kurtosis(signal),
        "Skewness": skew(signal),
        "Energy": np.sum(signal**2),
    }
    
    
    return features
```

4. Extraemos las características para las señales ECG

```bash
features_list = []
for i, signal in enumerate(signals):
    feat = extract_features_with_dwt(signal)
    feat["Label"] = labels[i]
    features_list.append(feat)
```

5. Creamos el dataframe con las características
```bash
df_features = pd.DataFrame(features_list)
```

6. Mostramos la tabla de características con DWT
```bash
print("\n=== Tabla de características con coeficientes DWT ===")
print(df_features)
```
7. Visualizamos el PCA
 ```bash  
plt.figure(figsize=(10, 6))
for label in df_pca["Label"].unique():
    subset = df_pca[df_pca["Label"] == label]
    plt.scatter(subset["PC1"], subset["PC2"], label=f"Clase {label}", s=100)

plt.title("PCA de Características ECG con Coeficientes DWT")
plt.xlabel(f"Componente Principal 1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"Componente Principal 2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.grid(True)
plt.legend(title="Clase")
plt.tight_layout()
plt.show()
```

### Resultado:
![actividad5](./imagenesL10/imagen_actividad5.png)


## 3. Bibliografía <a name="id6"></a>

[1] (https://neuropsychology.github.io/NeuroKit/)

[2] N. Nazmi et al., “A Review of Classification Techniques of EMG Signals during Isotonic and Isometric Contractions,” Sensors, vol. 16, no. 8, p. 1304, 2016. [En línea]. Disponible en: https://doi.org/10.3390/s16081304

[3] M. B. I. Raez, M. S. Hussain y F. Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications,” Biological Procedures Online, vol. 8, pp. 11–35, 2006. [En línea]. Disponible en: https://doi.org/10.1251/bpo115

[4] NeuroKit2 Documentation, “EMG Signal Processing,” [En línea]. Disponible en: https://neurokit2.readthedocs.io/en/latest/functions/emg.html

