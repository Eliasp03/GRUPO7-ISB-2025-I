# Laboratorio 3

## Introducción (fundamentos)

El BITalino es un sistema desarrollado por PLUX Biosignals para la adquisición de bioseñales con fines educativos y de investigación. En esta actividad se utilizará su sensor de electromiografía (EMG) para medir de forma no invasiva la actividad eléctrica muscular. La señal será registrada con el software OpenSignals y luego analizada usando Python.

<div align="center">
<img src="ImagesL3/material2.jpeg" width="45%">
<img src="ImagesL3/material3.jpeg" width="41.6%">
</div>

<p align="center"><i>Figura 1. Placa BiTalino (r)evolution</i><p>

## Propósito de la práctica

- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG del software OpenSignals (r)evolution

## Materiales

- BiTalino (r)evolution kit
- 3 electrodos de superficie
- Laptop con software Open Signals
- Python 3.12
- Librerías: `neurokit2`, `matplotlib`, `scipy`, `numpy`

Para la adquisición de la sñal EMG se empleará el cable de tres derivaciones (3-leads), compuesto por un electrodo positivo, uno negativo y uno de referencia.

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

<div align="center"><img src="ImagesL3/electrodos1.jpeg" width="15%">
<img src="ImagesL3/electrodos2.jpeg" width="15%">
<img src="ImagesL3/electrodos4.jpeg" width="15%"></div>
<p align="center"><i>Figura 3. Colocación de electrodos</i><p>

Inicialmente, se realizó una prueba preliminar para verificar que el dispositivo Bitalino y el software OpenSignals registraran adecuadamente la señal del usuario. Una vez confirmado, se procedió a realizar tres pruebas, cada una con tres grabaciones. En la primera prueba, se evaluó la señal EMG del bíceps en reposo; en la segunda prueba, se midió la contracción del bíceps; y, en la tercera prueba, se sometió al usuario a una carga externa para inducir un esfuerzo muscular adicional.

<div align="center">

| **Prueba 1** | **Prueba 2** | **Prueba 3** |
|:------------:|:------------:|:------------:|
| <img src="ImagesL3/brazo1.jpeg" width="150"> | <img src="ImagesL3/brazo2.jpeg" width="200"> | <img src="ImagesL3/brazo3.jpeg" width="200"> |

</div>
<p align="center"><i>Tabla 2. Pruebas realizadas en el bíceps braquial</i><p>

<p align="center"><a href="#"> <strong>Videos Bíceps Braquial</strong> </a></p>

[<img src="ImagesL3/Youtube_logo.png" width="15%">](https://www.youtube.com/playlist?list=PL0yjbUQfs0HI3KjGtao96HebQhwQrK4IF)

### EMG - Gastrocnemio 

...

<div align="center"><img src="ImagesL3/pierna1.jpeg" width="25%">
<img src="ImagesL3/pierna1.1.jpeg" width="15%"></div>
<p align="center"><i>Figura 4. Colocación de electrodos</i><p>

<div align="center">

| **Prueba 1** | **Prueba 2** | **Prueba 3** |
|:------------:|:------------:|:------------:|
| <img src="ImagesL3/pierna2.jpeg" width="45%"> | <img src="ImagesL3/pierna2.1.jpeg" width="45%"> | <img src="ImagesL3/pierna3.jpg" width="95%"> |

</div>


Videos Gastrocnemio

[<img src="ImagesL3/Youtube_logo.png" width="15%">](https://www.youtube.com/playlist?list=PL0yjbUQfs0HJbjQnfOTrr8QcOsbAQNYDM)

## Resultados y Limitaciones



## Referencias


