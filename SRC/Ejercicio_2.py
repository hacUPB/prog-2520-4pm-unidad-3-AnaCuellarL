# Determinar si un número es par o impar

#Leer Número

numero = int(input("Ingrese un número entero: "))
residuo = numero % 2

#Si residuo es 0 es par

if residuo == 0:
    print(numero, "es par")
else:
    print(numero,"Es impar")
