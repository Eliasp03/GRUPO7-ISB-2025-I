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
3. Simulamos una señal EMG base con 10 segundos de duración, 1000 Hz de muestreo, 10 ráfagas (bursts) y bajo nivel de ruido.
```bash
emg_base = nk.emg_simulate(duration=10, sampling_rate=1000, burst_number=10, noise=0.01)
```
4. Mostramos encabezado en consola y preparamos una figura con 5 subgráficos para comparar las señales simuladas.
```bash
print("Resultados del Symmetry Ratio:\n")
plt.figure(figsize=(12, 8))
```
5. Iniciamos el bucle para aplicar cada una de las escalas definidas al músculo izquierdo. La señal derecha se mantiene como referencia original, La señal izquierda se escala proporcionalmente según el valor actual (escala). Luego se aplica filtros de limpieza a ambas señales usando la función emg_clean() de NeuroKit2, ahora calculamos la envolvente de la señal EMG (indicador de amplitud muscular) con emg_amplitude(). Además, calculamos el área bajo la curva (AUC) de la envolvente de cada señal usando integración numérica (trapz), como medida de activación. Se calcula el Symmetry Ratio como el cociente entre el menor y mayor área (siempre ≤ 1), y se guarda para análisis posterior. Mostramos por consola el resultado numérico para cada escala. Por último, se grafican las señales limpias de izquierda y derecha en subplots para observar visualmente la diferencia en amplitud y simetría.
```bash
for i, escala in enumerate(escalas):
    emg_derecha = emg_base.copy()
    emg_izquierda = emg_base * escala
    clean_der = nk.emg_clean(emg_derecha, sampling_rate=1000)
    clean_izq = nk.emg_clean(emg_izquierda, sampling_rate=1000)
    amp_der = nk.emg_amplitude(clean_der)
    amp_izq = nk.emg_amplitude(clean_izq)
    area_der = np.trapz(amp_der)
    area_izq = np.trapz(amp_izq)
    ratio = min(area_der, area_izq) / max(area_der, area_izq)
    ratios.append(ratio)
    print(f"Escala {int(escala * 100)}%: Symmetry Ratio = {ratio:.4f}")
    plt.subplot(5, 1, i+1)
    plt.plot(clean_izq, label="Izquierda (escalada)", alpha=0.7)
    plt.plot(clean_der, label="Derecha (original)", alpha=0.7)
    plt.title(f"Escala {int(escala*100)}% - Symmetry Ratio = {ratio:.2f}")
    plt.ylabel("Amplitud")
    if i == 0:
        plt.legend(loc="upper right")
    if i < 4:
        plt.xticks([])
```
6. Se ajusta el diseño de la figura y se muestra el gráfico completo de comparación entre señales.
```bash
plt.tight_layout()
plt.suptitle("Comparación de señales EMG simuladas (Izquierda vs Derecha)", y=1.02)
plt.show()
```
7. Finalmente, se crea una gráfica de barras donde se visualiza la relación Escala (%) vs Symmetry Ratio, cumpliendo con el objetivo del experimento.
```bash
plt.figure(figsize=(8, 5))
plt.bar([int(e * 100) for e in escalas], ratios, color='skyblue')
plt.xlabel("Escala de amplitud del músculo izquierdo (%)")
plt.ylabel("Symmetry Ratio")
plt.title("Relación de Simetría vs Escala de Amplitud")
plt.ylim(0, 1.05)
plt.grid(axis='y')
plt.show()
```
### Resultados:

| Escala (%) | Symmetry Ratio |
|------------|----------------|
| 20         | 0.04           |
| 40         | 0.16           |
| 60         | 0.36           |
| 80         | 0.64           |
| 100        | 1.00           |

#### Comparación de Señales EMG:

![Señales EMG](ruta/a/tu/imagen1.png)

#### Relación de Simetría vs Escala

![Relación Simetría](ruta/a/tu/imagen2.png)

Se confirma que el **Symmetry Ratio** es directamente proporcional a la escala de amplitud del músculo izquierdo, bajo condiciones idénticas de señal y ruido. Esto valida la métrica como indicador útil de simetría muscular. 


### Pregunta de reflexión: ¿A partir de qué nivel de desbalance la simetría cae por debajo de un umbral “aceptable” (p.ej. 80 %)?
- La simetría cae por debajo del umbral del 80% con cualquier desbalance en la amplitud entre músculos. Específicamente, solo una igualdad total (100%) logra un Symmetry Ratio ≥ 0.80. Por tanto, incluso una disminución leve (ej. 80% de amplitud relativa) resulta en una simetría considerada inaceptable bajo ese criterio.


## 2. Ejercicio B: Índices de fatiga – pendiente de RMS vs. pendiente de frecuencia <a name="id2"></a>
### Objetivo: Comparar dos métricas clásicas de fatiga: la tasa de crecimiento de la amplitud (RMS) y la tasa de caída de la frecuencia mediana.
### Implementar:
- Simular una señal EMG de 30 s dividida en 3 segmentos de 10 s, siguiendo el patrón del ejercicio de fatiga (burst_number decreciente y amplitud creciente).
- Limpiar y extraer la envolvente con nk.emg_clean() + nk.emg_amplitude().
- Dividir la envolvente en ventanas de 1 s y para cada ventana calcular su RMS y la frecuencia mediana vía Welch (scipy.signal.welch).
- Ajustar una recta (regresión lineal) al RMS vs. tiempo y otra al freq_med vs. tiempo, y extraer sus pendientes (slope).

### Desarrollo:

### Resultados:


### Pregunta de reflexión 1: ¿Cuál de las dos pendientes (RMS o freq_med) resulta ser un indicador más sensible a la fatiga en este escenario sintético?
- sdsdssds

### Pregunta de reflexión 2: ¿Cómo cambiarían las pendientes si aumentas el nivel de ruido en la simulación?
- sdsdssds

## 3. Bibliografía <a name="id3"></a>
