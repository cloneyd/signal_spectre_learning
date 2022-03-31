import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QLabel,
    QSpinBox,
    QPushButton
)

from SignalPlotWidget import SignalPlotWidget
from SpectrePlotWidget import SpectrePlotWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.fs_params_label = QLabel('First signal', self)
        self.fs_toggle_button = QPushButton('ON/OFF', self)
        self.fs_toggle_button.setCheckable(True)
        self.fs_toggle_button.clicked.connect(self.set_signal)
        self.fs_params_label.setBuddy(self.fs_toggle_button)

        signal_types = ['-', 'sine', 'cosine', 'triangle', 'sawtooth', 'square']

        self.fs_signal_form_combo = QComboBox(self)
        self.fs_signal_form_combo.addItems(signal_types)
        self.fs_signal_form_combo_label = QLabel('Signal form', self)
        self.fs_signal_form_combo_label.setBuddy(self.fs_signal_form_combo)

        self.signal_plot = SignalPlotWidget()
        self.spectre_plot = SpectrePlotWidget()

        self.fs_frequency_spin = QSpinBox()
        self.fs_frequency_spin.setRange(0, 200_000)
        self.fs_frequency_spin.setValue(1)
        self.fs_frequency_label = QLabel('Frequency')
        self.fs_frequency_label.setBuddy(self.fs_frequency_spin)

        self.fs_amplitude_spin = QSpinBox()
        self.fs_amplitude_spin.setRange(0, 200_000)
        self.fs_amplitude_spin.setValue(1)
        self.fs_amplitude_label = QLabel('Amplitude')
        self.fs_amplitude_label.setBuddy(self.fs_amplitude_spin)

        self.fs_sample_rate_spin = QSpinBox()
        self.fs_sample_rate_spin.setRange(0, 200_000)
        self.fs_sample_rate_spin.setValue(440)
        self.fs_sample_rate_label = QLabel('Sample rate, Hz')
        self.fs_sample_rate_label.setBuddy(self.fs_sample_rate_spin)

        self.fs_duration_spin = QSpinBox()
        self.fs_duration_spin.setValue(5)
        self.fs_duration_label = QLabel('Duration, sec')
        self.fs_duration_label.setBuddy(self.fs_duration_spin)

        fs_params_layout = QVBoxLayout()

        fs_switch_layout = QHBoxLayout()
        fs_switch_layout.addWidget(self.fs_params_label)
        fs_switch_layout.addWidget(self.fs_toggle_button)

        fs_signal_form_layout = QHBoxLayout()
        fs_signal_form_layout.addWidget(self.fs_signal_form_combo_label)
        fs_signal_form_layout.addWidget(self.fs_signal_form_combo)

        fs_frequency_input_layout = QHBoxLayout()
        fs_frequency_input_layout.addWidget(self.fs_frequency_label)
        fs_frequency_input_layout.addWidget(self.fs_frequency_spin)

        fs_amplitude_input_layout = QHBoxLayout()
        fs_amplitude_input_layout.addWidget(self.fs_amplitude_label)
        fs_amplitude_input_layout.addWidget(self.fs_amplitude_spin)

        fs_sample_rate_input_layout = QHBoxLayout()
        fs_sample_rate_input_layout.addWidget(self.fs_sample_rate_label)
        fs_sample_rate_input_layout.addWidget(self.fs_sample_rate_spin)

        fs_duration_input_layout = QHBoxLayout()
        fs_duration_input_layout.addWidget(self.fs_duration_label)
        fs_duration_input_layout.addWidget(self.fs_duration_spin)

        fs_params_layout.addLayout(fs_switch_layout)
        fs_params_layout.addLayout(fs_signal_form_layout)
        fs_params_layout.addLayout(fs_frequency_input_layout)
        fs_params_layout.addLayout(fs_amplitude_input_layout)
        fs_params_layout.addLayout(fs_sample_rate_input_layout)
        fs_params_layout.addLayout(fs_duration_input_layout)

        self.ss_params_label = QLabel('Second signal')
        self.ss_toggle_button = QPushButton('ON/OFF', self)
        self.ss_toggle_button.setCheckable(True)
        self.ss_toggle_button.clicked.connect(self.set_signal)
        self.ss_params_label.setBuddy(self.ss_toggle_button)

        self.ss_signal_form_combo_label = QLabel('Signal form',  self)
        self.ss_signal_form_combo = QComboBox(self)
        self.ss_signal_form_combo.addItems(signal_types)
        self.ss_signal_form_combo_label.setBuddy(self.ss_signal_form_combo)

        self.ss_frequency_spin = QSpinBox()
        self.ss_frequency_spin.setRange(0, 200_000)
        self.ss_frequency_spin.setValue(1)
        self.ss_frequency_label = QLabel('Frequency')
        self.ss_frequency_label.setBuddy(self.ss_frequency_spin)

        self.ss_amplitude_spin = QSpinBox()
        self.ss_amplitude_spin.setRange(0, 200_000)
        self.ss_amplitude_spin.setValue(1)
        self.ss_amplitude_label = QLabel('Amplitude')
        self.ss_amplitude_label.setBuddy(self.ss_amplitude_spin)

        self.ss_sample_rate_spin = QSpinBox()
        self.ss_sample_rate_spin.setRange(0, 200_000)
        self.ss_sample_rate_spin.setValue(440)
        self.ss_sample_rate_label = QLabel('Sample rate, Hz')
        self.ss_sample_rate_label.setBuddy(self.ss_sample_rate_spin)

        self.ss_duration_spin = QSpinBox()
        self.ss_duration_spin.setValue(5)
        self.ss_duration_label = QLabel('Duration, sec')
        self.ss_duration_label.setBuddy(self.ss_duration_spin)

        ss_params_layout = QVBoxLayout()

        ss_switch_layout = QHBoxLayout()
        ss_switch_layout.addWidget(self.ss_params_label)
        ss_switch_layout.addWidget(self.ss_toggle_button)

        ss_signal_form_layout = QHBoxLayout()
        ss_signal_form_layout.addWidget(self.ss_signal_form_combo_label)
        ss_signal_form_layout.addWidget(self.ss_signal_form_combo)

        ss_frequency_input_layout = QHBoxLayout()
        ss_frequency_input_layout.addWidget(self.ss_frequency_label)
        ss_frequency_input_layout.addWidget(self.ss_frequency_spin)

        ss_amplitude_input_layout = QHBoxLayout()
        ss_amplitude_input_layout.addWidget(self.ss_amplitude_label)
        ss_amplitude_input_layout.addWidget(self.ss_amplitude_spin)

        ss_sample_rate_input_layout = QHBoxLayout()
        ss_sample_rate_input_layout.addWidget(self.ss_sample_rate_label)
        ss_sample_rate_input_layout.addWidget(self.ss_sample_rate_spin)

        ss_duration_input_layout = QHBoxLayout()
        ss_duration_input_layout.addWidget(self.ss_duration_label)
        ss_duration_input_layout.addWidget(self.ss_duration_spin)

        self.formula_label = QLabel()

        ss_params_layout.addLayout(ss_switch_layout)
        ss_params_layout.addLayout(ss_signal_form_layout)
        ss_params_layout.addLayout(ss_frequency_input_layout)
        ss_params_layout.addLayout(ss_amplitude_input_layout)
        ss_params_layout.addLayout(ss_sample_rate_input_layout)
        ss_params_layout.addLayout(ss_duration_input_layout)

        params_layout = QHBoxLayout()
        params_layout.addLayout(fs_params_layout)
        params_layout.addLayout(ss_params_layout)

        plots_layout = QHBoxLayout()
        plots_layout.addWidget(self.signal_plot)
        plots_layout.addWidget(self.spectre_plot)

        self.receive_button = QPushButton('Receive')

        main_layout = QVBoxLayout()
        main_layout.addLayout(params_layout)
        main_layout.addLayout(plots_layout)
        main_layout.addWidget(self.formula_label)
        # main_layout.addWidget(self.receive_button)

        self.setLayout(main_layout)

        # self.receive_button.clicked.connect(self.set_signal)

        self.showMaximized()

    def set_signal(self):
        if not(self.fs_toggle_button.isChecked() or self.ss_toggle_button.isChecked()):
            self.signal_plot.clear()
            self.spectre_plot.clear()
            return

        self.formula_label.setText('Formula')
        self.formula_label.setWordWrap(True)

        fs_form_name = self.fs_signal_form_combo.currentText()
        fs_amplitude = self.fs_amplitude_spin.value()
        fs_frequency = self.fs_frequency_spin.value()
        fs_sample_rate = self.fs_sample_rate_spin.value()
        fs_duration = self.fs_duration_spin.value()

        ss_form_name = self.ss_signal_form_combo.currentText()
        ss_amplitude = self.ss_amplitude_spin.value()
        ss_frequency = self.ss_frequency_spin.value()
        ss_sample_rate = self.ss_sample_rate_spin.value()
        ss_duration = self.ss_duration_spin.value()

        if self.fs_toggle_button.isChecked():
            self.signal_plot.plot(fs_form_name, fs_amplitude, fs_frequency, fs_sample_rate, fs_duration)
            self.spectre_plot.plot(fs_form_name, fs_amplitude, fs_frequency, fs_sample_rate, fs_duration)

        if self.ss_toggle_button.isChecked():
            self.signal_plot.plot(ss_form_name, ss_amplitude, ss_frequency, ss_sample_rate, ss_duration)
            self.spectre_plot.plot(ss_form_name, ss_amplitude, ss_frequency, ss_sample_rate, ss_duration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
