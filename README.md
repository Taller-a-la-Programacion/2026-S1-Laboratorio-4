# 2026 S2 Laboratorio 4

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio4.py**
- No olvidar hacer los comentarios y validaciones respectivas

## Ejercicio 1. Valor 10 puntos.
Escriba una función llamada **eliminarPares** que reciba como parámetro de entrada una lista con elementos enteros y eliminar si un elemento de esta lista en **Par**. 

```python
>>> eliminarPares( [12, 78, 12, 0, 0, 12, 12] )
[]
>>> eliminarPares( [12, 5, 12] )
[5]
```

## Ejercicio 2. Valor 10 puntos.
Escriba una función **sumaValoresPares (vector1, vector2)** que reciba dos vetores de números enteros, y retorne un nuevo vector que contenga la suma de las posiciones con valores pares de los dos vectores y donde no cumpla esta condición retornará un **CERO**. No puede usar len (), solo puede recorrer el vector una vez. La función debe comportarse de la siguiente manera:

```python
>>> sumaValoresPares([0,2,3,4], [4, 8, 6, 0])
[4,10,0,4]
>>> sumaValoresPares([10, 0], [1,2])
[0,2]
 >>> sumaValoresPares([1,2], [1,2,3])
 "Error: Los vectores no son del mismo tamaño"
 ```

## Ejercicio 3. Valor 10 puntos.
Escriba una función llamada **convertirBinario** que reciba como parámetro de entrada una lista con diferentes dígitos enteros. El resultado a retornar será su representación en binario

```python
>>> convertirBinario( [2,0] )
10100
>>> convertirBase( [8,2,1])
1100100001

```
