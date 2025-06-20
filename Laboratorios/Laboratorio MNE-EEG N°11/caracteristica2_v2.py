import mne
import numpy as np
import pywt
import pandas as pd

# Parámetros
archivos = [f"S001R{i:02}.edf" for i in range(1, 11)]
wavelet = 'db4'
nivel = 4

# Función para extraer estadísticas de los coeficientes
def extraer_features_wavelet(signal, wavelet, nivel):
    coeficientes = pywt.wavedec(signal, wavelet, level=nivel)
    nombres = [f'cA{nivel}'] + [f'cD{i}' for i in range(nivel, 0, -1)]
    features = []

    for nombre, coef in zip(nombres, coeficientes):
        stats = {
            'Nivel': nombre,
            'Varianza (µV²)': np.var(coef) * 1e12,
            'Energía (µV²)': np.sum(coef**2) * 1e12,
            'Máximo (µV)': np.max(coef) * 1e6,
            'Mediana (µV)': np.median(coef) * 1e6,
            'Desv. Estándar (µV)': np.std(coef) * 1e6,
        }
        features.append(stats)
    
    return features

# Procesar todos los archivos
tabla_final = []

for archivo in archivos:
    raw = mne.io.read_raw_edf(archivo, preload=True, verbose=False)
    raw.filter(1., 40., fir_design='firwin')
    raw.notch_filter(60., fir_design='firwin')
    raw.pick_types(eeg=True)

    datos, _ = raw.get_data(return_times=True)
    canal_prom = np.mean(datos, axis=0)

    features = extraer_features_wavelet(canal_prom, wavelet, nivel)
    for f in features:
        f['Archivo'] = archivo
        tabla_final.append(f)

# Convertir a DataFrame y reorganizar columnas
df = pd.DataFrame(tabla_final)
df = df[['Archivo', 'Nivel', 'Varianza (µV²)', 'Energía (µV²)', 'Máximo (µV)', 'Mediana (µV)', 'Desv. Estándar (µV)']]

# Mostrar resultados
print(df.head(50).to_string(index=False))
