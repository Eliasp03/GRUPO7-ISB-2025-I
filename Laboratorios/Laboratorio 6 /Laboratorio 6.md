# Laboratorio 07 - Filtros Digitales
## Contenido
1. [Introducción](#id1)
2. [Propósito de la práctica](#id2)
3. [Materiales y equipos](#id3)
4. [Señal ECG](#id4)
5. [Señal EMG](#id5)
6. [Señal EEG](#id6)

## 1. Introducción <a name="id1"></a>

En el procesamiento de señales biomédicas como ECG, EMG y EEG, es común encontrar ruido y artefactos que pueden dificultar el análisis. Por eso, se usan filtros digitales para mejorar la calidad de estas señales. Los filtros IIR (Respuesta Infinita al Impulso) utilizan retroalimentación, lo que les permite ser eficientes y parecidos a los filtros analógicos tradicionales, aunque pueden generar distorsión de fase [1]. Por otro lado, los filtros FIR (Respuesta Finita al Impulso) no usan retroalimentación y su salida depende solo de las entradas actuales, lo que les da una respuesta de fase lineal y mayor estabilidad, aunque suelen requerir más cálculos. En este laboratorio, se diseñarán y compararán filtros IIR y FIR aplicados a señales ECG, EMG y EEG para observar cómo afectan la eliminación de ruido y la preservación de las características importantes de cada señal [2].


## 3. Materiales y equipos <a name="id3"></a>
| Equipo/Material     |Cantidad   |
|-----------   |:------------:
|BITalino (r)evolution Board Kit BLE/BT[4]  |1          |
|Laptop           |1          |
|Electrodos ECG   |3          |

<img src="" width="500" height="300"/>

## 3. Señal ECG <a name="id4"></a>


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




