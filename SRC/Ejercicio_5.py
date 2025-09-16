#En el ciclo for se usa la función range que determina el número de intervalor en el ciclo para que se ejecute con cada
#número que aparece en el ciclo:

#Ejemplo:
'''
for i in range(0,-21,-1):
    print(i)
'''
# Siendo el primer numero en el range el inicio de la secuencia, el segundo el número al que queremos llegar dado por el
# número al que realmente se quiere llegar menos 1, y el tercero el número por el cuál se incrementa.

#Ejemplo 1:
'''
mensaje = "Programación en Phyton."

numero = int(input("Ingrese el número: "))

for i in range(numero):
    print(mensaje)
'''
#Ejercicio 1: Calcular la suma de todos los números pares desde 0 hasta el numero qaue ingrese el usuario
# y mostrar el resultado en la pantalla.
'''
numero = int(input("Ingrese un número positivo:"))
acumulador = 0
if numero <= 0:
    print("El número debe ser positivo.")
else:
    for i in range(0,numero+1,2):
        acumulador += i
    print(acumulador)
'''
#Ejemplo 2: Se tiene la siguiente secuencia en filas y columnas:
#1
#1 2
#1 2 3
#1 2 3 4 
#1 2 3 4 5

# genere un programa que implrima la secuencia el numero de veces que diga el usuario

#Solución:

# Tenemos 2 variables:

#   i           j
#  1 hasta n    1 hasta i y así sucesivamente.

# Entonces el código es:

numero = int(input("Ingrese el número entero positivo: "))

for i in range(1,numero+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

