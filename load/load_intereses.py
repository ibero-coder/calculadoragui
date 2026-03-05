from PyQt5 import QtWidgets, uic
from clases.intereses import Intereses

class VentanaIntereses(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_intereses.ui", self)
        self.show()

        self.btnCalcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        capital = float(self.edit_capital.text())
        tasa_interes = float(self.edit_tasa.text())
        tiempo = float(self.edit_tiempo.text())
        intereses = Intereses()
        intereses.cantidad = capital
        intereses.interes = tasa_interes
        intereses.años = tiempo
        intereses.realizarcalculos()
        self.label_resultado.setText(str(intereses.vf))