import mne
import numpy as np
from scipy.integrate import simpson

# Cargar archivo
raw = mne.io.read_raw_edf("S001R10.edf", preload=True)
new_names = {ch: ch.strip('.').upper() for ch in raw.ch_names}
raw.rename_channels(new_names)
raw.set_montage("standard_1020", on_missing='ignore')
raw.filter(1., 40.)
raw.notch_filter(60)

# Duración segura
duracion_total = raw.times[-1]
psd = raw.compute_psd(fmin=0.5, fmax=40.0, tmax=min(60, duracion_total), picks="eeg")
psds = psd.get_data()
freqs = psd.freqs

# Verificar frecuencias disponibles
print(f"Rango de freqs disponibles: {freqs[0]:.2f} - {freqs[-1]:.2f} Hz")

# Bandas
bandas = {
    'delta': (0.5, 4),
    'theta': (4, 8),
    'alpha': (8, 13),
    'beta': (13, 30),
}


# Energía por banda
energia_bandas = {}
for nombre, (fmin, fmax) in bandas.items():
    idx = np.logical_and(freqs >= fmin, freqs <= fmax)
    print(f"{nombre}: {np.sum(idx)} puntos de frecuencia en banda")
    if not np.any(idx):
        energia_bandas[nombre] = np.zeros(psds.shape[0])
    else:
        energia = simpson(y=psds[:, idx], x=freqs[idx])
        energia_bandas[nombre] = energia * 1e12 #convert to uV^2


# Resultado
for banda, valores in energia_bandas.items():
    print(f"Energía en {banda}: {np.mean(valores):.15f}")
