import time
class Central:
   def __init__(self, quantum, memoriaReal, memoriaSwap, pageSize):
     self.memoriaAlloc = MemoriaAlloc(memoriaReal / pageSize, memoriaSwap / pageSize)
     self.cpu = Cpu(quantum)
     self.pidContador = 1
     self.pageSize = pageSize

   def crearProceso(self, tamano):
     procesoNuevo = Proceso(pidContador, tamano, time.time())
     cpu.anadirProceso(procesoNuevo)
     pidContador = pidContador + 1

   def accederMemoria(self, pid, virtual):
     memoriaAlloc.accessPage(pid, virtual / pageSize, time.time())
   
   def matarProceso(self, pid):
     cpu.terminarProceso(pid)
     memoriaAlloc.terminarProceso(pid)
     
     
