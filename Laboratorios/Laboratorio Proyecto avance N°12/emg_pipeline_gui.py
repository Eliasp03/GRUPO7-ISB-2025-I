import sys
import re
import wfdb
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import pywt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QStackedWidget,
    QFormLayout, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

PRIMARY_COLOR = "#005377"
ACCENT_COLOR = "#FFC857"
BACKGROUND_COLOR = "#F4F4F4"
TEXT_COLOR = "#1E1E1E"
BUTTON_COLOR = "#2A9D8F"

class RegistroWidget(QWidget):
    def __init__(self, switch_to_loader):
        super().__init__()
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR};")
        layout = QVBoxLayout()

        title = QLabel("\nDETECCIÓN DE PATRONES DE FATIGA")
        title.setFont(QFont("Segoe UI", 42, QFont.Bold))
        title.setStyleSheet(f"color: {PRIMARY_COLOR};")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Segoe UI", 28))
        self.age_input = QLineEdit()
        self.age_input.setFont(QFont("Segoe UI", 28))
        self.dni_input = QLineEdit()
        self.dni_input.setFont(QFont("Segoe UI", 28))
        self.dni_input.setMaxLength(8)
        self.email_input = QLineEdit()
        self.email_input.setFont(QFont("Segoe UI", 28))
        form.setVerticalSpacing(25)
        form.addRow("<b>Nombre:</b>", self.name_input)
        form.addRow("<b>Edad:</b>", self.age_input)
        form.addRow("<b>DNI:</b>", self.dni_input)
        form.addRow("<b>Correo electrónico:</b>", self.email_input)
        layout.addLayout(form)

        self.start_btn = QPushButton("Evaluar")
        self.start_btn.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: white; font-weight: bold; padding: 24px; font-size: 28px; border-radius: 6px;")
        self.start_btn.clicked.connect(lambda: self.validate(switch_to_loader))
        layout.addWidget(self.start_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def validate(self, switch):
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        dni = self.dni_input.text().strip()
        email = self.email_input.text().strip()

        if not all([name, age, dni, email]):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos.")
            return

        if not age.isdigit():
            QMessageBox.warning(self, "Edad inválida", "La edad debe ser un número.")
            return

        if not dni.isdigit() or len(dni) != 8:
            QMessageBox.warning(self, "DNI inválido", "El DNI debe contener exactamente 8 dígitos.")
            return

        email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            QMessageBox.warning(self, "Correo inválido", "Ingrese un correo electrónico válido.")
            return

        self.user_info = {"name": name, "age": age, "dni": dni, "email": email}
        switch(self.user_info)

class LoaderWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR};")
        layout = QVBoxLayout()

        self.label = QLabel("Cargar archivo .hea")
        self.label.setFont(QFont("Segoe UI", 32))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.load_btn = QPushButton("Seleccionar archivo")
        self.load_btn.setFont(QFont("Segoe UI", 26))
        self.load_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: {TEXT_COLOR}; font-size: 26px; padding: 16px; border-radius: 6px;")
        self.load_btn.clicked.connect(self.load_file)
        layout.addWidget(self.load_btn, alignment=Qt.AlignCenter)

        self.next_btn = QPushButton("Analizar Señal")
        self.next_btn.setFont(QFont("Segoe UI", 26))
        self.next_btn.setEnabled(False)
        self.next_btn.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: white; font-size: 26px; padding: 16px; border-radius: 6px;")
        layout.addWidget(self.next_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Cargar .hea", "", "*.hea")
        if path:
            base = path.replace(".hea", "")
            try:
                self.record = wfdb.rdrecord(base)
                self.label.setText(f"Archivo cargado: {base}")
                try:
                    self.next_btn.clicked.disconnect()
                except TypeError:
                    pass  # No estaba conectado

                self.next_btn.clicked.connect(lambda: self.switch_to_analyzer(self.record, self.user_info))
                self.next_btn.setEnabled(True)
            except Exception as e:
                QMessageBox.critical(self, "Error al cargar archivo", str(e))

    def set_switch_callback(self, callback, user_info):
        self.switch_to_analyzer = callback
        self.user_info = user_info

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QTextDocument

class EMGAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR};")

        layout = QVBoxLayout()

        self.title = QLabel("Resultado del Análisis EMG")
        self.title.setFont(QFont("Segoe UI", 38, QFont.Bold))
        self.title.setStyleSheet(f"color: {PRIMARY_COLOR};")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.text_result = QTextEdit()
        self.text_result.setFont(QFont("Segoe UI", 22))
        self.text_result.setReadOnly(True)
        layout.addWidget(self.text_result)

        self.figure = plt.figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.export_btn = QPushButton("Exportar PDF")
        self.export_btn.setFont(QFont("Segoe UI", 24))
        self.export_btn.setStyleSheet(f"background-color: {ACCENT_COLOR}; color: black; font-size: 24px; padding: 16px; border-radius: 6px;")
        self.export_btn.clicked.connect(self.export_pdf)
        layout.addWidget(self.export_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def analyze(self, record, user_info):
        self.user_info = user_info
        emg_signal = record.p_signal[:, 0]
        fs = record.fs

        b, a = signal.butter(4, [20/(fs/2), 450/(fs/2)], btype='band')
        filtered = signal.filtfilt(b, a, emg_signal)
        rectified = np.abs(filtered)

        rms = np.sqrt(np.mean(rectified**2))
        mav = np.mean(rectified)
        zc = np.sum(np.diff(np.sign(rectified)) != 0)
        ssc = np.sum(np.diff(np.sign(np.diff(rectified))) != 0)
        wl = np.sum(np.abs(np.diff(rectified)))

        self.results_data = f"RMS: {rms:.4f}\nMAV: {mav:.4f}\nZC: {zc}\nSSC: {ssc}\nWL: {wl:.2f}"
        self.text_result.setText(self.results_data)

        self.figure.clear()
        tiempo = np.arange(len(emg_signal)) / fs

        ax1 = self.figure.add_subplot(211)
        ax1.plot(tiempo, emg_signal, color='gray')
        ax1.set_title("Señal EMG Original", fontsize=14)
        ax1.set_ylabel("Amplitud (uV)", fontsize=12)

        ax2 = self.figure.add_subplot(212)
        ax2.plot(tiempo, filtered, color=PRIMARY_COLOR)
        ax2.set_title("Señal EMG Filtrada", fontsize=14)
        ax2.set_xlabel("Tiempo (s)", fontsize=12)
        ax2.set_ylabel("Amplitud (uV)", fontsize=12)

        self.canvas.draw()

    def export_pdf(self):
        from matplotlib.backends.backend_pdf import PdfPages

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar PDF", "analisis_emg_resultado.pdf", "PDF Files (*.pdf)", options=options)
        if not file_path:
            return

        with PdfPages(file_path) as pdf:
            self.figure.suptitle(
                f"Paciente: {self.user_info['name']}, DNI: {self.user_info['dni']}, Edad: {self.user_info['age']}",
                fontsize=12, y=1.02
            )
            pdf.savefig(self.figure, bbox_inches='tight')
            plt.close(self.figure)

        QMessageBox.information(self, "Exportación completada", "Los resultados y la gráfica se han exportado en PDF correctamente.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    stacked = QStackedWidget()

    analyzer = EMGAnalyzer()
    loader = LoaderWidget()
    registro = RegistroWidget(lambda user_info: go_loader(user_info))

    stacked.addWidget(registro)
    stacked.addWidget(loader)
    stacked.addWidget(analyzer)

    def go_loader(user_info):
        loader.set_switch_callback(lambda record, info: go_analyzer(record, info), user_info)
        stacked.setCurrentWidget(loader)

    def go_analyzer(record, user_info):
        analyzer.analyze(record, user_info)
        stacked.setCurrentWidget(analyzer)

    window = QMainWindow()
    window.setWindowTitle("Verificación EMG")
    window.setGeometry(100, 100, 1200, 800)
    window.setCentralWidget(stacked)
    window.show()

    sys.exit(app.exec_())
