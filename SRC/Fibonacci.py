N = int(input("Ingrese número de términos: "))
if N <= 0:
    print("No se imprimen términos.")
else:
    if N == 1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)
        cont=1

        while cont <= (N - 2):
            siguiente = a + b
            print(siguiente)
            a = b
            b = siguiente
            cont += 1

