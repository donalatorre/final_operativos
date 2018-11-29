import time
from Proceso import Proceso
class Central:
   def __init__(self, quantum, memoriaReal, memoriaSwap, pageSize):
     self.memoriaAlloc = MemoriaAlloc(memoriaReal / pageSize, memoriaSwap / pageSize)
     self.cpu = Cpu(quantum)
     self.pidContador = 1
     self.pageSize = pageSize

   def crearProceso(self, tamano):
     procesoNuevo = Proceso(pidContador, tamano, time.time())
     self.cpu.anadirProceso(procesoNuevo)
     self.pidContador = self.pidContador + 1

   def accederMemoria(self, pid, virtual):
     self.memoriaAlloc.accessPage(pid, virtual / self.pageSize, time.time())
   
   def matarProceso(self, pid):
     self.cpu.terminarProceso(pid)
     self.memoriaAlloc.terminarProceso(pid)
     
     
