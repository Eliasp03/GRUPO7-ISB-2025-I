import mne
import numpy as np
import pywt
import os

# Parámetros
wavelet = 'db4'
nivel = 4
canales_eeg = 'eeg'
carpeta = '.'

# Etiquetas de coeficientes
niveles = [f'cA{nivel}'] + [f'cD{i}' for i in range(nivel, 0, -1)]

# Encabezado de resultados
print(f"{'Archivo':<12} " + " ".join([f"{n:<12}" for n in niveles]))

# Iterar sobre archivos
for i in range(1, 11):
    archivo = f"S001R{i:02d}.edf"
    ruta = os.path.join(carpeta, archivo)

    try:
        raw = mne.io.read_raw_edf(ruta, preload=True, verbose=False)
        raw.filter(1., 40., fir_design='firwin')
        raw.notch_filter(60., fir_design='firwin')
        raw.pick_types(eeg=True)

        # Canal promedio
        data, _ = raw.get_data(return_times=True)
        promedio = np.mean(data, axis=0)

        # Transformada wavelet
        coef = pywt.wavedec(promedio, wavelet, level=nivel)

        # Varianzas y conversión a µV²
        varianzas = [np.var(c) * 1e12 for c in coef]

        # Mostrar resultados formateados
        print(f"{archivo:<12} " + " ".join([f"{v:.2f}".ljust(12) for v in varianzas]))

    except Exception as e:
        print(f"{archivo:<12} Error: {e}")
