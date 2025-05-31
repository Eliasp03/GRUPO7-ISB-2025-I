import neurokit2 as nk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Escalas de amplitud para el "músculo izquierdo"
escalas = [0.2, 0.4, 0.6, 0.8, 1.0]
ratios = []

# Simular señal base
emg_base = nk.emg_simulate(duration=10, sampling_rate=1000, burst_number=10, noise=0.01)

print("Resultados del Symmetry Ratio:\n")

# Crear figura para comparar señales simuladas
plt.figure(figsize=(12, 8))

for i, escala in enumerate(escalas):
    # Señal derecha (sin cambios)
    emg_derecha = emg_base.copy()
    
    # Señal izquierda escalada
    emg_izquierda = emg_base * escala

    # Limpieza
    clean_der = nk.emg_clean(emg_derecha, sampling_rate=1000)
    clean_izq = nk.emg_clean(emg_izquierda, sampling_rate=1000)

    # Amplitud (envolvente)
    amp_der = nk.emg_amplitude(clean_der)
    amp_izq = nk.emg_amplitude(clean_izq)

    # Área bajo la curva
    area_der = np.trapz(amp_der)
    area_izq = np.trapz(amp_izq)

    # Calcular ratio de simetría
    ratio = min(area_der, area_izq) / max(area_der, area_izq)
    ratios.append(ratio)

    # Mostrar resultado en consola
    print(f"Escala {int(escala * 100)}%: Symmetry Ratio = {ratio:.4f}")

    # Graficar par de señales EMG limpias
    plt.subplot(5, 1, i+1)
    plt.plot(clean_izq, label="Izquierda (escalada)", alpha=0.7)
    plt.plot(clean_der, label="Derecha (original)", alpha=0.7)
    plt.title(f"Escala {int(escala*100)}% - Symmetry Ratio = {ratio:.2f}")
    plt.ylabel("Amplitud")
    if i == 0:
        plt.legend(loc="upper right")
    if i < 4:
        plt.xticks([])

plt.tight_layout()
plt.suptitle("Comparación de señales EMG simuladas (Izquierda vs Derecha)", y=1.02)
plt.show()

# Graficar Symmetry Ratio vs Escala
plt.figure(figsize=(8, 5))
plt.bar([int(e * 100) for e in escalas], ratios, color='skyblue')
plt.xlabel("Escala de amplitud del músculo izquierdo (%)")
plt.ylabel("Symmetry Ratio")
plt.title("Relación de Simetría vs Escala de Amplitud")
plt.ylim(0, 1.05)
plt.grid(axis='y')
plt.show()
