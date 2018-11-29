class Proceso:
   def __init__(self, pid, tamano, tLlegada):
    self.pid = pid
    self.tamano = tamano
    self.tLlegada = tLlegada
    self.tSalida = 0
    self.tCPU = 0

   def terminar(tSalida):
    self.tSalida = tSalida

   def getTurnAround():
    return tSalida - tLlegada

   def getTiempoEspera():
    return getTurnAround() - tCPU
