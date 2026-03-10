from PyQt5 import QtWidgets, uic
from clases.calculadora import Calculadora
from load.load_ventana_calculadora import VentanaCalculadora
from load.load_farenheit import VentanaFarenheit
from load.load_km_millas import VentanaKmMillas
from load.load_intereses import VentanaIntereses

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()
        self.show()

        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionSalir.triggered.connect(self.salir)
        self.actionConvertir_Km_a_Millas.triggered.connect(self.ingresarKmMillas)
        self.actionConvertir_Farenheit_a_Celsius.triggered.connect(self.ingresarFarenheit)
        self.actionCalcular_intereses.triggered.connect(self.ingresarIntereses)
    
    def ingresarCalculadora(self):
        calculadora=VentanaCalculadora()
        calculadora.exec()
    
    def ingresarIntereses(self):
        intereses=VentanaIntereses()
        intereses.exec()
        
    def ingresarKmMillas(self):
        km_millas=VentanaKmMillas()
        km_millas.exec()
    
    def ingresarFarenheit(self):
        farenheit=VentanaFarenheit()
        farenheit.exec()
    

    def salir(self):
        self.close()


