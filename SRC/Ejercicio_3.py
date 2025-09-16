print(10 > 5)
print("Hola" != "Mundo")
print(3.14 <= 4.5)
nombre = "Juan"
print(nombre == "Juan")
print("buñuelo" == "Pizza")
print(25>50)
operacion= 20+3
print(operacion<20)

# Ejercicio:

# Condicional simple:
 # Resuelve el siguiente problema usando el condicional simple. 
 # Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
#Solución:

envio = 0
compra = int(input("Ingrese el valor de la compra>> "))
if compra < 100000:
	envio = 9000
total = compra + envio
print(f"El total de la compra es {total}")

# Condicional multiple:

# Ejercicio: Una compañía de paquetería internacional tiene servicio en algunos países según su zona.
#  El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. 
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad.

#Solución:

zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un número:"))

if zona > 0 and zona <= 5:
	peso = int(input("Ingrese el peso del paquete en gramos: "))
	if peso <= 5000:
		if zona == 1:
			total = peso * 11
		elif zona == 2:
			total = peso * 10
		elif zona == 3:
			total = peso * 12
		elif zona == 4:
			total = peso * 24
		elif zona == 5:
			total = peso * 27
		print(f"El envío de su paquete cuesta ${total}. ")
	else:
		print("No se pueden enviar paquetes de mas de 5Kg")
else:
	print("La zona ingresada no existe")
