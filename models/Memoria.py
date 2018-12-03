class Memoria:
  def __init__(self, paginas):
    self.tabla = []
    self.limite = paginas
    for i in range(paginas):
      self.tabla.append(Row(-1, -1, -1))
  
  def __repr__(self):
    ret = ""
    for i, val in enumerate(self.tabla):
      ret += str(i) + ":" + str(self.tabla[i]) + "\n"
    if ret:
      ret = ret[0: len(ret) - 1]
    return ret
        
  def __str__(self):
    return self.__repr__()
  def hasRow(self, newRow):
    for row in self.tabla:
      if newRow.pid == row.pid and newRow.pagina == row.pagina:
        return True
    return False
  
  def insertar(self,newRow):
    for i in range(self.limite):
      if self.tabla[i].pid == -1:
        self.tabla[i] = newRow
        return True
    return False
    
  def eliminar(self, newRow):
    for i, row in enumerate(self.tabla):
      if newRow.pid == row.pid and newRow.pagina == row.pagina:
        self.tabla[i] = Row(-1,-1,-1)
        return True
    return False

  def eliminarProceso(self, newRow):
    somethingChanged = False
    for i, row in enumerate(self.tabla):
      if newRow.pid == row.pid:
        self.tabla[i] = Row(-1,-1,-1)
        somethingChanged = True
    return somethingChanged

  def lru(self, newRow):
    minIndex = 0
    minTiempo = self.tabla[0].tiempo
    for i, row in enumerate(self.tabla):
      if row.tiempo < minTiempo:
        minIndex = i
        minTiempo = row.tiempo
    oldRow = self.tabla[minIndex]
    self.tabla[minIndex] = newRow
    return oldRow

  def actualizarTiempo(self, newRow):
    for i, row in enumerate(self.tabla):
      if newRow.pid == row.pid and newRow.pagina == row.pagina:
        self.tabla[i] = newRow
        return i
    return -1

  
class Row:
  def __init__(self, pid, pagina, tiempo):
    self.pid = pid
    self.pagina = pagina
    self.tiempo = tiempo

  def __repr__(self):
    if self.pid == -1:
      return "L;"
    return "%d.%d;" % (self.pid, self.pagina)

  def __str__(self):
      if self.pid == -1:
	 return "L;"
      return "%d.%d;" % (self.pid, self.pagina)
  
