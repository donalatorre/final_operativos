from models.Central import Central
from models.Cpu import Cpu
from models.Impresora import initTalba, agregarResultados, imprimirTabla
from models.Memoria import Memoria
from models.MemoriaAlloc import MemoriaAlloc
from models.Proceso import Proceso
import time
from models.InfoFinal import InfoFinal
initTime = -1.0

def actualProcess(inst, ret, data):
   dirReal = ""
   comando = ""
   tmstmp = ret
   if inst == "Create":
     ret += "Proceso " + str(central.pidContador) + " con tamano " + str(float(data[1]) / pageSize) + " paginas"
     comando = "Create " + str(central.pidContador)
     central.crearProceso(int(data[1]))
   elif inst == "Address":
     #print(data[1], data[2])
     comando = "Address " + data[1] + ", " + data[2]
     if central.cpu.procesoAtendido() == data[1]:
       if int(data[2]) >= central.cpu.colaListos[0].tamano:
         ret += "La direccion excede el tamano del proceso! Se va a ignorar la instruccion"
       else:
         dirReal = str(central.accederMemoria(int(data[1]), int(data[2])))
	 ret += "Memoria real " + dirReal
     else:
       ret += data[1] + " no se esta ejecutando. Se va a ignorar la instruccion"
   elif inst == "Quantum":
     ret += "Quantum End"
     comando = "Quantum"
     if not central.cpu.colaListos:
       ret += " CPU vacia. Se ignora"
     central.quantum()
   elif inst == "Fin":
     comando = "Finaliza " + data[1]
     ret += "Finalizando proceso " + str(data[1])
     central.matarProceso(int(data[1]))
   elif inst == "End":
     print imprimirTabla(resultList)
     finall = InfoFinal()
     for proc in central.cpu.colaListos:
       finall.agregar(proc)
     for proc in central.cpu.listaTerminados:
       finall.agregar(proc)
     finall.imprFinal()
   else:
     ret += inst
     return ret
   agregarResultados(comando, tmstmp, dirReal, central.cpu.imprimeListos(), central.cpu.procesoAtendido(), central.memoriaAlloc.ram, central.memoriaAlloc.swap, central.cpu.imprimeTerminados(), resultList)
   return ret

def handleMessage(data):
  data = data.split(" ")
  inst = data[0]
  global initTime
  ret = ""
  if inst == "QuantumV":
    global quantum
    quantum = float(data[1])
    ret += "Quantum recibido " + str(quantum) + " segundos"
  elif inst == "RealMemory":
    global realMemory
    realMemory = int(data[1])
    realMemory *= 1024
    ret += "Memoria real recibida " + str(realMemory)
  elif inst == "SwapMemory":
    global swapMemory
    swapMemory = int(data[1])
    swapMemory *= 1024
    ret += "Swap Memory recibida " + str(swapMemory)
  elif inst == "PageSize":
    global pageSize
    pageSize = int(data[1])
    pageSize *= 1024
    global resultList
    resultList = list()
    initTalba(resultList)
    global central
    central = Central(quantum, realMemory, swapMemory, pageSize)
    ret += "Tamano de pagina recibida " + str(pageSize)
  else:
    if initTime == -1.0:
      initTime = time.time()
    ret = str(round(time.time() - initTime, 3)) + " "
    ret = actualProcess(inst, ret, data)
  print ret
  return ret
