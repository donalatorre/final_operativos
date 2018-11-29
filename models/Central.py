import time
class Central:
   def __init__(quantum, memoriaReal, memoriaSwap, pageSize):
     self.memoriaAlloc = MemoriaAlloc(memoriaReal / pageSize, memoriaSwap / pageSize)
     self.cpu = Cpu(quantum)
     self.pidContador = 1

   def crearProceso(tamano):
     procesoNuevo = Proceso(pidContador, tamano, time.time())
     cpu.anadirProceso(procesoNuevo)
     pidContador = pidContador + 1

   
     
