# Laboratorio 09 - EMG processing
## Contenido
1. [Ejercicio A](#id1)
2. [Ejercicio B](#id2)
3. [Referencias](#id3)


## 1. Ejercicio A: Simulación de distintos grados de asimetría <a name="id1"></a>
### Objetivo: Estudiar cómo varía el Symmetry Ratio al alterar la amplitud relativa del músculo “izquierdo”
### Implementar:
- Simular cinco pares de señales EMG idénticas (burst_number=10, noise=0.01) y escalar el segundo canal al 20 %, 40 %, 60 %, 80 % y 100 % de la amplitud original.
- Para cada par, limpiar con nk.emg_clean(), extraer la envolvente con nk.emg_amplitude() y calcular el Symmetry Ratio.
- Graficar en un único plot de barras el ratio obtenido frente al %% de escala utilizado.

### Desarrollo:

### Resultado:


### Pregunta de reflexión: ¿A partir de qué nivel de desbalance la simetría cae por debajo de un umbral “aceptable” (p.ej. 80 %)?
- sdsdssds


## 2. Ejercicio B: Índices de fatiga – pendiente de RMS vs. pendiente de frecuencia <a name="id2"></a>
### Objetivo: Comparar dos métricas clásicas de fatiga: la tasa de crecimiento de la amplitud (RMS) y la tasa de caída de la frecuencia mediana.
### Implementar:
- Simular una señal EMG de 30 s dividida en 3 segmentos de 10 s, siguiendo el patrón del ejercicio de fatiga (burst_number decreciente y amplitud creciente).
- Limpiar y extraer la envolvente con nk.emg_clean() + nk.emg_amplitude().
- Dividir la envolvente en ventanas de 1 s y para cada ventana calcular su RMS y la frecuencia mediana vía Welch (scipy.signal.welch).
- Ajustar una recta (regresión lineal) al RMS vs. tiempo y otra al freq_med vs. tiempo, y extraer sus pendientes (slope).

### Desarrollo:

### Resultado:

### Pregunta de reflexión 1: ¿Cuál de las dos pendientes (RMS o freq_med) resulta ser un indicador más sensible a la fatiga en este escenario sintético?
- sdsdssds

### Pregunta de reflexión 2: ¿Cómo cambiarían las pendientes si aumentas el nivel de ruido en la simulación?
- sdsdssds

## 3. Bibliografía <a name="id3"></a>
