# Clase día 3
# Promedio numeros
# ##############

suma=0
cantidad=int(input("Ingrese la cantidad de números: "))

for i in range(1,cantidad+1,1):
    numero=float(input("Ingrese un número: "))
    suma=suma+numero

promedio=suma/cantidad
print("El promedio es: ", promedio)

#Desarrollado por: Alan Ramirez - T.I. 1096702159