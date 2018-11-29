import time
from Proceso import Proceso
from MemoriaAlloc import MemoriaAlloc
from Cpu import Cpu
class Central:
   def __init__(self, quantum, memoriaReal, memoriaSwap, pageSize):
     self.memoriaAlloc = MemoriaAlloc(memoriaReal / pageSize, memoriaSwap / pageSize)
     self.cpu = Cpu(quantum)
     self.pidContador = 1
     self.pageSize = pageSize
   
   def cargarPagina(self):
     if self.cpu.colaListos:
       self.memoriaAlloc.accessPage(self.cpu.colaListos[0].pid, 0, time.time())

   def quantum(self):
     self.cpu.Quantum()
     self.cargarPagina()

   def crearProceso(self, tamano):
     procesoNuevo = Proceso(pidContador, tamano, time.time())
     self.cpu.anadirProceso(procesoNuevo)
     self.cargarPagina()
     self.pidContador = self.pidContador + 1

   def accederMemoria(self, pid, virtual):
     self.memoriaAlloc.accessPage(pid, virtual / self.pageSize, time.time())
   
   def matarProceso(self, pid):
     self.cpu.terminarProceso(pid)
     self.memoriaAlloc.terminarProceso(pid)
     self.cargarPagina()
     
