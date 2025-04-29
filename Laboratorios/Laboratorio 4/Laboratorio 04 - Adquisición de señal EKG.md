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
#### 4.1.1. Señal Cruda <a name="411-señal-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_cruda_1der_reposo.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_cruda_2der_reposo.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_cruda_3der_reposo.png" width="800" height="400"> |


#### 4.1.2. Señal Filtrada <a name="412-señal-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_1der_reposo.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_signal_filtered_2der_reposo.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_3der_reposo.png" width="800" height="400"> |

#### 4.1.3. FFT Cruda <a name="413-fft-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_1der_reposo.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_cruda_2der_reposo.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_3der_reposo.png" width="800" height="400"> |

#### 4.1.4. FFT Filtrada <a name="414-fft-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_1der_reposo.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_filtered_2der_reposo.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_3der_reposo.png" width="800" height="400"> |

#### 4.1.5. Función ecg_process() <a name="415-función-ecg_process"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_procesada_1der_reposo.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_procesada_2der_reposo.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_procesada_3der_reposo.png" width="800" height="400"> |

### 4.2. Señales procesadas - Respiración controlada <a name="id42"></a>
#### 4.2.1. Señal Cruda <a name="416-señal-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_cruda_1der_resp.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_cruda_2der_resp.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_cruda_3der_resp.png" width="800" height="400"> |

#### 4.2.2. Señal Filtrada <a name="417-señal-filtrada-respiración"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_1der_resp.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_signal_filtered_2der_resp.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_3der_resp.png" width="800" height="400"> |

#### 4.2.3. FFT Cruda <a name="418-fft-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_1der_resp.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_cruda_2der_resp.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_3der_resp.png" width="800" height="400"> |

#### 4.2.4. FFT Filtrada <a name="419-fft-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_1der_resp.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_filtered_2der_resp.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_3der_resp.png" width="800" height="400"> |

#### 4.2.5. Función ecg_process() <a name="420-función-ecg_process"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_procesada_1der_resp.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_procesada_2der_resp.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_procesada_3der_resp.png" width="800" height="400"> |

### 4.3. Señales procesadas - Inhalación larga <a name="id43"></a>
#### 4.3.1. Señal Cruda <a name="431-señal-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_cruda_1der_inha.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_cruda_2der_inha.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_cruda_3der_inha.png" width="800" height="400"> |

#### 4.3.2. Señal Filtrada <a name="432-señal-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_1der_inha.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_signal_filtered_2der_inha.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_3der_inha.png" width="800" height="400"> |

#### 4.3.3. FFT <a name="433-fft-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_1der_inha.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_cruda_2der_inha.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_3der_inha.png" width="800" height="400"> |

#### 4.3.4. FFT Filtrada <a name="434-fft-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_1der_inha.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_filtered_2der_inha.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_3der_inha.png" width="800" height="400"> |

#### 4.3.5. Función ecg_process() <a name="435-función-ecg_process"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_procesada_1der_inha.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_procesada_2der_inha.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_procesada_3der_inha.png" width="800" height="400"> |

### 4.4. Señales procesadas - Ejercicio físico <a name="id44"></a>
#### 4.4.1. Señal Cruda <a name="441-señal-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_cruda_1der_ejercicio.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_cruda_2der_ejercicio.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_cruda_3der_ejercicio.png" width="800" height="400"> |

#### 4.4.2. Señal Filtrada <a name="442-señal-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_1der_ejercicio.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_signal_filtered_2der_ejercicio.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_signal_filtered_3der_ejercicio.png" width="800" height="400"> |

#### 4.4.3. FFT <a name="443-fft-cruda"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_1der_ejercicio.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_cruda_2der_ejercicio.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_cruda_3der_ejercicio.png" width="800" height="400"> |

#### 4.4.4. FFT Filtrada <a name="444-fft-filtrada"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_1der_ejercicio.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_fft_filtered_2der_ejercicio.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_fft_filtered_3der_ejercicio.png" width="800" height="400"> |

#### 4.4.5. Función ecg_process() <a name="445-función-ecg_process"></a>

| Derivada | Gráfica generada |
|:---------|:-----------------|
| 1ra Derivada | <img src="./ImagesL4/ecg_procesada_1der_ejercicio.png" width="800" height="400"> |
| 2da Derivada | <img src="./ImagesL4/ecg_procesada_2der_ejercicio.png" width="800" height="400"> |
| 3ra Derivada | <img src="./ImagesL4/ecg_procesada_3der_ejercicio.png" width="800" height="400"> |


