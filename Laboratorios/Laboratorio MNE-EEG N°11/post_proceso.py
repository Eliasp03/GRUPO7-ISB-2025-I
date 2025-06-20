import mne
from mne.channels import make_standard_montage
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# cargar el archivo
file = "S001R04.edf"
raw = mne.io.read_raw_edf(file, preload=True)
raw.filter(1., 40., fir_design='firwin')
raw.notch_filter(60., fir_design='firwin')
raw.pick_types(eeg=True)  # Solo EEG
# Eliminar puntos y pasar a mayúsculas para usar montaje estándar
clean_names = {ch: ch.replace('.', '').upper() for ch in raw.ch_names}
raw.rename_channels(clean_names)
# Aplicar sistema de posiciones estándar
raw.set_montage("standard_1020", on_missing='ignore')

# Aplicar ICA
ica = mne.preprocessing.ICA(n_components=15, random_state=97, max_iter='auto')
ica.fit(raw)
ica.exclude = [0, 1]  # Estos índices se deben ajustar manualmente luego de visualizar
raw_ica = raw.copy()
ica.apply(raw_ica)

# parte b) sensorial y montaje
fig_sensor = raw_ica.plot_sensors(show_names=True, show=False)
fig_sensor.savefig("L11_images/post_sensor_posiciones.png")

# parte c)simulación de eventos
events = mne.make_fixed_length_events(raw_ica, id=1, duration=2.)
epochs = mne.Epochs(raw_ica, events, event_id=1, tmin=-0.2, tmax=0.8, baseline=(None, 0), preload=True)
fig_epochs = epochs.plot(show=False)
fig_epochs.savefig("L11_images/post_epochs_simulados.png")

# parte c) cálculo evoked
evoked = epochs.average()
fig_evoked = evoked.plot(show=False)
fig_evoked.savefig("L11_images/post_evoked_promediado.png")

# parte d) Topomap en 3 tiempos
montage = make_standard_montage("standard_1020")
raw.set_montage(montage, on_missing='ignore')
# excluir los canales conflictivos
canales_conflictivos = ['FCZ', 'CZ', 'CPZ', 'FP1', 'FPZ', 'FP2', 'AFZ', 'FZ', 'PZ', 'POZ', 'OZ', 'IZ']
# Filtrar evoked sin esos canales
evoked_clean = evoked.copy().drop_channels(canales_conflictivos)
fig_topomap = evoked_clean.plot_topomap(times=[0.1, 0.2, 0.3], ch_type='eeg', show=False)
fig_topomap.savefig("L11_images/post_evoked_topomap.png")

# parte e) extracción de features y PCA (simulado)
# Simulación de un DataFrame de features
np.random.seed(0)
X = np.random.rand(10, 6)
# Normalización
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Reducción de dimensionalidad
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualización de PCA
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue')
plt.title("Proyección PCA de características")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.savefig("L11_images/post_pca_features.png")
plt.close()
