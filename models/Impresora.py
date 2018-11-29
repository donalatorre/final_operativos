from texttable import Texttable as hacerTabla

# imprimir status dando los datos
def imprimirStatus(timeStamp, pid, tamano):
    print (str(timestamp)," process", str(pid), " created", " size", str(tamano), "page")
# imprimir tabla al final
def imprimirResultados(comand, timeStamp, dirReal,colaListos, CPU, memoReal, areaSwap, processosTerminados)
    resultList = list()
    headerList = ["Comando","Timestamp","Dir. Real","Cola de listos","CPU","Memoria Real","Area de swapping","Procesos terminados",]
    datosList = [comand, timeStamp, dirReal,colaListos, CPU, memoReal, areaSwap, processosTerminados]
    resultList.append(datosList)
    tablaResultados = hacerTabla()
    tablaResultados.add_rows(resultList)
    print tablaResultados.draw()

    



