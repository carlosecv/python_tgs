from coche import Coche
from coche_volador import CocheVolador
c1 = Coche("verde",45)
c = CocheVolador('rojo', 60)
# print(c.color)
# print(c.ruedas)
# print(c.esta_volando)
# c.vuela()
# print(c.esta_volando)

# print("Mi coche: ",type(c1),"Mi volador:",type(c))

# print(isinstance(c1,Coche))
# print(isinstance(c,Coche))
print(issubclass(CocheVolador,Coche))
print(issubclass(Coche,CocheVolador))