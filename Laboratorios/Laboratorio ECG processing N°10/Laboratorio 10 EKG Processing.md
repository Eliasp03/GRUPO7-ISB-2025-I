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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
2. Definimos las escalas de amplitud para el músculo izquierdo (20% a 100%) y una lista vacía ratios para almacenar los resultados del Symmetry Ratio.
```bash
escalas = [0.2, 0.4, 0.6, 0.8, 1.0]
ratios = []
```

### Resultado:

![Señales EMG](./L9-images/comparacion-actividad1.png)

## 2. Actividad 2 <a name="id2"></a>

### Objetivo: 
- Para cada señal simulada, extraer las características básicas

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

[1] P. Konrad, The ABC of EMG: A Practical Introduction to Kinesiological Electromyography, Noraxon Inc., 2005. [En línea]. Disponible en: https://hermanwallace.com/download/The_ABC_of_EMG_by_Peter_Konrad.pdf

[2] N. Nazmi et al., “A Review of Classification Techniques of EMG Signals during Isotonic and Isometric Contractions,” Sensors, vol. 16, no. 8, p. 1304, 2016. [En línea]. Disponible en: https://doi.org/10.3390/s16081304

[3] M. B. I. Raez, M. S. Hussain y F. Mohd-Yasin, “Techniques of EMG signal analysis: detection, processing, classification and applications,” Biological Procedures Online, vol. 8, pp. 11–35, 2006. [En línea]. Disponible en: https://doi.org/10.1251/bpo115

[4] NeuroKit2 Documentation, “EMG Signal Processing,” [En línea]. Disponible en: https://neurokit2.readthedocs.io/en/latest/functions/emg.html

