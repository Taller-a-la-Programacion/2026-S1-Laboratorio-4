import Laboratorio4;
import pytest;
    
def test_eliminarPares_1():
    assert Laboratorio4.eliminarPares( [12, 78, 12, 0, 0, 12, 12] ) == []
    
def test_eliminarRepetidos_2():
    assert Laboratorio4.eliminarPares( [12, 5, 12] ) == [5]

def test_eliminarRepetidos_3():
    assert isinstance(Laboratorio4.eliminarPares([12, "5", 12] ), str) == isinstance("Error: Los valores deben ser enteros", str)

###############################################################
def test_sumaValoresPares_1():
    assert Laboratorio4.sumaValoresPares([0,2,3,4], [4, 8, 6, 0]) == [4,10,0,4]
    
def test_sumaValoresPares_2():
    assert Laboratorio4.sumaValoresPares([10, 0], [1,2]) == [0,2]
    
def test_sumaValoresPares_3():
    assert isinstance(Laboratorio4.sumaValoresPares([1,2], "dos"), str) == isinstance("Error: Los vectores no son del mismo tamaño", str)

######################################################################

def test_convertirBinario_1():
    assert Laboratorio4.convertirBinario([2,0]) == 10100

def test_convertirBase_2():
    assert Laboratorio4.convertirBinario([8,2,1]) == 1100100001

def test_convertirBase_3():
    assert isinstance(Laboratorio4.convertirBinario(20), str) == isinstance("Error: El parámetro debe ser una lista", str)
