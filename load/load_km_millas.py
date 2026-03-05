from PyQt5 import QtWidgets, uic
from clases.km_millas import KilometrosMillas

class VentanaKmMillas(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_km_millas.ui", self)
        self.show()

        self.btnConvertir.clicked.connect(self.botonConvertirClick)

    def botonConvertirClick(self):
        millas = float(self.edit_millas.text())
        km_millas = KilometrosMillas(0)
        km = km_millas.convertir(millas)
        self.label_resultado.setText(str(km))