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
El preprocesamiento se realizó utilizando MNE-Python y consistió en los siguientes pasos:

- **Lectura del archivo**: S001R04.edf (ejemplo de la base de datos PhysioNet)
- **Montaje**: Se aplicó el sistema estándar 10-20
- **Filtro pasa banda**: entre 1 y 40 Hz para eliminar componentes de baja y alta frecuencia irrelevantes
- **Filtro notch**: a 60 Hz para eliminar interferencias de la red eléctrica
- **Interpolación de canales**: no se identificaron canales malos en esta muestra (o se interpolaron Fp1 y Fp2, etc.)
- **Eliminación de artefactos**: se utilizó Independent Component Analysis (ICA) con 20 componentes. Se eliminaron los componentes relacionados con parpadeo (ej. componente 0).
- **Herramientas**: MNE-Python (versión x.x), matplotlib, numpy

#### Archivos EDF descargados – Sujeto S001

| Archivo           | Descripción                                                  |
|-------------------|--------------------------------------------------------------|
| S001R01.edf       | Baseline – ojos abiertos                                     |
| S001R01.edf.event | Eventos correspondientes a R01                               |
| S001R02.edf       | Baseline – ojos cerrados                                     |
| S001R02.edf.event | Eventos correspondientes a R02                               |
| S001R03.edf       | Tarea 1 – Movimiento real, mano izquierda o derecha          |
| S001R03.edf.event | Eventos correspondientes a R03                               |
| S001R04.edf       | Tarea 2 – Movimiento imaginado, mano izquierda o derecha     |
| S001R04.edf.event | Eventos correspondientes a R04                               |
| S001R05.edf       | Tarea 3 – Movimiento real, ambas manos o ambos pies          |
| S001R05.edf.event | Eventos correspondientes a R05                               |
| S001R06.edf       | Tarea 4 – Movimiento imaginado, ambas manos o ambos pies     |
| S001R06.edf.event | Eventos correspondientes a R06                               |
| S001R07.edf       | Repetición de Tarea 1 (real – manos)                         |
| S001R07.edf.event | Eventos correspondientes a R07                               |
| S001R08.edf       | Repetición de Tarea 2 (imaginada – manos)                    |
| S001R08.edf.event | Eventos correspondientes a R08                               |
| S001R09.edf       | Repetición de Tarea 3 (real – manos/pies)                    |
| S001R09.edf.event | Eventos correspondientes a R09                               |
| S001R10.edf       | Repetición de Tarea 4 (imaginada – manos/pies)               |


## 3. Extracción de características <a name="id3"></a>

### Objetivo: 
- Aplicar técnicas de feature engineering sobre las componentes extraídas (estadísticas, bandas, transformaciones) para mejorar la calidad de los datos antes de alimentar modelos de clasificación.

## 4. Optimización y selección <a name="id4"></a>

### Objetivo: 
- Integrar y analizar los datos a través de observaciones temporales, frecuenciales y espaciales empleando MNE-Python (Epochs, Evoked, montage, interpolate_bads).
