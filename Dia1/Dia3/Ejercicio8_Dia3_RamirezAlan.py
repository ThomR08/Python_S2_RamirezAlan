# Clase día 3
# Area de un triangulo
# ##############

A=0
B=1
N=int(input("Ingrese la cantidad de términos: "))

print(A)
print(B)
for i in range(3,N+1,1):
    Siguiente=A+B
    print(Siguiente)
    A=B
    B=Siguiente

#Desarrollado por: Alan Ramirez - T.I. 1096702159