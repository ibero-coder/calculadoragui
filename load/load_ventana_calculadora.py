from PyQt5 import QtWidgets, uic
from clases.calculadora import Calculadora

class VentanaCalculadora(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_calculadora.ui", self)
        self.show()

        self.boton_sumar.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        numero1 = int(self.edit_numero1.text())
        numero2 = int(self.edit_numero2.text())
        calculadora=Calculadora(numero1, numero2)
        calculadora.sumar()
        self.label_resultado.setText(str(calculadora.resultado))

