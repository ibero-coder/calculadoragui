from PyQt5 import QtWidgets, uic
from clases.farenheit import Farenheit

class VentanaFarenheit(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/farenheit.ui", self)
        self.show()

        self.btnConvertir.clicked.connect(self.botonConvertirClick)

    def botonConvertirClick(self):
        fahrenheit = float(self.inputFahrenheit.text())
        fahrenheit_obj = Farenheit(fahrenheit)
        celsius = fahrenheit_obj.convertir_a_celsius()
        self.resultadoCelsius.setText(str(celsius))