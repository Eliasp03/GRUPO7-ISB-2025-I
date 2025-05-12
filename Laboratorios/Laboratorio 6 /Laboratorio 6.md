# Laboratorio 06 - Filtros Digitales
## Contenido
1. [Introducción](#id1)
2. [Materiales y equipos](#id2)
3. [Metodología](#id3)<br>
  3.1. [Señal ECG](#id4)<br>
  3.2. [Señal EMG](#id5)<br>
  3.3. [Señal EEG](#id6)<br>
4. [Discusiones](#id7)
5. [Referencias](#id7)

## 1. Introducción <a name="id1"></a>

Las señales biomédicas, tales como el electrocardiograma (ECG), el electromiograma (EMG) y el electroencefalograma (EEG), desempeñan un papel esencial en el diagnóstico clínico. Sin embargo, estas señales suelen estar contaminadas por ruidos y artefactos que dificultan su interpretación. Por ejemplo, el ECG es susceptible a interferencias de la red eléctrica (50/60 Hz) y al movimiento del paciente; el EMG puede afectarse por señales musculares adicionales y artefactos de movimiento; y el EEG, por su parte, presenta distorsiones generadas por parpadeos u otras señales eléctricas y musculares. Ante esta situación, resulta necesario implementar técnicas de procesamiento digital para mejorar la calidad de estas señales. En este contexto, los filtros digitales juegan un papel crucial, siendo los más utilizados los filtros FIR (Finite Impulse Response) e IIR (Infinite Impulse Response), debido a que permiten eliminar el ruido sin alterar las características fisiológicas relevantes de las señales. En consecuencia, se logra una interpretación clínica más precisa y confiable [1], [2].

Por otro lado, el diseño de filtros digitales depende en gran medida de las características espectrales de cada señal biomédica. Por ejemplo, el ECG tiene un rango útil entre 0.05 y 100 Hz, por lo que se emplean filtros pasa bajos, pasa altos y notch para eliminar ruidos específicos como el zumbido de la red eléctrica o los movimientos corporales. En cambio, el EMG presenta componentes útiles entre 20 y 500 Hz, por lo que se prefieren filtros pasa banda que supriman las frecuencias no deseadas. Asimismo, el EEG requiere especial atención, ya que sus señales de interés se sitúan por debajo de los 100 Hz y están organizadas en bandas específicas (delta, theta, alfa, beta y gamma). Por ende, se deben diseñar filtros que no alteren estas bandas. En términos técnicos, los filtros FIR suelen diseñarse mediante técnicas como el método de ventanas o el algoritmo de Parks-McClellan. Por su parte, los filtros IIR, que destacan por su eficiencia computacional, se obtienen transformando funciones analógicas como Butterworth o Chebyshev mediante la transformación bilineal [3], [4], [1].


## 2. Materiales y equipos <a name="id2"></a>

- Laptop con pyfda
- Python 3.12
- Librerías: `neurokit2`, `matplotlib`, `scipy`, `numpy`

## 3. Metodología <a name="id3"></a>

Para el procesamiento de señales ECG, se diseñó un filtro digital IIR del tipo elíptico mediante la herramienta PyFDA, seleccionando una estructura bandpass con orden 6. Este orden fue elegido como compromiso entre una buena respuesta en frecuencia y estabilidad del filtro, ya que valores superiores (como N=8) generaban efectos de resonancia y distorsión. La frecuencia de muestreo fue fijada en 1000 Hz, lo que permitió definir las especificaciones del filtro en función de fracciones de f_S. Se establecieron los bordes de la banda de paso en 0.5 Hz (F_PB = 0.0005 kHz) y 40 Hz (F_PB2 = 0.04 kHz), frecuencias típicas para preservar el contenido fisiológico útil del ECG. Las bandas de rechazo se colocaron en 0.2 Hz y 50 Hz para eliminar componentes de muy baja frecuencia (deriva de línea base) y ruido de red. Además, se fijó una atenuación mínima de 60 dB en las bandas de rechazo (A_SB) y un rizado de 2 dB en la banda de paso (A_PB). Esta configuración garantiza una señal filtrada estable, con supresión adecuada del ruido, sin pérdida de los componentes clínicamente relevantes.

### 3.1. Señal ECG <a name="id4"></a>

| 1era derivada | Señal Cruda | Filtro IIR Elliptic | Filtro IIR Butterworth |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal1der.png) | ![](./imagesL6/ecg_señal_filtrada_basal1der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_basal1der_butt.png) |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp1der.png) | ![](./imagesL6/ecg_señal_filtrada_resp1der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_basal1der_butt.png) |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer1der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer1der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_ejer1der_butt.png) |


| 1era derivada | Señal Cruda | Filtro FIR Hamming | Filtro FIR Blackman |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal1der.png) | ![](./imagesL6/ecg_señal_filtrada_reposo1der_fir_hamming.png) | ![](./imagesL6/ecg_señal_filtrada_reposo1der_fir_black.png) |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp1der.png) | ![](./imagesL6/ecg_señal_filtrada_resp1der_fir_hamming.png)  | ![](./imagesL6/ecg_señal_filtrada_resp1der_fir_black.png) |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer1der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer1der_fir_hamming.png)  | ![](./imagesL6/ecg_señal_filtrada_ejer1der_fir_black.png) |


| 2da derivada | Señal Cruda | Filtro IIR Elliptic | Filtro IIR Butterworth |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal2der.png) | ![](./imagesL6/ecg_señal_filtrada_basal2der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_basal2der_butt.png) |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp2der.png) | ![](./imagesL6/ecg_señal_filtrada_resp2der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_resp2der_butt.png) |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer2der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer2der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_ejer2der_butt.png) |


