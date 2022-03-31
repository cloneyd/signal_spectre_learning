# This Python file uses the following encoding: utf-8
from PlotWidget import PlotWidget


from wave import (
    generate_sine_wave,
    generate_cosine_wave,
    generate_triangle_wave,
    generate_sawtooth_wave,
    generate_square_wave
)

wave_generators = {
    'sine': generate_sine_wave,
    'cosine': generate_cosine_wave,
    'triangle': generate_triangle_wave,
    'sawtooth': generate_sawtooth_wave,
    'square': generate_square_wave,
}


class SignalPlotWidget(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.axes.set_xlabel('Time, s')
        self.axes.set_ylabel('U, V')
        self.axes.grid(True)

    def plot(self, signal_name, amplitude, frequency, sample_rate, duration):
        self.clear()

        if signal_name == '-':
            return

        x, y = wave_generators[signal_name](amplitude, frequency, sample_rate, duration)

        self.axes.plot(x, y, color='#1f77b4')

        self.view.draw()
