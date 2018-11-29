class Memoria:
  def __init__(self, paginas):
    self.tabla = []
    for i in range(paginas):
      self.tabla.append(Row(1, 1, 1))
  
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
    return
  
  def eliminar(self, newRow):
    return

  def lru(self, newRow):
    return None

  def actualizarTiempo(newRow):
    return

  
class Row:
  def __init__(self, pid, pagina, tiempo):
    self.pid = pid
    self.pagina = pagina
    self.tiempo = tiempo

  def __repr__(self):
        return "(%d, %d, %d)\n" % (self.pid, self.pagina, self.tiempo)

  def __str__(self):
      return "(%d, %d, %d)" % (self.pid, self.pagina, self.tiempo)

  # def __str__(self):
  #   return "pid: " + str(self.pid) + " pagina: " + str(self.pagina)
  
