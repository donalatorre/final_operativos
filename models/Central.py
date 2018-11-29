import time
class Central:
   def __init__(quantum, memoriaReal, memoriaSwap, pageSize):
     self.memoriaAlloc = MemoriaAlloc(memoriaReal / pageSize, memoriaSwap / pageSize)
     self.cpu = Cpu(quantum)
     self.pidContador = 1
     self.pageSize = pageSize

   def crearProceso(tamano):
     procesoNuevo = Proceso(pidContador, tamano, time.time())
     cpu.anadirProceso(procesoNuevo)
     pidContador = pidContador + 1

   def accederMemoria(pid, virtual):
     memoriaAlloc.accessPage(pid, virtual / pageSize, time.time())
   
   def matarProceso(pid):
     cpu.terminarProceso(pid)
     memoriaAlloc.terminarProceso(pid)
     
     
