import Central from Central

def prt(central):
   print central.memoriaAlloc.ram.tabla
   print central.memoriaAlloc.swap.tabla

central = Central(1.0, 30, 30, 10)

