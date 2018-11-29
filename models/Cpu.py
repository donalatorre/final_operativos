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
		if(self.colaListos[0] == proceso):
			self.tLlegadaCpu = datetime.datetime.now().time()

	def Quantum(self):
		
		self.tTotalCpu = (datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.now().time()) - datetime.datetime.combine(datetime.datetime.today(), self.tLlegadaCpu)).total_seconds()
		self.tTotalCpu = round(self.tTotalCpu, 4)

		print(self.tTotalCpu)
		aux = self.colaListos.pop(0)
		aux.tCPU += self.tTotalCpu
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

				self.listaTerminados.append(x)
				self.colaListos.remove(x)

def main():
	test = Cpu(1)
	test.anadirProceso(proceso.Proceso("A", 1024, 0))
	test.anadirProceso(proceso.Proceso("B", 1024, 0))
	print(test.colaListos[0].pid)
	test.Quantum()
	print(test.colaListos[0].pid)
	test.terminarProceso("B")
	print(test.colaListos[0].pid)
	test.Quantum()
	print(test.colaListos[0].pid)
	

if __name__ == '__main__':
	main()