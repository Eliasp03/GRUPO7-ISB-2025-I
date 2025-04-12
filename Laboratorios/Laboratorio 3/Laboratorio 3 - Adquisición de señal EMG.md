# Laboratorio 3 Adquisición de señales EMG

## Introducción

El **BITalino (r)evolution** es un sistema modular desarrollado por *PLUX Wireless Biosignals* que permite la adquisición y análisis de bioseñales en tiempo real. Está diseñado para aplicaciones educativas, de investigación y prototipado en el campo de la Ingeniería Biomédica. Este dispositivo cuenta con sensores integrados para medir señales como electrocardiografía (ECG), electromiografía (EMG), actividad galvánica de la piel (EDA), entre otros, y se comunica de forma inalámbrica a través de Bluetooth [1].

En esta práctica se utilizará el sensor de **electromiografía (EMG)** incluido en el BITalino para medir la actividad eléctrica producida por los músculos esqueléticos. La señal será adquirida usando el software **OpenSignals (r)evolution**, procesada posteriormente con herramientas de análisis digital en Python, y analizada en los dominios del tiempo y la frecuencia para evaluar su comportamiento fisiológico y posibles artefactos. Este tipo de análisis es ampliamente utilizado en áreas como rehabilitación, biomecánica y control de prótesis. [2] [3]


## Propósito de la práctica

- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG del software OpenSignals (r)evolution

## Materiales y equipos

- BiTalino (r)evolution kit ( 1 cable de de 2 hilos; 1 cable de 3 hilos, 1 bateria, 1 guía de
inicio rápido, 1 BITalino).
- 3 electrodos de superficie
- Laptop con software Open Signals
- Python 3.12
- Librerías: `neurokit2`, `matplotlib`, `scipy`, `numpy`

En la adquisición de la sñal EMG se empleará el cable de tres derivaciones (3-leads), compuesto por un electrodo positivo, uno negativo y uno de referencia.
<div align="center">
<img src="ImagesL3/material2.jpeg" width="45%">
<img src="ImagesL3/material3.jpeg" width="41.6%">
</div>

<p align="center"><i>Figura 1. Placa BiTalino (r)evolution</i><p>
  
<div align="center">
<img src="ImagesL3/material5.jpeg" width="27.5%">
<img src="ImagesL3/material1.jpeg" width="15%"> 
<img src="ImagesL3/material4.jpeg" width="20%">
</div>


<p align="center"><i>Figura 2. Kit bitalino con cables de 2 y 3 derivaciones</i><p>

<div align="center"><img src="ImagesL3/Leads.jpg" width="60%"></div>
<p align="center"><i>Tabla 1. Significado de los colores [<a href="https://support.pluxbiosignals.com/wp-content/uploads/2021/11/electromyography-emg-user-manual.pdf">EMG BiTalino User Manual</a>]</i></p>

## Métodos  
### EMG - Bíceps Braquial

El primer músculo analizado fue el bíceps braquial. Previo a la colocación de los electrodos, se realizó una limpieza adecuada de la zona con el fin de asegurar una buena conductividad. Posteriormente, se colocaron los electrodos según lo indicado en la Figura 3: el electrodo positivo se ubicó en la parte proximal del músculo, el negativo en la parte distal, y el electrodo de referencia sobre una zona ósea adyacente, en este caso el codo.

<div align="center"><img src="ImagesL3/electrodos1.jpeg" width="20%">
<img src="ImagesL3/electrodos2.jpeg" width="20%">
<img src="ImagesL3/electrodos4.jpeg" width="20%"></div>
<p align="center"><i>Figura 3. Colocación de electrodos</i><p>

Inicialmente, se realizó una prueba preliminar para verificar que el dispositivo Bitalino y el software OpenSignals registraran adecuadamente la señal del usuario. Una vez confirmado, se procedió a realizar tres pruebas, cada una con tres grabaciones. En la primera prueba, se evaluó la señal EMG del bíceps en reposo; en la segunda prueba, se midió la contracción del bíceps; y, en la tercera prueba, se sometió al usuario a una carga externa para inducir un esfuerzo muscular adicional.

<div align="center">

| **Prueba 1** | **Prueba 2** | **Prueba 3** |
|:------------:|:------------:|:------------:|
| <img src="ImagesL3/brazo1.jpeg" width="150"> | <img src="ImagesL3/brazo2.jpeg" width="200"> | <img src="ImagesL3/brazo3.jpeg" width="200"> |

</div>
<p align="center"><i>Tabla 2. Pruebas realizadas en el bíceps braquial</i><p>

<p align="center"><strong>EMG - Bíceps Braquial</strong></p>

<p align="center">
  <a href="https://www.youtube.com/playlist?list=PL0yjbUQfs0HI3KjGtao96HebQhwQrK4IF">
    <img src="ImagesL3/Youtube_logo.png" width="15%">
  </a>
</p>

### EMG - Gastrocnemio 

El segundo músculo analizado fue el gastrocnemio. Se repitieron los mismos procedimientos, ubicando el electrodo positivo en la parte proximal del músculo, el negativo en la parte distal y el electrodo de referencia sobre la rodilla.

<div align="center"><img src="ImagesL3/pierna1.jpeg" width="25%">
<img src="ImagesL3/pierna1.1.jpeg" width="14%"></div>
<p align="center"><i>Figura 4. Colocación de electrodos</i><p>

Después de colocar los electrodos, se realizaron tres pruebas. En la primera, se registró la actividad del gastrocnemio en reposo. En la segunda, se captó la actividad muscular durante una ligera contracción del músculo. Finalmente, en la tercera prueba, el usuario se puso de pie e intentó levantarse de puntillas para generar más esfuerzo en el músculo.

<div align="center">

| **Prueba 1** | **Prueba 2** | **Prueba 3** |
|:------------:|:------------:|:------------:|
| <img src="ImagesL3/pierna2.jpeg" width="45%"> | <img src="ImagesL3/pierna2.1.jpeg" width="45%"> | <img src="ImagesL3/pierna3.jpg" width="95%"> |

</div>

<p align="center"><i>Tabla 3. Pruebas realizadas en el gastrocnemio</i><p>

<p align="center"><strong>EMG - Gastrocnemio</strong></p>

<p align="center">
  <a href="https://www.youtube.com/playlist?list=PL0yjbUQfs0HJbjQnfOTrr8QcOsbAQNYDM">
    <img src="ImagesL3/Youtube_logo.png" width="15%">
  </a>
</p>

## Resultados y Limitaciones



## Referencias
[1] PLUX Wireless Biosignals, "BITalino (r)evolution Board Kit," [Online]. Available: https://www.pluxbiosignals.com.

[2] De Luca, C.J. Electromyography.  Encyclopedia of Medical Devices and Instrumentation, (John G. Webster, Ed.), [Online]. Available: [https://www.delsys.com/knowledge-center/what-is-emg/.](https://delsys.com/downloads/TUTORIAL/emg-encyclopedia-of-medical-devices-and-instrumentation.pdf)

[3] J. Merletti and D. Farina, *Surface Electromyography: Physiology, Engineering, and Applications*. Wiley-IEEE Press, 2016.