| 2da derivada | Señal Cruda | Filtro FIR Hamming | Filtro FIR Blackman |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal2der.png) | ![](./imagesL6/ecg_señal_filtrada_reposo2der_fir_hamming.png) | ![](./imagesL6/ecg_señal_filtrada_reposo2der_fir_black.png)  |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp2der.png) | ![](./imagesL6/ecg_señal_filtrada_resp2der_fir_hamming.png)  | ![](./imagesL6/ecg_señal_filtrada_resp2der_fir_black.png)  |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer2der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer2der_fir_hamming.png) | ![](./imagesL6/ecg_señal_filtrada_ejer2der_fir_black.png) |


| 3era derivada | Señal Cruda | Filtro IIR Elliptic | Filtro IIR Butterworth |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal3der.png) | ![](./imagesL6/ecg_señal_filtrada_basal3der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_basal3der_butt.png) |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp3der.png) | ![](./imagesL6/ecg_señal_filtrada_resp3der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_basal3der_butt.png) |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer3der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer3der_eliptic.png) | ![](./imagesL6/ecg_señal_filtrada_ejer3der_butt.png) |


| 3era derivada | Señal Cruda | Filtro FIR Hamming | Filtro FIR Blackman |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Basal         | ![](./imagesL6/ecg_señal_cruda_basal1der.png) | ![](./imagesL6/ecg_señal_filtrada_reposo3der_fir_hamming.png) | ![](./imagesL6/ecg_señal_filtrada_reposo3der_fir_black.png)  |
| Respiración   | ![](./imagesL6/ecg_señal_cruda_resp1der.png) | ![](./imagesL6/ecg_señal_filtrada_resp2der_fir_hamming.png)  | ![](./imagesL6/ecg_señal_filtrada_resp3der_fir_black.png)  |
| Post-Ejercicio| ![](./imagesL6/ecg_señal_cruda_ejer1der.png) | ![](./imagesL6/ecg_señal_filtrada_ejer3der_fir_hamming.png) | ![](./imagesL6/ecg_señal_filtrada_ejer3der_fir_black.png) |



### 3.2. Señal EMG <a name="id5"></a>

Especificaciones: 
- Filtro IIR:  Tipo Eliptico y Butterworth. Fc = 60 Hz, Wp = 188 rad/s, Ws = 300 rad/s (elimina frecuencias altas que correspondan a ruido eléctrico y artefactos de movimiento).
- Filtro FIR: Tipo Hamming y Blackman. Fc = 40 Hz, paso banda bajo

| Campo | Señal Cruda | Filtro IIR Elliptic | Filtro IIR Butterworth |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Reposo Biceps        | ![](./imagesL6/emg_señal_cruda_reposobiceps.png) | ![](./imagesL6/emg_señal_filtrada_reposobiceps_elliptic.png) | ![](./imagesL6/emg_señal_filtrada_reposobiceps_butt.png) |
| Leve Biceps | ![](./imagesL6/emg_señal_cruda_levebiceps.png) | ![](./imagesL6/emg_señal_filtrada_levebiceps_elliptic.png) | ![](./imagesL6/emg_señal_filtrada_levebiceps_butt.png) |
| Maximo Biceps| ![](./imagesL6/emg_señal_cruda_maxbiceps.png) | ![](./imagesL6/emg_señal_filtrada_maxbiceps_elliptic.png) | ![](./imagesL6/emg_señal_filtrada_maxbiceps_butt.png) |

