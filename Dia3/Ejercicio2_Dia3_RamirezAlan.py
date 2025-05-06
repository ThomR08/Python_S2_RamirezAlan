# Clase dia 3
# Mayor de tres
# ###################

num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))

if(num1>num2 and num1>num3):
    Mayor=num1
elif(num2>num3):
    Mayor=num2
else:
    Mayor=num3

print("El número mayor es: ",Mayor)

#Desarrollado por: Alan Ramirez - T.I. 1096702159