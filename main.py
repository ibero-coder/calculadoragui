from load.load_intereses import VentanaIntereses
from load.load_ventana_calculadora import VentanaCalculadora
from PyQt5 import QtWidgets
from load.load_km_millas import VentanaKmMillas
from load.load_farenheit import VentanaFarenheit
import sys

def main():
    app=QtWidgets.QApplication(sys.argv)
    ventana=VentanaFarenheit()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()