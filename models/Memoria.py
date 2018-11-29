class Memoria:
  def __init__(self, paginas):
    self.tabla = []
    self.limite = paginas
    for i in range(paginas):
      self.tabla.append(Row(-1, -1, -1))
  
  def __repr__(self):
    return "[{}]".format("".join(self.tabla))
        
  def __str__(self):
    return "[{}]".format("-".join(self.tabla))

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
        return True
    return False

  
class Row:
  def __init__(self, pid, pagina, tiempo):
    self.pid = pid
    self.pagina = pagina
    self.tiempo = tiempo

  def __repr__(self):
        return "(%d, %d, %d)\n" % (self.pid, self.pagina, self.tiempo)

  def __str__(self):
      return "(%d, %d, %d)" % (self.pid, self.pagina, self.tiempo)
  
