import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import skew, kurtosis
from sklearn.decomposition import PCA

# Parámetros generales
fs = 1000  # frecuencia de muestreo
duration = 20  # duración en segundos
np.random.seed(42)  # reproducibilidad

# Señal normal base
ti0 = np.array([-70, -15, 0, 15, 100])
ai0 = np.array([1.2, -5, 30, -7.5, 0.75])
bi0 = np.array([0.25, 0.1, 0.1, 0.1, 0.4])

# Generar 6 señales ECG (2 por tipo)
signals = []
labels = []

# ECG tipo 0: normal
for _ in range(2):
    ecg = nk.ecg_simulate(duration=duration, sampling_rate=fs,
                          method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)
    signals.append(ecg)
    labels.append(0)

# ECG tipo 1: modificada (ligera variación de parámetros)
for _ in range(2):
    ti1 = np.random.normal(ti0, np.ones(5) * 3)
    ai1 = np.random.normal(ai0, np.abs(ai0 / 5))
    bi1 = np.random.normal(bi0, np.abs(bi0 / 5))
    ecg = nk.ecg_simulate(duration=duration, sampling_rate=fs,
                          method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)
    signals.append(ecg)
    labels.append(1)

# ECG tipo 2: anómala (onda T invertida, QRS ancho)
for _ in range(2):
    ti2 = np.random.normal(ti0, np.ones(5) * 3)
    ai2 = np.random.normal(ai0, np.abs(ai0 / 5))
    bi2 = np.random.normal(bi0, np.abs(bi0 / 5))
    ai2[4] = -0.5  # T invertida
    bi2[2] *= 2    # QRS ancho
    ecg = nk.ecg_simulate(duration=duration, sampling_rate=fs,
                          method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)
    signals.append(ecg)
    labels.append(2)

# Extraer características

def extract_features(ecg_signal):
    return {
        "Mean": np.mean(ecg_signal),
        "Median": np.median(ecg_signal),
        "STD": np.std(ecg_signal),
        "Kurtosis": kurtosis(ecg_signal),
        "Skewness": skew(ecg_signal),
        "Energy": np.sum(ecg_signal**2)
    }

features = []
for i, ecg in enumerate(signals):
    feats = extract_features(ecg)
    feats["Label"] = labels[i]
    features.append(feats)

df_features = pd.DataFrame(features)

print("\n=== Tabla de características ===")
print(df_features)

# PCA en 2 dimensiones
X = df_features.drop(columns=["Label"])
y = df_features["Label"]

# Aplicar PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Crear DataFrame para graficar
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Label"] = y.astype(str)

# Visualización PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="Label", palette="Set2", s=100)
plt.title("PCA de características ECG (6 señales)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(alpha=0.3)
plt.legend(title="Clase")
plt.tight_layout()
plt.show()
