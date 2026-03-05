from load.load_intereses import VentanaIntereses
from load.load_ventana_calculadora import VentanaCalculadora
from PyQt5 import QtWidgets
import sys

def main():
    app=QtWidgets.QApplication(sys.argv)
    ventana=VentanaIntereses()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()