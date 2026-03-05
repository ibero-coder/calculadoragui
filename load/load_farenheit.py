from PyQt5 import QtWidgets, uic
from clases.farenheit import Farenheit

class VentanaFarenheit(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_farenheit.ui", self)
        self.show()

        self.btnConvertir.clicked.connect(self.botonConvertirClick)

    def botonConvertirClick(self):
        farenheit = float(self.edit_farenheit.text())
        farenheit_obj = Farenheit(farenheit)
        celsius = farenheit_obj.convertir_a_celsius()
        self.label_resultado.setText(str(celsius))