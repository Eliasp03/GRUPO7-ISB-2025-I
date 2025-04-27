# Laboratorio 04 - Adquisición de señal EKG
## Contenido
1. [Introducción](#id1)
2. [Propósito de la práctica](#id2)
3. [Materiales y equipos](#id3)
4. [Metodología y resultados](#id4)<br>
   4.1. [Señales procesadas - Reposo](#id41)<br>
   4.2. [Señales procesadas - Respiración controlada](#id42)<br>
   4.3. [Señales procesadas - Inhalación larga](#id43)<br>
   4.4. [Señales procesadas - Ejercicio físico](#id44)<br>
   4.5. [Detalles del procesamiento](#id45)<br>
5. [Discusiones y limitaciones](#id5)
6. [Conclusiones](#id6)

## 1. Introducción <a name="id1"></a>
<p style="text-align: justify;">     
El electrocardiograma (ECG o EKG) es un procedimiento médico no invasivo e indoloro, ampliamente utilizado para apoyar el diagnóstico de enfermedades cardíacas, como insuficiencia cardíaca, hipertrofias, infartos y cuadros benignos, entre otros. Proporciona información esencial sobre la frecuencia cardíaca, el ritmo y patrones eléctricos asociados a patologías [1].
  
<p style="text-align: justify;">  
El registro del ECG se realiza mediante electrodos colocados en extremidades y tórax, captando la actividad eléctrica del corazón. Un ECG estándar incluye 6 derivaciones primarias (de extremidades) y 6 derivaciones precordiales, que registran diferencias de potencial entre electrodos (bipolares) o entre un punto virtual y un electrodo (monopolares) [2].

  <img src="https://www.cuidandote.net/articulos/ECG/ecg03.jpg" width="500" height="300"/>

<p style="text-align: justify;">  
La despolarización cardíaca se refleja en el ECG como deflexiones: una onda que se acerca a un electrodo genera una deflexión positiva (ascendente), mientras que una que se aleja produce una deflexión negativa (descendente). La amplitud de estas ondas se mide en milímetros (mm), y su análisis permite evaluar la dirección general del impulso eléctrico, conocido como eje cardíaco [2].

  <img src="https://cerebromedico.com/wp-content/uploads/2017/12/Papel-del-electrocardiograma.png" width="500" height="200"/>

<p style="text-align: justify;"> 
Las ondas básicas del ECG incluyen:

- Onda P: Corresponde a la despolarización atrial, con una duración ≤0.11 segundos y altura ≤2.5 mm.

- Complejo QRS: Representa la despolarización ventricular, con una duración normal de 0.06-0.10 segundos.

- Onda T: Indica la repolarización ventricular y su dirección suele coincidir con el QRS. Alteraciones en su morfología sugieren patologías [3].
<img src="https://cerebromedico.com/wp-content/uploads/2017/12/electrocardiograma-conduccion-electrica-del-corazon.gif" width="500" height="300"/>

</p>

## 2. Propósito de la práctica <a name="id2"></a>
<p style="text-align: justify;">   
El propósito de este proceso consiste en comprender el funcionamiento del dispositivo BITalino y definir la disposición adecuada de los electrodos para la captura de señales biomédicas. Posteriormente, se busca adquirir registros electrocardiográficos (ECG), tal que las señales recopiladas serán procesadas y visualizadas en tiempo real a través del software OpenSignals. Adicionalmente, se configura el BITalino de manera correcta para asegurar la calidad de las mediciones. Finalmente, se realiza la exportación de los datos brutos de las señales ECG con el fin de facilitar su procesamiento.
</p>

## 3. Materiales y equipos <a name="id3"></a>
| Material     |Cantidad   |
|-----------   |:------------:
|Kit BITalino[4]  |1          |
|Laptop           |1          |
|Electrodos ECG   |3          |

<img src="https://www.pluxbiosignals.com/cdn/shop/products/BITalino-Board.1.jpg" width="500" height="300"/>

## 3. Metodología y resultados <a name="id4"></a>

Se adquirieron señales ECG reales usando el sistema BITalino en diferentes condiciones:

- Ejercicio físico (movimiento)
- Reposo (tranquilo)
- Inhalación prolongada
- Respiración controlada

Para cada condición y cada derivada, se aplicó:

- Lectura de la señal cruda
- Procesamiento con NeuroKit2 (`ecg_process`)
- Análisis en el dominio del tiempo (visualización)
- Análisis en el dominio de la frecuencia (FFT)
- Aplicación de filtro pasa banda (0.5–40 Hz)
- Cálculo de FFT sobre la señal filtrada

<p align="center"><strong>Adquisición de la señal</strong></p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=tEmNLL7wylE&list=PL0yjbUQfs0HJIlzI2OXYC5avDCqxtay_i&index=1" target="_blank">
    <img src="ImagesL4/Youtube_logo.png" width="15%">
  </a>
</p>

### 🔧 Detalles del procesamiento <a name="id45"></a>

- **Filtro** aplicado: pasa banda 0.5–40 Hz, orden 4.
- **Transformada rápida de Fourier (FFT)** con 1024 puntos.
- **Segmento de visualización (zoom):** de 5 a 10 segundos.
- **Software usado:** Python 3.12, NeuroKit2, Matplotlib, OpenSignalsReader.

### 4.1. Señales procesadas - Reposo <a name="id41"></a>
#### 4.1.1. Señal Cruda

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_cruda_1der_ejercicio.png" width="600"> |
| 2da Derivada | <img src="./ImagesL4/ecg_cruda_2der_ejercicio.png" width="600"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_cruda_3der_ejercicio.png" width="600"> |


#### 4.1.2. Señal Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_signal_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_signal_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_signal_filtered_3der_ejercicio.png` |

#### 4.1.3. FFT

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_cruda_3der_ejercicio.png` |

#### 4.1.4. FFT Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_filtered_3der_ejercicio.png` |

#### 4.1.5. Función ecg_process()

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_procesada_1der_ejercicio.png` |
| 2da Derivada | `ecg_procesada_2der_ejercicio.png` |
| 3ra Derivada | `ecg_procesada_3der_ejercicio.png` |

### 4.2. Señales procesadas - Respiración controlada <a name="id42"></a>
#### 4.2.1. Señal Cruda

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_cruda_3der_ejercicio.png` |

#### 4.2.2. Señal Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_signal_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_signal_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_signal_filtered_3der_ejercicio.png` |

#### 4.2.3. FFT

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_cruda_3der_ejercicio.png` |

#### 4.2.4. FFT Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_filtered_3der_ejercicio.png` |

#### 4.2.5. Función ecg_process()

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_procesada_1der_ejercicio.png` |
| 2da Derivada | `ecg_procesada_2der_ejercicio.png` |
| 3ra Derivada | `ecg_procesada_3der_ejercicio.png` |

### 4.3. Señales procesadas - Inhalación larga <a name="id43"></a>
#### 4.3.1. Señal Cruda

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_cruda_3der_ejercicio.png` |

#### 4.3.2. Señal Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_signal_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_signal_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_signal_filtered_3der_ejercicio.png` |

#### 4.3.3. FFT

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_cruda_3der_ejercicio.png` |

#### 4.3.4. FFT Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_filtered_3der_ejercicio.png` |

#### 4.3.5. Función ecg_process()

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_procesada_1der_ejercicio.png` |
| 2da Derivada | `ecg_procesada_2der_ejercicio.png` |
| 3ra Derivada | `ecg_procesada_3der_ejercicio.png` |

### 4.4. Señales procesadas - Ejercicio físico <a name="id44"></a>
#### 4.4.1. Señal Cruda

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_cruda_3der_ejercicio.png` |

#### 4.4.2. Señal Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_signal_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_signal_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_signal_filtered_3der_ejercicio.png` |

#### 4.4.3. FFT

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_cruda_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_cruda_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_cruda_3der_ejercicio.png` |

#### 4.4.4. FFT Filtrada

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_fft_filtered_1der_ejercicio.png` |
| 2da Derivada | `ecg_fft_filtered_2der_ejercicio.png` |
| 3ra Derivada | `ecg_fft_filtered_3der_ejercicio.png` |

#### 4.4.5. Función ecg_process()

| Derivada | Gráfica generada |
|:---------|:-------------------|
| 1ra Derivada | `ecg_procesada_1der_ejercicio.png` |
| 2da Derivada | `ecg_procesada_2der_ejercicio.png` |
| 3ra Derivada | `ecg_procesada_3der_ejercicio.png` |


## 5. Discusiones y limitaciones <a name="id5"></a>


# Limitaciones

Durante la adquisición de señales electrocardiográficas (ECG) con tres derivaciones, una limitación frecuente fue la presencia de ruido eléctrico ambiental. La cercanía de dispositivos electrónicos como laptops o cargadores puede introducir interferencias en la señal, afectando la nitidez del registro [a]. Para reducir este problema, se recomienda mantener distancia de fuentes de ruido y emplear filtros digitales adecuados [b].

Aunque se realizó una limpieza previa de la piel con alcohol, la adherencia de los electrodos puede verse afectada por factores como el sudor o pequeños movimientos durante la prueba, generando artefactos en la señal [c]. Para optimizar el registro, es aconsejable revisar periódicamente la fijación de los electrodos y utilizar parches de alta adherencia [d].

Finalmente, la tensión mecánica en los cables representa otra fuente de inestabilidad. Si los cables se tensan o mueven, pueden provocar desplazamientos de los electrodos y aumentar el ruido de la señal [1]. Se recomienda sujetar los cables de forma segura sobre una superficie fija o utilizar sujetadores específicos para minimizar este problema [e].



## 6. Conclusiones <a name="id6"></a>

## Bibliografía
[1] “Papel del Electrocardiograma y sus Características - Cerebromedico”. Cerebromedico. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://cerebromedico.com/electrocardiograma/papel-ekg

[2] “Estimating Cardiac Axis”. Discover Clinical Medicine - MedSchool. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://medschool.co/tests/ecg-basics/estimating-cardiac-axis

[3] “The Basics of ECG”. ACLS Medical Training. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://www.aclsmedicaltraining.com/basics-of-ecg/

[4] “BITalino”. PLUX Biosignals. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOopxPuL4rizGon-RlE3KPmQOCbfBI1UOzH1FhKijinshBj1K7VCj
