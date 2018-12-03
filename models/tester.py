from MemoriaAlloc import MemoriaAlloc

def prt(testMem):
   print testMem.ram
   print testMem.swap

testMem = MemoriaAlloc(4, 3)
prt(testMem)
testMem.accessPage(1, 2, 1)
prt(testMem)
testMem.accessPage(3, 4, 1)
prt(testMem)
testMem.accessPage(4, 7, 2)
prt(testMem)
testMem.accessPage(5, 2, 3)
prt(testMem)
testMem.accessPage(6, 8, 4)
prt(testMem)
testMem.accessPage(7, 9, 5)
prt(testMem)
testMem.accessPage(8, 0, 6)
prt(testMem)
testMem.accessPage(4, 8, 7)
prt(testMem)
testMem.accessPage(4, 10,8)
prt(testMem)
testMem.terminarProceso(4)
prt(testMem)
