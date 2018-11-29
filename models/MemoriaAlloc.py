from Memoria import Memoria, Row
class MemoriaAlloc:
   def __init__(self, limiteRam, limiteSwap):
     self.ram = Memoria(limiteRam)
     self.swap = Memoria(limiteSwap)
     self.prueba = 0

   def accessPage(self, pid, page, tActual):
     row = Row(pid, page, tActual)
     if not ram.hasRow(row):
       poner(row)
     prueba = prueba + 1
     ram.actualizarTiempo(row)
     
   def poner(self, row):
     swap.eliminar(row)
     marco = ram.lru(row)
     if marco != None:
       swap.insert(marco)

   def terminarProceso(self, pid):
     ram.eliminarProceso(pid)
     swap.eliminarProceso(pid)



