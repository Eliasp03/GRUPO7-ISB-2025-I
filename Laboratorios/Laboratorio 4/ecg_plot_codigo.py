import ecg_plot
import matplotlib.pyplot as plt

# Ruta del archivo
file_path = r"C:\Users\ADMIN\Desktop\1derEjercicio.txt"

# Lista para almacenar los valores del ECG
ecg = []

# Leer el archivo
with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('#'):
            continue
        if line.strip() == '':
            continue
        columns = line.strip().split()
        if len(columns) >= 6:
            ecg.append(int(columns[5]))

# Escalar valores
ecg = [valor / 1000 for valor in ecg]

# Graficar ECG
ecg_plot.plot_1(ecg, sample_rate=1000)

# Ajustes para mejorar el eje X
plt.xticks(rotation=45)              # Rota las etiquetas del eje X
plt.locator_params(axis='x', nbins=30)  # Limita la cantidad de etiquetas
plt.tight_layout()                   # Ajusta para que no se sobrepongan

# Mostrar el gráfico
ecg_plot.show()


