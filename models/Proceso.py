class Proceso:
   def __init__(self, pid, tamano, tLlegada):
    self.pid = pid
    self.tamano = tamano
    self.tLlegada = tLlegada
    self.tSalida = 0
    self.tCPU = 0

   def terminar(self, tSalida):
    self.tSalida = tSalida

   def getTurnAround(self):
    return self.tSalida - self.tLlegada

   def getTiempoEspera(self):
    return self.getTurnAround() - self.tCPU
