class KilometrosMillas(object):
    def __init__(self, km):
        self.km = km

    def convertir(self, millas):
        self.km = millas * 1.609344
        return self.km