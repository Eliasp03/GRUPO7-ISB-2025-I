# Laboratorio 12 - Avance del proyecto

## Proyecto: Análisis de señales EMG para detección de patrones de fatiga muscular en miembro inferior

## 🎯 Objetivo

Desarrollar un pipeline en Python que permita analizar señales electromiográficas (EMG) de miembros inferiores para identificar posibles patrones de fatiga muscular, basándose en características extraídas del dominio temporal y su evolución durante caminatas prolongadas.

## Contenido
1. [Origen de los datos](#id1)
2. [Procedimiento de preprocesamiento](#id2)
3. [Extracción de características](#id3)
   - [Características basadas en energía de bandas](#id4)
   - [Características basadas en Wavelet](#id5) 
5. [Optimización y selección](#id6)

---

## 1. Origen de los datos <a name="id1"></a>

Se utilizará la base de datos pública:

**📚 Nombre:**  
*Surface electromyographic signals collected during long-lasting ground walking of young able-bodied subjects*

**🔗 Enlace:**  
[PhysioNet - semg/1.0.1](https://physionet.org/content/semg/1.0.1/)

**Descripción:**

- Señales **sEMG** obtenidas de **10 músculos del miembro inferior** (5 por pierna):  
  - Gastrocnemius lateralis (GL)  
  - Tibialis anterior (TA)  
  - Rectus femoris (RF)  
  - Vastus lateralis (VL)  
  - Hamstrings (Ham)
  
- Datos de **31 sujetos sanos** (20–30 años), caminando durante **~5 minutos** por una ruta en forma de “8” (curvas + tramos rectos).
- Registro simultáneo de:  
  - sEMG (μV)  
  - Footswitch (V)  
  - Electrogoniometría (°)
- Formato de archivo: `.dat` y `.hea` (compatible con `wfdb` en Python)
- Frecuencia de muestreo: **2000 Hz**  
- Resolución: **12 bits**  
- Alta fidelidad (CMRR > 126 dB, ruido < 1 µV rms)

**Justificación de uso:**  

Aunque no se indujo fatiga muscular intencionadamente, la duración de la caminata permite explorar la **variabilidad intra-sujeto** a lo largo del tiempo. Esto hace posible identificar **patrones progresivos relacionados con fatiga local o ajustes neuromusculares**.

---

## 2. ⚙️ Procedimiento de preprocesamiento <a name="id2"></a>

1. **Lectura y visualización inicial**:  
   Carga de los archivos con la librería `wfdb`.

2. **Filtrado de señales EMG**:  
   - Pasa banda Butterworth (20–450 Hz)  
   - Filtro notch (50/60 Hz) si es necesario  

3. **Rectificación**:  
   Conversión a valores absolutos.

4. **Segmentación temporal**:  
   División de la señal en bloques (ej. 10 ventanas de 30 segundos) para observar evolución de características.

5. **Normalización**:  
   - Z-score u otra estrategia si se requiere para comparación intersujeto.

---

## 3. 📐 Extracción de características <a name="id3"></a>

Por cada ventana de tiempo, se calcularán las siguientes métricas EMG en el dominio temporal:

| Característica | Interpretación |
|----------------|----------------|
| **RMS** (Root Mean Square) | Medida de la energía muscular |
| **MAV** (Mean Absolute Value) | Actividad promedio |
| **ZC** (Zero Crossings) | Complejidad / frecuencia del contenido |
| **SSC** (Slope Sign Changes) | Variabilidad / oscilaciones |
| **WL** (Waveform Length) | Longitud del contorno de señal |

Estas métricas serán analizadas en función del tiempo para identificar **tendencias relacionadas con la aparición de fatiga**.

---

## 4. 🗺️ Organización del proyecto



## 4. Optimización y selección <a name="id6"></a>

### Objetivo: 
- Integrar y analizar los datos a través de observaciones temporales, frecuenciales y espaciales empleando MNE-Python (Epochs, Evoked, montage, interpolate_bads).

### Desarrollo: 


#### a. Filtrado y eliminación de artefactos

```bash
ica = mne.preprocessing.ICA(n_components=15, random_state=97, max_iter='auto')
```

#### b. Visualización de la distribución espacial de los electrodos
```bash
fig_sensor = raw_ica.plot_sensors(show_names=True, show=False)
fig_sensor.savefig("L11_images/post_sensor_posiciones.png")
```

#### c. Segmentación en épocas (Epochs) y cálculo del promedio (Evoked)

```bash
events = mne.make_fixed_length_events(raw_ica, id=1, duration=2.)
```

#### d. Mapa topográfico del EEG

```bash
montage = make_standard_montage("standard_1020")
```

#### e. Reducción de dimensionalidad con PCA

```bash
# Visualización de PCA
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue')
plt.title("Proyección PCA de características")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.savefig("L11_images/post_pca_features.png")
plt.close()
```

