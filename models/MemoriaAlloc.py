class MemoriaAlloc:
   def __init__(limiteRam, limiteSwap):
     ram = Memoria(limiteRam)
     swap = Memoria(limiteSwap)

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


     
