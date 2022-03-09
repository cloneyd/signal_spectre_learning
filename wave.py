import numpy as np
from scipy import signal


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


def generate_cosine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.cos((2 * np.pi) * frequencies)
    return x, y


def generate_triangle_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = signal.sawtooth((2 * np.pi) * frequencies, 0.5)
    return x, y


def generate_sawtooth_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = signal.sawtooth((2 * np.pi) * frequencies, 1)
    return x, y


def generate_square_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = signal.square((2 * np.pi) * frequencies)
    return x, y
