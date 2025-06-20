# Laboratorio 12 - Avance del proyecto
## Contenido
1. [Origen de los datos](#id1)
2. [Procedimiento de preprocesamiento](#id2)
3. [Extracción de características](#id3)
   - [Características basadas en energía de bandas](#id4)
   - [Características basadas en Wavelet](#id5) 
5. [Optimización y selección](#id6)


## 1. Origen de los datos <a name="id1"></a>

### Objetivo: 
- Detallar la base de datos usada de Physionet(nombre, URL).

### Desarrollo:
Los datos utilizados provienen de la base de datos **EMG t**, disponible públicamente en PhysioNet, con las siguientes características:
- **Frecuencia de muestreo**: [X] Hz
- **Número de canales/electrodos**: X
- **Montaje**: 
- **Formato**: 
- **Descripción**:
  - Poner resumen:
  - Cada sujeto completó 14 sesiones experimentales, que incluyeron:
    - Tareas en reposo con ojos abiertos/cerrados
    - Movimientos reales pies.
- Fuente: Incluir fuente

## 2. Procedimiento de preprocesamiento <a name="id2"></a>

### Objetivo: 
- Limpiar las señales de EMG mediante técnicas de filtrado (por ejemplo, filtros pasa-banda, notch y wavelet), eliminar artefactos (blink, EMG, ECG) y normalizar/alinear las señales para hacerlas comparables entre sesiones y sujetos.

### Desarrollo de característica 1:
El preprocesamiento se realizó utilizando **MNE-Python** y consistió en los siguientes pasos:

- **Lectura del archivo**: Se utilizaron los archivos `S001R01.edf` a `S001R10.edf`, correspondientes a tareas motoras reales e imaginadas del sujeto S001 de la base de datos PhysioNet EEG Motor Movement/Imagery Dataset.
- **Montaje**: Se aplicó el sistema estándar **10-20** con la función `set_montage('standard_1020')` para ubicar correctamente los electrodos.
- **Filtro pasa banda**: Se aplicó un filtro entre **1 y 40 Hz** para eliminar componentes de baja frecuencia (artefactos de movimiento y deriva DC) y alta frecuencia (ruido muscular o eléctrico).
- **Filtro notch**: Se utilizó un filtro a **60 Hz** para suprimir la interferencia de la red eléctrica.
- **Interpolación de canales**: No se detectaron canales ruidosos en esta muestra específica, por lo que `raw.info['bads'] = []`. En caso de detección visual, se podrían interpolar automáticamente con `interpolate_bads()`.
- **Eliminación de artefactos**: Se utilizó **Análisis de Componentes Independientes (ICA)** con 20 componentes (`n_components=20`). Se eliminaron manualmente los componentes relacionados con artefactos de parpadeo (ej. componente 0), identificados con `ica.plot_components()`.
- **Herramientas**: MNE-Python, matplotlib, numpy


## 3. Extracción de características <a name="id3"></a>

### Objetivo: 
- Aplicar técnicas de feature engineering sobre las componentes extraídas (estadísticas, bandas, transformaciones) para mejorar la calidad de los datos antes de alimentar modelos de clasificación. (CAMBIAR A DETECCIÓN DE PATRONES DE FATIGA)

### Características basadas en energía de bandas: <a name="id4"></a>
Se utilizó el método de densidad espectral de potencia (PSD) mediante Welch (`raw.compute_psd`) aplicado sobre las señales preprocesadas. Posteriormente, se integró la PSD dentro de los rangos de frecuencia definidos para cada banda, y se calculó el promedio de energía por banda y archivo, todo el procedimiento realizado se encuentra en el archivo

Las bandas utilizadas fueron:

- **Delta:** 0.5 – 4 Hz  
- **Theta:** 4 – 8 Hz  
- **Alpha:** 8 – 13 Hz  
- **Beta:** 13 – 30 Hz

#### Tabla de energía promedio por banda (en µV²)


#### Visualización:


### Características basadas en Wavelet: <a name="id5"></a>
Se aplicó una transformada wavelet discreta (DWT) utilizando la función pywt.wavedec() de la librería PyWavelets, con los siguientes parámetros:
- **Wavelet utilizada:** Daubechies 4 ('db4')  
- **Niveles de descomposición:** 4 niveles
- **Señal de entrada:** canal promedio de cada archivo EEG preprocesado
- **Feature extraída:** varianza de los coeficientes en cada nivel (cA4, cD4, cD3, cD2, cD1), máximo (uV), mediana (uV) y desviación estándar (uV)
- **Herramientas**: MNE-Python, PyWavelets, numpy


#### Tabla de características varianzas de los coeficientes mediante DWT:


#### Tabla de características máximo (uV), mediana (uV) y desviación estándar (uV) de los coeficientes mediante DWT:

## 4. Optimización y selección <a name="id6"></a>

### Objetivo: 
- Integrar y analizar los datos a través de observaciones temporales, frecuenciales y espaciales empleando MNE-Python (Epochs, Evoked, montage, interpolate_bads).

### Desarrollo: 


#### a. Filtrado y eliminación de artefactos

```bash
ica = mne.preprocessing.ICA(n_components=15, random_state=97, max_iter='auto')
```

#### b. Visualización de la distribución espacial de los electrodos
```bash
fig_sensor = raw_ica.plot_sensors(show_names=True, show=False)
fig_sensor.savefig("L11_images/post_sensor_posiciones.png")
```

#### c. Segmentación en épocas (Epochs) y cálculo del promedio (Evoked)

```bash
events = mne.make_fixed_length_events(raw_ica, id=1, duration=2.)
```

#### d. Mapa topográfico del EEG

```bash
montage = make_standard_montage("standard_1020")
```

#### e. Reducción de dimensionalidad con PCA

```bash
# Visualización de PCA
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue')
plt.title("Proyección PCA de características")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.savefig("L11_images/post_pca_features.png")
plt.close()
```

