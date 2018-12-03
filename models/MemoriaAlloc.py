from Memoria import Memoria, Row
class MemoriaAlloc:
   def __init__(self, limiteRam, limiteSwap):
     self.ram = Memoria(limiteRam)
     self.swap = Memoria(limiteSwap)
     #self.prueba = 0 #esta variable no existe, solamente se usa para fines de debugging

   def accessPage(self, pid, page, tActual):
     row = Row(pid, page, tActual)
     ret = 0
     if not self.ram.hasRow(row):
       self.poner(row)
       ret = 1
     #self.prueba = self.prueba + 1
     return (self.ram.actualizarTiempo(row), ret)
     
   def poner(self, row):
     self.swap.eliminar(row)
     marco = self.ram.lru(row)
     if marco != None:
       self.swap.insertar(marco)

   def terminarProceso(self, pid):
     row = Row(pid, 0, 0)
     self.ram.eliminarProceso(row)
     self.swap.eliminarProceso(row)



