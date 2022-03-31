# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)
from PySide6.QtCore import Slot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


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

    def clear(self):
        if len(self.axes.lines):
            self.axes.lines[0].remove()
            self.view.draw()
