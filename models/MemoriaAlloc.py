from Memoria import Memoria, Row
class MemoriaAlloc:
   def __init__(self, limiteRam, limiteSwap):
     self.ram = Memoria(limiteRam)
     self.swap = Memoria(limiteSwap)
     self.prueba = 0

   def accessPage(self, pid, page, tActual):
     row = Row(pid, page, tActual)
     if not self.ram.hasRow(row):
       self.poner(row)
     self.prueba = prueba + 1
     self.ram.actualizarTiempo(row)
     
   def poner(self, row):
     self.swap.eliminar(row)
     marco = self.ram.lru(row)
     if marco != None:
       self.swap.insert(marco)

   def terminarProceso(self, pid):
     self.ram.eliminarProceso(pid)
     self.swap.eliminarProceso(pid)



