from coche import Coche

class CocheVolador(Coche):
    ruedas = 6

    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando
    def vuela(self):
        self.esta_volando = True
    def aterriza(self):
        self.esta_volando = False

