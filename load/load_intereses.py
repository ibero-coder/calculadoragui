from PyQt5 import QtWidgets, uic
from clases.intereses import Intereses

class VentanaIntereses(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/intereses.ui", self)
        self.show()

        self.btnCalcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        capital = float(self.inputCantidad.text())
        tasa_interes = float(self.inputInteres.text())
        tiempo = float(self.inputAnios.text())
        intereses = Intereses()
        intereses.cantidad = capital
        intereses.interes = tasa_interes
        intereses.años = tiempo
        intereses.realizarcalculos()
        self.resultado.setText(str(intereses.vf))