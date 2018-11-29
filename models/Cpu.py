import proceso

class Cpu:


	##quantum es un entero
	def __init__(self, quantum):
		self.quantumval = quantum
		self.colaListos = []
		self.listaTerminados = []

	##proceso es un objeto tipo proceso
	def anadirProceso(self, proceso):
		self.colaListos.append(proceso)

	def Quantum(self):
		aux = self.colaListos.pop(0);
		self.colaListos.append(aux)

	##pid es un string
	def terminarProceso(self, pid):
		for x in self.colaListos:
			if(x.pid == pid):
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