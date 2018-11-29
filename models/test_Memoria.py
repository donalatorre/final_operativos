from Memoria import Memoria
from Memoria import Row
t = Memoria(3)
row = Row(2,1,1)
print(t.tabla)
r = t.insertar(row)
print(r)
print(t.tabla)

row = Row(1,1,3)
r = t.actualizarTiempo(row)
print(r)
print(t.tabla)
