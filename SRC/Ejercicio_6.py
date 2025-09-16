'''
def suma(a, b):
	resultado = a + b
	return resultado

# Ejercicio 1= crea una función que imprima la tabla de cualquier número bucle -for

def tabla(num):
    for i in range (1,11):
        producto = i * num
        print(f"{num} + {i} = {producto}")
#Esta función no tiene ningun retorno si no tiene explicitamente "return"


#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

numero = int(input("Ingrese un valor:"))
var= tabla(numero)
'''
# Ejercicio 1: Definir una funcion de menu que no tenga parametros de entrada y que imprima cuatro opciones diferentes y 
# solicite que elija una opción y la guarde en una variable.

def menu():
    print("1. Encabezado\n2. Opcion 2\n3. Opción 3\n4. Opcion 4")
    opc= int(input("Elija una opción: "))
    return opc

eleccion = menu()
print(f"Opción elegida: {eleccion}")

match(eleccion):
    case 1:
        mensaje = input("Ingrese una frase: ")
        def Encabezado(mensaje):
            print("Nombre: Ana sofía Cuéllar Lozano y mi ID es 000568112")
            print(mensaje)
            
        # Que imperima información sobre ustedes. Reciba un parametro: Mensaje que se imprime dentro de la función
    case 2:
        pass
        #Parametro 1: Valor total
        #Parametro 2: Porcentaje
        #Retorno: Valor de porcentaje
    case 3:
        pass
        #No recibe ningun parametro y no devuelve un resultado.
        #Imprime en pantalla un mensaje de cierre de programa