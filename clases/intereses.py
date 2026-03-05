class Intereses(object):
    def __init__(self):
        self.cantidad=0
        self.interes=0
        self.años=0
        self.vf=0

    def leerdatos(self):
        self.cantidad = float(input("Ingrese la cantidad a invertir: "))
        self.interes = float(input("Ingrese el interés anual: "))
        self.años = int(input("Ingrese el número de años: "))

    def realizarcalculos(self):
        self.vf = self.cantidad * (self.interes+1)

    def mostrarresultados(self):
        print("Capital obtenido en la inversion cada año: ", self.vf)
    