## 5. Discusiones y limitaciones <a name="id5"></a>

La discusión de resultados se realizó de manera detallada para la primera derivada.
### Discusiones
#### Estado en reposo: 
- En la [**Señal cruda**](#411-señal-cruda), se observa un ECG con amplitud y periodicidad características de una condición basal. A pesar del ruido de fondo visible, la morfología principal de los complejos QRS se mantiene identificable para la primera derivada. El componente de interferencia de red a 50-60 Hz es evidente en el espectro.

- La [**Señal filtrada**](#412-señal-filtrada) mejora significativamente la relación señal-ruido. El filtro pasa banda (0.5–40 Hz) aplicado permitió eliminar ruido de alta frecuencia y artefactos de baja frecuencia. Los complejos QRS aparecen más definidos para la primera derivada, y la línea base se estabiliza, lo cual es crítico para análisis de intervalos y amplitudes.

- En el [**Espectro de Frecuencia – FFT Cruda**](#413-fft-cruda), destaca un pico marcado alrededor de 50–60 Hz, típico de la interferencia de red eléctrica. Este pico decrece notablemente tras la filtración, como se muestra en la [**FFT Filtrada**](#414-fft-filtrada), validando la efectividad del preprocesamiento.

- El procesamiento usando `neurokit2.ecg_process()` ([**Función ecg_process()**](#415-función-ecg_process)) permitió detectar de manera automática los R-peaks y calcular la frecuencia cardíaca (HR). Se observa una frecuencia cardíaca estable en reposo (~80 bpm), con ligeras variaciones fisiológicas normales.

- En el caso de las señales filtradas para la [**segunda y tercera derivada en reposo**](#412-señal-filtrada), los complejos QRS se destacan claramente como picos profundos y agudos. El análisis del espectro de frecuencia y procesamiento usando ecg_process() es similar al obtenido de la primera derivada.

#### Respiración controlada:
Durante la fase de respiración controlada, las señales ECG mostraron variaciones respecto a las observadas en reposo.

- Al aplicar el filtrado [**Señal filtrada**](#417-señal-filtrada-respiración), las ondas QRS se mantienen claras y definidas, mientras que la modulación de baja frecuencia producida por el movimiento respiratorio es atenuada, validando la eficiencia del filtro pasa banda (0.5–40 Hz).

- En la [**FFT Cruda**](#418-fft-cruda), aparece un pico característico alrededor de 0.2–0.3 Hz, correspondiente a la frecuencia de la respiración (~12–18 respiraciones por minuto). Este pico desaparece o disminuye notablemente en la [**FFT Filtrada**](#419-fft-filtrada).

- El análisis de [**ecg_process()**](#420-función-ecg_process) muestra que la frecuencia cardíaca mantiene estabilidad, aunque presenta mayor variabilidad rítmica (HRV) comparado al reposo.

Este fenómeno observado es consistente con la respuesta fisiológica conocida como **sinus arrhythmia respiratoria**, donde la frecuencia cardíaca varía en sincronía con la fase de inspiración y expiración. [5].

#### Inhalación larga:
El análisis de las señales durante la condición de inhalación larga muestra patrones fisiológicos característicos de la interacción cardiorrespiratoria.

- En la [**Señal cruda**](#431-señal-cruda), se observa una variabilidad importante en la amplitud de la señal ECG.

- Después del filtrado ([**Señal filtrada**](#432-señal-filtrada)), la morfología de los complejos QRS se mantiene clara, y se evidencia una mejor definición de los intervalos PR y QT. Las oscilaciones lentas inducidas por la respiración son atenuadas eficazmente.

- El análisis espectral ([**FFT Cruda**](#433-fft-cruda)) muestra un desplazamiento de la energía hacia bajas frecuencias, con un pico alrededor de 0.2 Hz, indicando el efecto de la respiración controlada sobre la señal.

- Con la aplicación del filtrado ([**FFT Filtrada**](#434-fft-filtrada)), se preservan las componentes fisiológicas importantes para el ECG mientras se reduce el ruido respiratorio residual.

- Finalmente, el procesamiento automático con [**ecg_process()**](#435-función-ecg_process) revela que la frecuencia cardíaca presenta una **variabilidad marcada** durante la inhalación prolongada, bajando y subiendo de forma sincronizada con el patrón respiratorio.

Estos hallazgos confirman que maniobras respiratorias voluntarias de gran amplitud afectan significativamente la dinámica de la frecuencia cardíaca, fenómeno conocido como **sinus arrhythmia respiratoria** [5].

#### Ejercicio físico:
Durante el análisis de las señales ECG obtenidas durante ejercicio físico moderado, se observaron variaciones significativas respecto al estado de reposo.

- En la [**Señal cruda**](#441-señal-cruda), se identifica un aumento de artefactos de movimiento y ruido muscular (EMG) superpuesto al ECG. Esto se manifiesta en un aumento de la variabilidad de la amplitud y distorsión en los ciclos cardíacos.

- El filtrado ([**Señal filtrada**](#442-señal-filtrada)) permite atenuar considerablemente el ruido de alta frecuencia, aunque algunas deformaciones en la morfología del complejo QRS persisten.

- Tras el filtrado ([**FFT Filtrada**](#444-fft-filtrada)), la concentración de energía vuelve a enfocarse en las frecuencias fisiológicas relevantes (<40 Hz), aunque con cierta dispersión residual.

- El procesamiento automático con [**ecg_process()**](#445-función-ecg_process) revela un aumento de la frecuencia cardíaca promedio y mayor variabilidad en los intervalos RR, lo que es fisiológicamente consistente con la respuesta simpática al ejercicio. [6]


### Limitaciones y recomendaciones a futuro

Durante la adquisición de señales electrocardiográficas (ECG) de tres derivaciones, se identificaron algunas limitaciones técnicas relevantes:

- **Ruido eléctrico ambiental:**  
Una limitación frecuente fue la presencia de ruido inducido por la proximidad de dispositivos electrónicos como laptops, cargadores o iluminación fluorescente [7]. Este tipo de interferencia se refleja claramente como picos o distorsiones de alta frecuencia en el espectro de la [**FFT Cruda**](#443-fft-cruda) y [**FFT Cruda Reposo**](#413-fft).  
🔵 *Mejora sugerida:* Mantener distancia de fuentes de ruido y aplicar filtros digitales adecuados en la etapa de preprocesamiento [8].

- **Adherencia imperfecta de electrodos:**  
Aunque se realizó limpieza previa de la piel con alcohol, factores como el sudor o pequeños desplazamientos afectaron la calidad del contacto, generando artefactos de movimiento visibles [9] como oscilaciones abruptas en la [**Señal cruda de Inhalación**](#431-señal-cruda).  
🔵 *Mejora sugerida:* Utilizar electrodos de alta adherencia y reforzar la fijación periódicamente durante la prueba [10].

- **Tensión mecánica en cables:**  
Movimientos o tensiones en los cables de conexión provocaron desplazamientos de los electrodos, incrementando el ruido. Estos artefactos se evidencian como variaciones irregulares de amplitud [7], especialmente durante [**Ejercicio**](#441-señal-cruda).  
🔵 *Mejora sugerida:* Asegurar los cables al cuerpo o a superficies fijas mediante sujetadores específicos para evitar tracción directa sobre los electrodos [11].

---

Estas limitaciones, si bien comunes en estudios con adquisición ambulatoria, pueden ser mitigadas con estrategias de prevención y una preparación adecuada del entorno y del sujeto. La calidad de los registros mejoraría notablemente, permitiendo análisis más precisos y confiables.



## 6. Conclusiones <a name="id6"></a>

- El procesamiento de señales ECG adquiridas en reposo permite obtener una señal clara, con morfología típica de los complejos P-QRS-T, luego de un filtrado adecuado.

- La interferencia de 50–60 Hz proveniente del entorno eléctrico es importante y debe ser corregida, como se evidenció en el paso de la [FFT Cruda](#413-fft-cruda) a la [FFT Filtrada](#414-fft-filtrada).

- El preprocesamiento realizado, basado en filtrado pasa banda y análisis espectral, facilita la identificación de eventos cardiacos (R-peaks) necesarios para cálculos posteriores como HRV (variabilidad de frecuencia cardíaca).

- El uso de herramientas automáticas como `neurokit2` agiliza la segmentación y análisis de la señal, proporcionando tanto métricas como visualizaciones útiles.

- La respiración controlada introduce variaciones de baja frecuencia que afectan principalmente la línea base del ECG crudo, pero que son corregidas eficazmente con técnicas de filtrado.

- La modulación respiratoria de la frecuencia cardíaca es detectable y constituye un indicador de la interacción entre los sistemas cardiovascular y respiratorio.

- Las herramientas aplicadas permiten no solo aislar la señal de interés (latidos) sino también observar fenómenos fisiológicos adicionales como la variabilidad de la frecuencia cardíaca (HRV).

- La inhalación profunda y sostenida genera modulaciones visibles tanto en la amplitud como en la frecuencia de la señal ECG.

- El filtrado pasa banda aplicado (0.5–40 Hz) es efectivo para preservar la integridad del ECG a pesar de los artefactos respiratorios.

- La presencia de picos en bajas frecuencias en la FFT de la señal cruda valida la influencia directa de la respiración sobre la señal eléctrica cardíaca.
  
- La actividad física genera un incremento considerable en la frecuencia cardíaca, así como en el nivel de ruido y artefactos en la señal ECG.

- La aplicación de filtrado pasa banda (0.5–40 Hz) permite recuperar en gran medida la morfología del ECG, aunque el movimiento extremo puede seguir afectando la calidad de la señal.

- La dispersión espectral observada en el dominio de la frecuencia refuerza la necesidad de métodos robustos de adquisición y procesamiento de señales en condiciones dinámicas.

- El análisis de ECG bajo ejercicio es crucial para evaluar la respuesta autonómica, el acondicionamiento físico y potenciales disfunciones cardíacas inducidas por estrés físico.

## 7. Actividad adicional

Realizamos el ploteo las señales ECG obtenidas para la primera derivada usando la libreria ECG plot. [12]
El código utilizado se encuentra en la misma carpeta que este documento.

#### ECG Plot primera derivada

| Estado | Gráfica generada |
|:---------|:-----------------|
| Reposo | <img src="./ImagesL4/ecg_plot_reposo.png" width="800" height="400"> |
| Respiración controlada | <img src="./ImagesL4/ecg_plot_resp.png" width="800" height="400"> |
| Inhalación larga | <img src="./ImagesL4/ecg_plot_inha.png" width="800" height="400"> |
| Ejercicio | <img src="./ImagesL4/ecg_plot_ejercicio.png" width="800" height="400"> |

## Bibliografía
[1] “Papel del Electrocardiograma y sus Características - Cerebromedico”. Cerebromedico. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://cerebromedico.com/electrocardiograma/papel-ekg

[2] “Estimating Cardiac Axis”. Discover Clinical Medicine - MedSchool. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://medschool.co/tests/ecg-basics/estimating-cardiac-axis

[3] “The Basics of ECG”. ACLS Medical Training. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://www.aclsmedicaltraining.com/basics-of-ecg/

[4] “BITalino”. PLUX Biosignals. Accedido el 26 de abril de 2025. [En línea]. Disponible: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOopxPuL4rizGon-RlE3KPmQOCbfBI1UOzH1FhKijinshBj1K7VCj

[5] Yasuma F, Hayano J-I. Respiratory sinus arrhythmia: why does the heartbeat synchronize with respiratory rhythm? Chest [Internet]. 2004;125(2):683–90. Disponible en: http://dx.doi.org/10.1378/chest.125.2.683

[6] Sone R, Yamazaki F, Fujii N, Fukuoka Y, Ikegami H. Respiratory variability in R-R interval during sinusoidal exercise. Eur J Appl Physiol Occup Physiol [Internet]. 1997;75(1):39–46. Disponible en: http://dx.doi.org/10.1007/s004210050124

[7] Lee J, Park H, Kim H. Development of a MATLAB toolbox for automated ECG signal quality assessment. Sci Rep. 2024;14(1):3752. Available from: https://www.sciencedirect.com/science/article/pii/S235271102400270X

[8] Zhang Y, Liu Y, Wu Z. Sustainability and predictive accuracy of gel-based and embroidered electrodes for ECG signal acquisition. Sci Rep. 2024;14(1):4961. Available from: https://www.sciencedirect.com/science/article/pii/S1746809424006906

[9] Liu S, Zhang T, Luo X. Electromechanical artifact in ECG from limb electrodes: Implications for the detection of arrhythmias. Sci Rep. 2024;14(1):5076. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC7677642/

[10] Wu Y, Chen M, Li Y. Real-time ECG signal artifact elimination using open-source digital filters. Sci Rep. 2024;14(1):4885. Available from: https://www.sciencedirect.com/science/article/pii/S2772415824000130

[11} Zhang X, Tang Z, Liang J. Automated algorithm for eliminating noisy beats and improving ECG signal purity. Sci Rep. 2024;14(1):4150. Available from: https://pmc.ncbi.nlm.nih.gov/articles/PMC9234687/

[12] Ecg-plot [Internet]. PyPI. [citado el 29 de abril de 2025]. Disponible en: https://pypi.org/project/ecg-plot/







