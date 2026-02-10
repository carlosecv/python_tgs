class Coche:
    """Esta clase define el estado y el comportamiento de un coche"""

    ruedas = 4  # Atributo de clase

    def __init__(self, color, aceleracion):
        # Atributos de instancia
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v


vw = Coche("rojo",35)

print("Color:",vw.color,"Aceleracion:",vw.aceleracion)
print("Velocidad:",vw.velocidad)
vw.acelera()
print("Velocidad:",vw.velocidad)
vw.acelera()
print("Velocidad:",vw.velocidad)
vw.frena()
print("Velocidad:",vw.velocidad)