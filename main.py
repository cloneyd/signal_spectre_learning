import sys

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from PySide6.QtCore import Qt, Slot, QSize
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QLineEdit,
    QLabel,
    QSpinBox,
    QPushButton
)

from wave import (
    generate_sine_wave,
    generate_cosine_wave,
    generate_triangle_wave,
    generate_sawtooth_wave,
    generate_square_wave
)

wave_generator = {
    'sine': generate_sine_wave,
    'cosine': generate_cosine_wave,
    'triangle': generate_triangle_wave,
    'sawtooth': generate_sawtooth_wave,
    'square': generate_square_wave,
}

sample_rate = 0
duration = 0


def set_sample_rate(value):
    global sample_rate
    sample_rate = value


def set_duration(value):
    global duration
    duration = value


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #  create widgets
        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.axes = self.view.figure.subplots()
        self.axes.grid(True)
        self.toolbar = NavigationToolbar2QT(self.view, self)

        #  Create layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        self.setLayout(vlayout)


class SignalPlotWidget(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_signal(self, signal_name):
        if signal_name == '-':
            self.axes.clear()
            self.axes.grid(True)
        else:
            global sample_rate
            global duration

            x, y = wave_generator[signal_name](1, sample_rate, duration)

            self.axes.clear()
            self.axes.grid(True)
            self.axes.plot(x, y)

        self.view.draw()


class SpectrePlotWidget(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_spectre(self, signal_name):
        if signal_name == '-':
            self.axes.clear()
            self.axes.grid(True)
        else:
            global sample_rate
            global duration

            _, y = wave_generator[signal_name](1, sample_rate, duration)

            self.axes.clear()
            self.axes.grid(True)
            self.axes.magnitude_spectrum(y, Fs=sample_rate)

        self.view.draw()


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(QSize(1920, 1080))

        signal_types = ['-', 'sine', 'cosine', 'triangle', 'sawtooth', 'square']
        self.signal_form_combo = QComboBox(self)
        self.signal_form_combo.addItems(signal_types)

        self.signal_plot = SignalPlotWidget()
        self.spectre_plot = SpectrePlotWidget()

        self.sample_rate_spin = QSpinBox()
        self.sample_rate_spin.setRange(0, 200_000)
        self.sample_rate_spin.setValue(440)
        set_sample_rate(self.sample_rate_spin.value())
        self.sample_rate_spin.valueChanged.connect(set_sample_rate)
        self.sample_rate_label = QLabel('Sample rate')
        self.sample_rate_label.setBuddy(self.sample_rate_spin)

        self.duration_spin = QSpinBox()
        self.duration_spin.setValue(5)
        set_duration(self.duration_spin.value())
        self.duration_spin.valueChanged.connect(set_duration)
        self.duration_label = QLabel('Duration label')
        self.duration_label.setBuddy(self.duration_spin)

        params_layout = QVBoxLayout()
        params_layout.addWidget(self.signal_form_combo)

        sample_rate_input_layout = QHBoxLayout()
        sample_rate_input_layout.addWidget(self.sample_rate_label)
        sample_rate_input_layout.addWidget(self.sample_rate_spin)

        duration_input_layout = QHBoxLayout()
        duration_input_layout.addWidget(self.duration_label)
        duration_input_layout.addWidget(self.duration_spin)

        params_layout.addLayout(sample_rate_input_layout)
        params_layout.addLayout(duration_input_layout)

        plots_layout = QHBoxLayout()
        plots_layout.addWidget(self.signal_plot)
        plots_layout.addWidget(self.spectre_plot)

        receive_button = QPushButton('Receive')
        receive_button.clicked.connect(self.receive)

        main_layout = QVBoxLayout()
        main_layout.addLayout(params_layout)
        main_layout.addLayout(plots_layout)
        main_layout.addWidget(receive_button)

        self.setLayout(main_layout)

    def receive(self):
        form_name = self.signal_form_combo.currentText()
        self.signal_plot.set_signal(form_name)
        self.spectre_plot.set_spectre(form_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec())
