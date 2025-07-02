# Entrenamiento y validación de RandomForest para detección de fatiga EMG
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('emg_features_dataset.csv', sep=',')

# Preparar features (X) y etiquetas (y)
X = df[["RMS", "ZC", "MDF", "MNF"]]
y = df["label_fatiga"]

# Separar entrenamiento y prueba (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Entrenar el RandomForest
clf = RandomForestClassifier(
    n_estimators=100, max_depth=None, random_state=42, class_weight="balanced"
)
clf.fit(X_train, y_train)

# Evaluar desempeño
y_pred = clf.predict(X_test)

print("=== Classification report ===")
print(classification_report(y_test, y_pred, target_names=['Leve', 'Moderada', 'Grave'], digits=3))

print("=== Confusion Matrix ===")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Leve', 'Moderada', 'Grave'])
disp.plot(cmap="Blues")
plt.title("Matriz de confusión - RandomForest")
plt.show()

# Importancia de variables
importancias = clf.feature_importances_
plt.bar(["RMS", "ZC", "MDF", "MNF"], importancias)
plt.title("Importancia de cada feature en el modelo")
plt.ylabel("Importancia")
plt.show()

# Guardar el modelo entrenado
joblib.dump(clf, "modelo_rf.joblib")
print("Modelo guardado como modelo_rf.joblib")
