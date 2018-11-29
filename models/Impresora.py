from texttable import Texttable as hacerTabla

# imprimir status dando los datos
def imprimirStatus(timeStamp, pid, tamano):
    print (str(timestamp) + ", process, " + str(pid) + ", created," + " size," + str(tamano) + ", page")

#inicializar tabla
def initTalba(resultList):
	headerList = ["Comando","Timestamp","Dir. Real","Cola de listos","CPU","Memoria Real","Area de swapping","Procesos terminados"]
	resultList.append(headerList)
	return resultList

# agregar resultados a la tabla
def agregarResultados(comand, timeStamp, dirReal, colaListos, CPU, memoReal, areaSwap, processosTerminados, resultList):
    datosList = [str(comand), str(timeStamp), str(dirReal), str(colaListos), str(CPU), str(memoReal), str(areaSwap), str(processosTerminados)]
    resultList.append(datosList)
    return resultList
    
#imprimir tabla al final
def imprimirTabla(resultList):
	tablaResultados = hacerTabla()
	tablaResultados.add_rows(resultList)
	print tablaResultados.draw()

def main():
	resultList = list()
	initTalba(resultList)
	agregarResultados("Quantum", "1.000", "412", "C, B", "A", "0:A.0", "", "", resultList)
	agregarResultados("Quantum", "3.020", "512", "C", "B", "0:B.0", "", "A", resultList)
	imprimirTabla(resultList)
	

if __name__ == '__main__':
	main()