nombre=input("Por favor ingrese su nombre: ")
print("Bienvenido", nombre)

#Calculo de indice de masa corporal
#IMC= peso/estatura^2

#Leer estattura
estatura=input("ingrese su estatura en metros: ")
estatura=float(estatura)
#Leer peso
peso= input("ingrese su peso en Kilogramos: ")
peso=float(peso)
#Calcular IMC
imc= peso / estatura ** 2
#Mostrar IMC
print("Su IMC= ", imc)

if imc < 18.49:
   Condición= "Peso bajo"
else:
    if imc < 24.99:
        Condición= "Peso normal"
    else:
        if imc < 29.9:
            Condición= "Sobrepeso"
        else:
            if imc < 39.99:
                Condición= "Obesidad"
            else:
                Condición= "Obesidad Extrema"
print(Condición)
                
