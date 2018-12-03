from texttable import Texttable as hacerTabla

class InfoFinal:
  def __init__(self):
    self.headerResultado = [0, 0, 0, 0, 0, 0]

    self.resultList = []
    self.resultList.append(["Proceso", "Tiempo de CPU", "Tiempo de Turnaround", "Tiempo de espera", "Visitas a pagina", "Page faults", "Rendimiento"])
    self.globalList = []
    self.globalList.append(["Tiempo promedio de CPU", "Tiempo promedio de Turnaround", "Tiempo promedio de espera", "Visitas a pagina", "Page faults", "Rendimiento"])
  
  def agregar(self, proceso):
     self.resultList.append([str(proceso.pid), str(proceso.tCPU), str(proceso.getTurnAround()), str(proceso.getTiempoEspera()), str(proceso.accesos), str(proceso.pagefaults), str(proceso.getRendimiento())])
     
     self.headerResultado[0] += proceso.tCPU
     self.headerResultado[1] += proceso.getTurnAround()
     self.headerResultado[2] += proceso.getTiempoEspera()
     self.headerResultado[3] += proceso.accesos
     self.headerResultado[4] += proceso.pagefaults
     self.headerResultado[5] += proceso.getRendimiento()

  def imprFinal(self):
     total = len(self.resultList) - 1
     self.headerResultado[0] /= total
     self.headerResultado[1] /= total
     self.headerResultado[2] /= total
     self.headerResultado[5] = 1 - float(self.headerResultado[4]) / self.headerResultado[3]
     
     self.globalList.append(self.headerResultado)

     tablaResultados = hacerTabla()
     tablaResultados.add_rows(self.resultList)
     print tablaResultados.draw()

     otrosResultados = hacerTabla()
     otrosResultados.add_rows(self.globalList)
     print otrosResultados.draw()
