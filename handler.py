from Central import Central
from Cpu import Cpu
from Impresora import Impresora
from Memoria import Memoria
from MemoriaAlloc import MemoriaAlloc
from Proceso import Proceso

def handleMessage(data):
  data = data.split(" ")
  inst = data[0]
  if inst == "RealMemory":
    print(1)
  elif inst == "SwapMemory":
    print(1)
  elif inst == "PageSize":
    print(1)
  elif inst == "Create":
    print(1)
  elif inst == "Address":
    print(1)
  elif inst == "Quantum":
    print(1)
  elif inst == "Fin":
    print(1)
  elif inst == "End":
    print(1)
  else:
    print(inst)