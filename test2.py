class gato:
    comida='carne '
    def __init__(self):
        pass
    #@classmethod
    def saco(self, vendedor):
        return self.comida+vendedor

#morrongo=gato()
print(gato.saco('corina'))