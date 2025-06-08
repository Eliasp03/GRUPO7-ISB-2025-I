import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import skew, kurtosis
from sklearn.decomposition import PCA

# Parámetros
fs = 1000
duration = 20
np.random.seed(42)

# Señal base común
ti0 = np.array([-70, -15, 0, 15, 100])
ai0 = np.array([1.2, -5, 30, -7.5, 0.75])
bi0 = np.array([0.25, 0.1, 0.1, 0.1, 0.4])

# === Crear 3 señales iniciales ===
# Clase 0: normal
ecg0 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)

# Clase 1: modificada
ti1 = np.random.normal(ti0, 3)
ai1 = np.random.normal(ai0, np.abs(ai0 / 5))
bi1 = np.random.normal(bi0, np.abs(bi0 / 5))
ecg1 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)

# Clase 2: anómala
ti2 = np.random.normal(ti0, 3)
ai2 = np.random.normal(ai0, np.abs(ai0 / 5))
bi2 = np.random.normal(bi0, np.abs(bi0 / 5))
ai2[4] = -0.5  # T invertida
bi2[2] *= 2    # QRS ancho
ecg2 = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)

# === Crear 3 señales adicionales con mismas características ===
ecg0_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti0, ai=ai0, bi=bi0)
ecg1_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti1, ai=ai1, bi=bi1)
ecg2_bis = nk.ecg_simulate(duration=duration, sampling_rate=fs, method="ecgsyn", ti=ti2, ai=ai2, bi=bi2)

# Agrupar señales y etiquetas
signals = [ecg0, ecg0_bis, ecg1, ecg1_bis, ecg2, ecg2_bis]
labels = [0, 0, 1, 1, 2, 2]

# === Extraer características ===
def extract_features(signal):
    return {
        "Mean": np.mean(signal),
        "Median": np.median(signal),
        "STD": np.std(signal),
        "Kurtosis": kurtosis(signal),
        "Skewness": skew(signal),
        "Energy": np.sum(signal**2)
    }

features = []
for i, ecg in enumerate(signals):
    feats = extract_features(ecg)
    feats["Label"] = labels[i]
    features.append(feats)

df = pd.DataFrame(features)

print("\n=== Tabla de características ===")
print(df)

# === PCA ===
X = df.drop(columns=["Label"])
y = df["Label"]

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["Label"] = y.astype(str)

# === Visualización ===
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="Label", palette="Set1", s=100)
plt.title("PCA de características ECG (3 clases, 2 señales por clase)")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.tight_layout()
plt.show()
