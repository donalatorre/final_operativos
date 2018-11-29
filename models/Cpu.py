import proceso
import datetime

class Cpu:


	##quantum es un entero
	def __init__(self, quantum):
		self.quantumval = quantum
		self.colaListos = []
		self.listaTerminados = []
		self.tLlegadaCpu = 0
		self.tTotalCpu = 0


	##proceso es un objeto tipo proceso
	def anadirProceso(self, proceso):
		self.colaListos.append(proceso)
		if(self.colaListos[0].pid == proceso.pid):
			self.tLlegadaCpu = datetime.datetime.now().time()

	def Quantum(self):
		
		self.tTotalCpu = (datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.now().time()) - datetime.datetime.combine(datetime.datetime.today(), self.tLlegadaCpu)).total_seconds()
		self.tTotalCpu = round(self.tTotalCpu, 4)

		aux = self.colaListos.pop(0)
		aux.tCPU += self.tTotalCpu
		print("Tiempo en CPU de Proceso {}: {}".format(aux.pid, aux.tCPU))
		self.tLlegadaCpu = datetime.datetime.now().time()
		self.colaListos.append(aux)

	##pid es un string
	def terminarProceso(self, pid):
		for x in self.colaListos:
			if(x.pid == pid):
				if(self.colaListos[0] == x):
					self.tTotalCpu = (datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.now().time()) - datetime.datetime.combine(datetime.datetime.today(), self.tLlegadaCpu)).total_seconds()
					self.tTotalCpu = round(self.tTotalCpu, 4)
					x.tCPU += self.tTotalCpu
					print("Tiempo en CPU de Proceso {} al terminar: {}".format(x.pid, x.tCPU))
				
				self.listaTerminados.append(x)
				self.colaListos.remove(x)

	def __str__(self):
		CPU = "Proceso en CPU: {}".format(self.colaListos[0].pid)
		listos = "Procesos en cola de listos:"
		for x in range(len(self.colaListos) - 1, -1, -1):
			if(x == 0):
				listos += " {}".format(self.colaListos[x].pid)
			else:
				listos += " {},".format(self.colaListos[x].pid)

		terminados = "Procesos terminados:"
		for x in range(len(self.listaTerminados) - 1, -1, -1):
			if(x == 0):
				terminados += " {}".format(self.listaTerminados[x].pid)
			else:
				terminados += " {},".format(self.listaTerminados[x].pid)
		
		return CPU + "\n" + listos + "\n" + terminados

def main():
	test = Cpu(1)
	
	test.anadirProceso(proceso.Proceso("A", 1024, 0))
	test.anadirProceso(proceso.Proceso("B", 1024, 0))
	print(test)
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.Quantum()
	test.terminarProceso("B")
	print(test)

if __name__ == '__main__':
	main()
