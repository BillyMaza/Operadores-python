import random
r1=int(input("Ingresa el número tope: "))
nsecret= random.randint(1,r1)
intentos=0
continuar=True
n=int(input("Ingresa el número secreto: "))
while n!=nsecret:
    if n>nsecret:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")
    n=int(input("Ingresa otro número porfavor: "))
    intentos+=1
print("Felicidades, encontraste el número secreto en ",intentos,"intentos")
continuar = False
            