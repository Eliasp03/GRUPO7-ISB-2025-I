# Laboratorio 07 - Transformada Wavelet
## Contenido
1. [Introducción](#id1)
2. [Materiales y equipos](#id2)
3. [Metodología](#id3)<br>
4. [Resultados](#id4)<br>
  4.1. [Señal ECG](#id5)<br>
  4.2. [Señal EMG](#id6)<br>
  4.3. [Señal EEG](#id7)<br>
5. [Discusiones](#id8)
6. [Referencias](#id9)


## 1. Introducción <a name="id1"></a>

En la ingeniería biomédica, el análisis de señales como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) es fundamental para el diagnóstico clínico y la investigación. Estas señales son inherentemente no estacionarias y suelen estar contaminadas con ruido y artefactos, lo que dificulta su análisis directo [1][2]. Frente a este desafío, la Transformada Wavelet ha demostrado ser una herramienta matemática poderosa para el procesamiento y análisis multiresolución de señales biomédicas, permitiendo una representación simultánea en tiempo y frecuencia [3][4].

A diferencia de la Transformada de Fourier, que solo proporciona una visión global de las frecuencias presentes en una señal, la Transformada Wavelet permite detectar eventos transitorios y cambios abruptos al adaptar su resolución según la escala: alta resolución temporal para frecuencias altas y alta resolución frecuencial para frecuencias bajas [4][5]. Esta característica la hace ideal para capturar componentes importantes en señales clínicas, como los complejos QRS en ECG, artefactos en EMG o patrones anormales en EEG [3][4][6].

Existen dos implementaciones principales: la Transformada Wavelet Continua (CWT), que proporciona un análisis detallado pero computacionalmente costoso debido a su carácter redundante [7], y la Transformada Wavelet Discreta (DWT), que utiliza escalas y posiciones discretas, permitiendo una representación más eficiente y adecuada para procesamiento digital [8]. La DWT emplea filtros pasaaltos y pasabajos para dividir la señal en componentes de alta y baja frecuencia, facilitando su descomposición jerárquica en distintos niveles de resolución [1].

Además, existen múltiples familias de wavelets, como Haar, Daubechies, Symlets, Coiflets o Morlet, cada una con propiedades específicas que las hacen más adecuadas para diferentes tipos de señales y objetivos de análisis [8].

## 2. Materiales y equipos <a name="id9"></a>

## 3. Metodología <a name="id9"></a>

## 4. Resultados <a name="id9"></a>

## 5. Discusiones y Conclusiones <a name="id9"></a>

## 6. Referencias <a name="id9"></a>

[1] S. Kouro and R. Musalem, “Tutorial introductorio a la Teoría de Wavelet.” Available: http://www2.elo.utfsm.cl/~elo377/documentos/Wavelet.pdf.

[2] G. Antonio and L. Paredes, “Reconocimiento de patrones en electroforesis capilar utilizando análisis multiresolucional y programación dinámica / Gerardo Ceballos,” 2024. https://www.researchgate.net/publication/44720047_Reconocimiento_de_patrones_en_electroforesis_capilar_utilizando_analisis_multiresolucional_y_programacion_dinamica_Gerardo_Ceballos

[3] T. Sharma and K. K. Sharma, "QRS Complex Detection in ECG Signals Using the Synchrosqueezed Wavelet Transform," IETE Journal of Research, vol. 62, no. 6, pp. 885-892, Nov.-Dec. 2016, doi: 10.1080/03772063.2016.1221744.

[4] P. Zandiyeh, L. R. Parola, B. C. Fleming, and J. E. Beveridge, "Wavelet analysis reveals differential lower limb muscle activity patterns long after anterior cruciate ligament reconstruction," Journal of Biomechanics, vol. 133, p. 110957, 2022, doi: 10.1016/j.jbiomech.2022.110957.

[5] N. N. B and D. Marcela, “El uso de la transformada wavelet discreta en la reconstrucción de señales senosoidales.,” Scientia et Technica, vol. 1, no. 38, pp. 381–386, 2024, doi: https://dialnet.unirioja.es/descarga/articulo/4782789.pdf.‌‌

[6] S. Mallat, "Chapter 3 - Discrete Revolution," in A Wavelet Tour of Signal Processing, 3rd ed., San Diego, CA, USA: Academic Press, 2009, pp. 59-88, doi: 10.1016/B978-0-12-374370-1.00007-0.

[7] R. González G., "Capítulo 3: Revisión de la Teoría de Wavelets," Universidad de las Américas Puebla, Puebla, México. Disponible: https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf.

[8]  E. Pinto Moreno, "Familias de Wavelets," Universidad Carlos III de Madrid, Madrid, España. Disponible: https://e-archivo.uc3m.es/bitstream/10016/16582/1/PFC_Elena_Pinto_Moreno_Anexos.pdf. 
