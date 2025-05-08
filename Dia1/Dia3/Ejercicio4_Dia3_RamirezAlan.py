# Clase día 3
# Primo
# ##############

divisores=0

N=int(input("Ingrese un número: "))

for i in range(1,N+1,1):
    if(N%i==0):
        divisores=divisores+1

if(divisores==2):
    print("El número es primo.")
else:
    print("El número no es primo.")

#Desarrollado por: Alan Ramirez - T.I. 1096702159