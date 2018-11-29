from Memoria import Memoria
class MemoriaAlloc:
   def __init__(self, limiteRam, limiteSwap):
     self.ram = Memoria(limiteRam)
     self.swap = Memoria(limiteSwap)

   def accessPage(pid, page, tActual):
     row = Row(pid, page, tActual)
     if not ram.hasRow(row):
       poner(row)
     ram.actualizarTiempo(row)
     
   def poner(row):
     swap.eliminar(row)
     marco = ram.lru(row)
     if marco != None:
       swap.insert(marco)

   def terminarProceso(pid):
     ram.eliminarProceso(pid)
     swap.eliminarProceso(pid)

testMem = MemoriaAlloc(4, 3)
