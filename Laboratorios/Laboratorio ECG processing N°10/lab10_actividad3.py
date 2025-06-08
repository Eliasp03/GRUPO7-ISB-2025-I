import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.stats import skew, kurtosis
import seaborn as sns

# Parámetros
fs = 1000  # Hz
duration = 20  # segundos

# Simular 3 señales ECG distintas (puedes personalizar HR o forma)
ecg1 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=70)
ecg2 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=90)
ecg3 = nk.ecg_simulate(duration=duration, sampling_rate=fs, heart_rate=110)

signals = [ecg1, ecg2, ecg3]
labels = ["70bpm", "90bpm", "110bpm"]

# Función para extraer características
def extract_features(signal):
    return {
        "Mean": np.mean(signal),
        "Median": np.median(signal),
        "STD": np.std(signal),
        "Kurtosis": kurtosis(signal),
        "Skewness": skew(signal),
        "Energy": np.sum(signal**2)
    }

# Extraer y almacenar en DataFrame
features = [extract_features(sig) for sig in signals]
df = pd.DataFrame(features)
df["Label"] = labels

print("\n=== Tabla de características ===")
print(df)

# Aplicar PCA (2D)
X = df.drop(columns=["Label"])
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Convertir a DataFrame para graficar
df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Label"] = labels

# Scatter plot del PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="Label", s=120, palette="Set1")
plt.title("PCA de características de 3 señales ECG")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.tight_layout()
plt.show()
