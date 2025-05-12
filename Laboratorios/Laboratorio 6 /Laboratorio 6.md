# Laboratorio 07 - Filtros Digitales
## Contenido
1. [Introducción](#id1)
2. [Materiales y equipos](#id2)
3. [Metodología](#id3)
  3.1. [Señal ECG](#id4)
  3.2. [Señal EMG](#id5)
  3.3. [Señal EEG](#id6)
4. [Discusiones](#id7)
5. [Referencias](#id7)

## 1. Introducción <a name="id1"></a>

Las señales biomédicas, tales como el electrocardiograma (ECG), el electromiograma (EMG) y el electroencefalograma (EEG), desempeñan un papel esencial en el diagnóstico clínico. Sin embargo, estas señales suelen estar contaminadas por ruidos y artefactos que dificultan su interpretación. Por ejemplo, el ECG es susceptible a interferencias de la red eléctrica (50/60 Hz) y al movimiento del paciente; el EMG puede afectarse por señales musculares adicionales y artefactos de movimiento; y el EEG, por su parte, presenta distorsiones generadas por parpadeos u otras señales eléctricas y musculares. Ante esta situación, resulta necesario implementar técnicas de procesamiento digital para mejorar la calidad de estas señales. En este contexto, los filtros digitales juegan un papel crucial, siendo los más utilizados los filtros FIR (Finite Impulse Response) e IIR (Infinite Impulse Response), debido a que permiten eliminar el ruido sin alterar las características fisiológicas relevantes de las señales. En consecuencia, se logra una interpretación clínica más precisa y confiable [1], [2].

Por otro lado, el diseño de filtros digitales depende en gran medida de las características espectrales de cada señal biomédica. Por ejemplo, el ECG tiene un rango útil entre 0.05 y 100 Hz, por lo que se emplean filtros pasa bajos, pasa altos y notch para eliminar ruidos específicos como el zumbido de la red eléctrica o los movimientos corporales. En cambio, el EMG presenta componentes útiles entre 20 y 500 Hz, por lo que se prefieren filtros pasa banda que supriman las frecuencias no deseadas. Asimismo, el EEG requiere especial atención, ya que sus señales de interés se sitúan por debajo de los 100 Hz y están organizadas en bandas específicas (delta, theta, alfa, beta y gamma). Por ende, se deben diseñar filtros que no alteren estas bandas. En términos técnicos, los filtros FIR suelen diseñarse mediante técnicas como el método de ventanas o el algoritmo de Parks-McClellan. Por su parte, los filtros IIR, que destacan por su eficiencia computacional, se obtienen transformando funciones analógicas como Butterworth o Chebyshev mediante la transformación bilineal [3], [4], [1].


## 3. Materiales y equipos <a name="id3"></a>

- Laptop con pyfda
- Python 3.12
- Librerías: `neurokit2`, `matplotlib`, `scipy`, `numpy`

## 4. Señal ECG <a name="id4"></a>


| Campo | Señal Cruda | Filtro IIR | Filtro FIR |
|:---------|:-----------------|:---------|:-----------------|
| Basal | <img src="./ImagesL4/ecg_cruda_1der_reposo.png" width="800" height="400"> |
| Respiración | <img src="./ImagesL4/ecg_cruda_2der_reposo.png" width="800" height="400"> |
| Post-Ejercicio | <img src="./ImagesL4/ecg_cruda_3der_reposo.png" width="800" height="400"> |



## 5. Señal EMG <a name="id5"></a>

| Campo | Señal Cruda | Filtro IIR (1) | Filtro IIR (2) | Filtro FIR (1) | Filtro FIR(2) |
|:---------|:-----------------|:---------|:-----------------|:---------|:-----------------|
| Descanso |  |
| Contracción leve |  |
| Contracción fuerte |  |

## 6. Señal EEG <a name="id6"></a>

| Campo | Señal Cruda | Filtro IIR | Filtro FIR |
|:---------|:-----------------|:---------|:-----------------|
| Basal |  |
| Parpadeo |  |
| Lectura |  |

## 7. Referencias <a name="id7"></a>

[1] J. Ochoa, D. Andres, "Diseño e implementación de filtros digitales FIR e IIR utilizando el microcontrolador XMEGA de Atmel para tratamiento de señales de audio", Universidad Politécnica Salesiana, 2016. Disponible: [https://dspace.ups.edu.ec/handle/123456789/13087](https://dspace.ups.edu.ec/handle/123456789/13087).

[2] Juan's Audio, "IIR vs FIR: Entendiendo realmente sus diferencias", 2020. Disponible: [https://www.juansaudio.com/post/iir-vs-fir-entendiendo-realmente-sus-diferencias](https://www.juansaudio.com/post/iir-vs-fir-entendiendo-realmente-sus-diferencias)

[3] H. H., A. K., K. A.-h., "Optimized FIR Filter Using Genetic Algorithms: A Case Study of ECG Signals Filter Optimization", MDPI, vol. 3, no. 4, pp. 71, 2023. Available in: https://www.mdpi.com/2673-7426/3/4/71

[4] Song et al., "Arrhythmia Classification for Non-Experts Using IIR Filter-Based Machine Learning and Deep Learning Models of the Electrocardiogram", PeerJ, 2020. Available in: https://peerj.com/articles/cs-1774/

