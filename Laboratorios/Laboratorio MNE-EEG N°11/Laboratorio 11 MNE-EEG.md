# Laboratorio 11 - MNE-EEG
## Contenido
1. [Origen de los datos](#id1)
2. [Procedimiento de preprocesamiento](#id2)
3. [Extracción de características](#id3)
4. [Optimización y selección](#id4)


## 1. Origen de los datos <a name="id1"></a>

### Objetivo: 
- Detallar recolección con Ultracortex (frecuencia de muestreo, nro. de electrodos) o la base de datos usada (nombre, URL).

### Desarrollo:
Los datos utilizados provienen de la base de datos **EEG Motor Movement/Imagery Dataset**, disponible públicamente en PhysioNet, con las siguientes características:
- **Frecuencia de muestreo**: 160 Hz
- **Número de canales/electrodos**: 64
- **Montaje**: Sistema internacional 10-10 (excepto Nz, F9, F10, FT9, FT10, A1, A2, TP9, TP10, P9 y P10)
- **Formato**: EDF+ (European Data Format Plus)
- **Descripción**:
  - Se recopilaron registros EEG de 109 voluntarios mientras realizaban (o imaginaban) movimientos motores específicos (manos, pies) en diferentes condiciones experimentales.
  - Cada sujeto completó 14 sesiones experimentales, que incluyeron:
    - Tareas en reposo con ojos abiertos/cerrados
    - Movimientos reales e imaginados de manos y pies, en respuesta a estímulos visuales en pantalla.
  - Las anotaciones T0, T1 y T2 indican respectivamente: reposo, movimiento de mano izquierda/brazos, o pie derecho/piernas (dependiendo de la tarea).
- Fuente: Schalk, G., McFarland, D.J., Hinterberger, T., Birbaumer, N., Wolpaw, J.R. BCI2000: A General-Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering 51(6):1034-1043, 2004. https://www.physionet.org/content/eegmmidb/1.0.0/

## 2. Procedimiento de preprocesamiento <a name="id2"></a>

### Objetivo: 
- Limpiar las señales de EEG mediante técnicas de filtrado (por ejemplo, filtros pasa-banda, notch y wavelet), eliminar artefactos (blink, EMG, ECG) y normalizar/alinear las señales para hacerlas comparables entre sesiones y sujetos.

### Desarrollo:
El preprocesamiento se realizó utilizando **MNE-Python** y consistió en los siguientes pasos:

- **Lectura del archivo**: Se utilizaron los archivos `S001R01.edf` a `S001R10.edf`, correspondientes a tareas motoras reales e imaginadas del sujeto S001 de la base de datos PhysioNet EEG Motor Movement/Imagery Dataset.
- **Montaje**: Se aplicó el sistema estándar **10-20** con la función `set_montage('standard_1020')` para ubicar correctamente los electrodos.
- **Filtro pasa banda**: Se aplicó un filtro entre **1 y 40 Hz** para eliminar componentes de baja frecuencia (artefactos de movimiento y deriva DC) y alta frecuencia (ruido muscular o eléctrico).
- **Filtro notch**: Se utilizó un filtro a **60 Hz** para suprimir la interferencia de la red eléctrica.
- **Interpolación de canales**: No se detectaron canales ruidosos en esta muestra específica, por lo que `raw.info['bads'] = []`. En caso de detección visual, se podrían interpolar automáticamente con `interpolate_bads()`.
- **Eliminación de artefactos**: Se utilizó **Análisis de Componentes Independientes (ICA)** con 20 componentes (`n_components=20`). Se eliminaron manualmente los componentes relacionados con artefactos de parpadeo (ej. componente 0), identificados con `ica.plot_components()`.
- **Herramientas**: MNE-Python, matplotlib, numpy

#### Archivos EDF descargados – Sujeto S001
Se utilizó el código python adjuntado 'señal_cruda.py' para graficar cada uno de los archivos detallados a continuación:

| Archivo       | Descripción                                                  | Señal cruda                          | PSD                                  |
|---------------|--------------------------------------------------------------|---------------------------------------|---------------------------------------|
| S001R01.edf   | Baseline – ojos abiertos                                     | ![](L11_images/eeg_crudo01.png)     | ![](L11_images/psd_crudo01.png)     |
| S001R02.edf   | Baseline – ojos cerrados                                     | ![](L11_images/eeg_crudo02.png)     | ![](L11_images/psd_crudo02.png)     |
| S001R03.edf   | Tarea 1 – Movimiento real, mano izquierda o derecha          | ![](L11_images/eeg_crudo03.png)     | ![](L11_images/psd_crudo03.png)     |
| S001R04.edf   | Tarea 2 – Movimiento imaginado, mano izquierda o derecha     | ![](L11_images/eeg_crudo04.png)     | ![](L11_images/psd_crudo04.png)     |
| S001R05.edf   | Tarea 3 – Movimiento real, ambas manos o ambos pies          | ![](L11_images/eeg_crudo05.png)     | ![](L11_images/psd_crudo05.png)     |
| S001R06.edf   | Tarea 4 – Movimiento imaginado, ambas manos o ambos pies     | ![](L11_images/eeg_crudo06.png)     | ![](L11_images/psd_crudo06.png)     |
| S001R07.edf   | Repetición de Tarea 1 (real – manos)                         | ![](L11_images/eeg_crudo07.png)     | ![](L11_images/psd_crudo07.png)     |
| S001R08.edf   | Repetición de Tarea 2 (imaginada – manos)                    | ![](L11_images/eeg_crudo08.png)     | ![](L11_images/psd_crudo08.png)     |
| S001R09.edf   | Repetición de Tarea 3 (real – manos/pies)                    | ![](L11_images/eeg_crudo09.png)     | ![](L11_images/psd_crudo09.png)     |
| S001R10.edf   | Repetición de Tarea 4 (imaginada – manos/pies)              | ![](L11_images/eeg_crudo10.png)     | ![](L11_images/psd_crudo10.png)     |


## 3. Extracción de características <a name="id3"></a>

### Objetivo: 
- Aplicar técnicas de feature engineering sobre las componentes extraídas (estadísticas, bandas, transformaciones) para mejorar la calidad de los datos antes de alimentar modelos de clasificación.

| Archivo      | Delta (nV²) | Theta (nV²) | Alpha (nV²) | Beta (nV²) |
|--------------|-------------|-------------|-------------|------------|
| S001R01.edf  | 0.882       | 0.211       | 0.147       | 0.159      |
| S001R02.edf  | 0.763       | 0.211       | 0.754       | 0.241      |
| S001R03.edf  | 1.273       | 0.254       | 0.147       | 0.193      |
| S001R04.edf  | 1.367       | 0.271       | 0.137       | 0.175      |
| S001R05.edf  | 1.397       | 0.261       | 0.128       | 0.184      |
| S001R06.edf  | 0.885       | 0.198       | 0.177       | 0.156      |
| S001R07.edf  | 1.467       | 0.226       | 0.164       | 0.186      |
| S001R08.edf  | 0.764       | 0.170       | 0.149       | 0.165      |
| S001R09.edf  | 1.345       | 0.233       | 0.154       | 0.187      |
| S001R10.edf  | 1.193       | 0.226       | 0.164       | 0.175      |


## 4. Optimización y selección <a name="id4"></a>

### Objetivo: 
- Integrar y analizar los datos a través de observaciones temporales, frecuenciales y espaciales empleando MNE-Python (Epochs, Evoked, montage, interpolate_bads).
