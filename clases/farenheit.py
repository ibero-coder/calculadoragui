import math
class Farenheit(object):
    def __init__(self, farenheit):
        self.farenheit = farenheit

    def convertir_a_celsius(self):
        return (self.farenheit - 32) * (5 / 9)