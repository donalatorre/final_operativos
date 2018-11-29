from MemoriaAlloc import MemoriaAlloc

def prt(testMem):
   print testMem.ram.tabla
   print testMem.swap.tabla

testMem = MemoriaAlloc(4, 3)
prt(testMem)
testMem.accessPage(1, 2, testMem.prueba)
prt(testMem)
testMem.accessPage(3, 4, testMem.prueba)
prt(testMem)
testMem.accessPage(4, 7, testMem.prueba)
prt(testMem)
testMem.accessPage(5, 2, testMem.prueba)
prt(testMem)
testMem.accessPage(6, 8, testMem.prueba)
prt(testMem)
testMem.accessPage(7, 9, testMem.prueba)
prt(testMem)
testMem.accessPage(8, 0, testMem.prueba)
prt(testMem)
testMem.accessPage(4, 8, testMem.prueba)
prt(testMem)
testMem.accessPage(4, 10, testMem.prueba)
prt(testMem)
testMem.terminarProceso(4)
prt(testMem)
