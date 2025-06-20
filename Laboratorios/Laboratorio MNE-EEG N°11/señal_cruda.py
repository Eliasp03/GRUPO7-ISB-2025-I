import mne
import matplotlib.pyplot as plt

# Cargar archivo .edf
ruta_archivo = "S001R10.edf"
raw = mne.io.read_raw_edf(ruta_archivo, preload=True)

# Renombrar canales para quitar puntos extraños (., ..)
new_names = {ch_name: ch_name.strip('.').upper() for ch_name in raw.ch_names}
raw.rename_channels(new_names)

# Aplicar sistema de electrodos estándar
raw.set_montage('standard_1020', on_missing='ignore')

# Guardar la señal cruda
fig = raw.plot(n_channels=32, duration=10, scalings='auto')
fig.savefig("eeg_crudo10.png")

# Guardar el espectro de potencia (PSD)
fig_psd = raw.plot_psd(fmax=60, average=True)
fig_psd.savefig("psd_crudo10.png")
