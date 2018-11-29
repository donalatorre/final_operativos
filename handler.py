from models.Central import Central
from models.Cpu import Cpu
# from models.Impresora import Impresora
from models.Memoria import Memoria
from models.MemoriaAlloc import MemoriaAlloc
from models.Proceso import Proceso

def handleMessage(data):
  data = data.split(" ")
  inst = data[0]
  if inst == "QuantumV":
    global quantum
    quantum = float(data[1])
    print(quantum)
    print(1)
  elif inst == "RealMemory":
    global realMemory
    realMemory = int(data[1])
    print("real memory")
    print(realMemory)
    print(2)
  elif inst == "SwapMemory":
    global swapMemory
    swapMemory = int(data[1])
    print(swapMemory)
    print(3)
  elif inst == "PageSize":
    pageSize = int(data[1])
    central = Central(quantum, realMemory, swapMemory, pageSize)
    print(central)
    print(4)
  elif inst == "Create":
    print(5)
  elif inst == "Address":
    print(6)
  elif inst == "Quantum":
    print(7)
  elif inst == "Fin":
    print(8)
  elif inst == "End":
    print(9)
  else:
    print(inst)