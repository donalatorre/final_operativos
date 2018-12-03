class Proceso:
   def __init__(self, pid, tamano, tLlegada):
    self.pid = pid
    self.accesos = 0
    self.pagefaults = 0
    self.tamano = tamano
    self.tLlegada = tLlegada
    self.tSalida = 0.0
    self.tCPU = 0.0
   
   def getRendimiento(self):
    if self.accesos == 0:
      return 0
    return 1.0 - float(self.pagefaults) / self.accesos

   def terminar(self, tSalida):
    self.tSalida = tSalida

   def getTurnAround(self):
    return self.tSalida - self.tLlegada

   def getTiempoEspera(self):
    return self.getTurnAround() - self.tCPU
