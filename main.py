from load.load_intereses import VentanaIntereses
from load.load_ventana_calculadora import VentanaCalculadora
from PyQt5 import QtWidgets
from load.load_km_millas import VentanaKmMillas
from load.load_farenheit import VentanaFarenheit
from load.load_menu_principal import MenuPrincipal
import sys

def main():
    app=QtWidgets.QApplication(sys.argv)
    ventana=MenuPrincipal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()