| Campo | Señal Cruda | Filtro FIR Hamming | Filtro FIR Blackman |
|:-------------:|:------------:|:-------------------:|:----------------------:|
| Reposo Biceps        | ![](./imagesL6/emg_señal_cruda_reposobiceps.png) | ![](./imagesL6/emg_señal_filtrada_reposobiceps_fir_hamming.png) | ![](./imagesL6/emg_señal_filtrada_reposobiceps_fir_black.png) |
| Leve Biceps | ![](./imagesL6/emg_señal_cruda_levebiceps.png) | ![](./imagesL6/emg_señal_filtrada_levebiceps_fir_hamming.png) | ![](./imagesL6/emg_señal_filtrada_levebiceps_fir_black.png) |
| Maximo Biceps| ![](./imagesL6/emg_señal_cruda_maxbiceps.png) | ![](./imagesL6/emg_señal_filtrada_maxbiceps_fir_hamming.png) | ![](./imagesL6/emg_señal_filtrada_maxbiceps_fir_black.png) |

## 3.3. Señal EEG <a name="id6"></a>

Especificaciones: 
- Filtro IIR:  Tipo Eliptico. Pasabajos Fc = 30 Hz, Wp = 94 rad/s, Ws = 157 rad/s (suprimir la interferencia de frecuencia alta y artefactos).
- Filtro FIR: Tipo Hanning. Fc = 12 Hz, paso banda para ondas alfa.

| Campo | Señal Cruda | Filtro IIR | Filtro FIR |
|:---------|:-----------------|:---------|:-----------------|
| Basal |  |
| Parpadeo |  |
| Lectura |  |

## 7. Discusiones <a name="id7"></a>

Dado que el filtro IIR diseñado posee una ganancia distinta de 1, la señal resultante mantiene su forma morfológica pero con una escala menor en amplitud. Este comportamiento es esperado al aplicar coeficientes exportados sin normalización automática. Para propósitos de visualización se recomienda reescalar la salida.

### ECG
1. Rango de frecuencias en ECG:

0.5 Hz a 40 Hz como banda de paso corresponde al estándar para monitoreo clínico, donde se prioriza la eliminación de artefactos por movimiento (0.2-2 Hz) y ruido muscular (5-50 Hz).

Para diagnóstico detallado se recomiendan rangos más amplios (0.01-250 Hz), pero su elección es adecuada si el objetivo es monitoreo continuo.

2. Frecuencia de muestreo:

Los 1000 Hz seleccionados superan el mínimo de Nyquist (≥2×f_max) para 150 Hz y coinciden con requerimientos para análisis de onda P y variabilidad cardíaca.

3. Bordes de rechazo:

0.2 Hz elimina deriva de línea base (<0.5 Hz)

50 Hz atenúa ruido de red (60 Hz en América, 50 Hz en Europa). Recomendaría ajustar a 55-70 Hz si el entorno usa 60 Hz.

4. Atenuación de 60 dB:

Supera los 40 dB recomendados para supresión de ruido muscular y ruido de red.

Fundamentos en normas:

- La AHA recomienda 0.05-150 Hz para diagnóstico, pero con frecuencias de corte ajustables.

- El estándar ANSI/AAMI EC11 sugiere 0.67-40 Hz para dispositivos de monitoreo

## 8. Referencias <a name="id8"></a>

[1] J. Ochoa, D. Andres, "Diseño e implementación de filtros digitales FIR e IIR utilizando el microcontrolador XMEGA de Atmel para tratamiento de señales de audio", Universidad Politécnica Salesiana, 2016. Disponible: [https://dspace.ups.edu.ec/handle/123456789/13087](https://dspace.ups.edu.ec/handle/123456789/13087).

[2] Juan's Audio, "IIR vs FIR: Entendiendo realmente sus diferencias", 2020. Disponible: [https://www.juansaudio.com/post/iir-vs-fir-entendiendo-realmente-sus-diferencias](https://www.juansaudio.com/post/iir-vs-fir-entendiendo-realmente-sus-diferencias)

[3] H. H., A. K., K. A.-h., "Optimized FIR Filter Using Genetic Algorithms: A Case Study of ECG Signals Filter Optimization", MDPI, vol. 3, no. 4, pp. 71, 2023. Available in: https://www.mdpi.com/2673-7426/3/4/71

[4] Song et al., "Arrhythmia Classification for Non-Experts Using IIR Filter-Based Machine Learning and Deep Learning Models of the Electrocardiogram", PeerJ, 2020. Available in: https://peerj.com/articles/cs-1774/

[5] C. Vidal, V. Gatica, "Diseño e implementación de un sistema electrocardiográfico digital", Disponible en: http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0120-62302010000500010.

[6] Ingeniería, Investigación y Desarrollo, "Reducción de interferencias en señales ECG mediante filtros digitales IIR", Disponible en: https://revistas.uptc.edu.co/index.php/ingenieria_sogamoso/article/view/858/857.

[7] Jove, "Adquisición y análisis de una señal de ECG (electrocardiografía)", Disponible en: https://www.jove.com/v/10473/acquisition-and-analysis-of-an-ecg-electrocardiography-signal?language=Spanish.
