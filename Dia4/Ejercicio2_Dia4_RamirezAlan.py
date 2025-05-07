# Clase dia 4
# Sueldo mayor y menor
# ###############

cantidad=int(input("¿Cuántos empleados quieres ingresar? :"))

auxEmpleado=str(input("Ingresa el nombre del empleado 1: "))
auxHoras=int(input("Ingresa el numero de horas trabajadas de ", auxEmpleado, ": "))

horasMayor=auxHoras
empleadoMayor=auxEmpleado
horasMenor=auxHoras
empleadoMenor=auxEmpleado
horasSuma=auxHoras

for i in range(2,cantidad+1,1):
    auxEmpleado=str(input("Ingresa el nombre del empleado ", i, ": "))
    auxHoras=int(input("Ingresa el numero de horas trabajadas de ", auxEmpleado, ": "))

horasSuma=horasSuma+auxHoras

 if(auxHoras>horasMayor):
        horasMayor=auxHoras
        empleadoMayor=auxEmpleado
if(auxHoras<horasMenor):
        horasMenor=auxHoras
        empleadoMenor=auxEmpleado

SueldoBMayor=horasMayor*20000
epsMayor=SueldoBMayor*0.04
pensionMayor=SueldoBMayor*0.04
sueldoNMayor=SueldoBMayor-epsMayor-pensionMayor

SueldoBMenor=horasMenor*20000
epsMenor=SueldoBMenor*0.04
pensionMenor=SueldoBMenor*0.04
sueldoNMenor=SueldoBMenor-epsMenor-pensionMenor

promedioHoras=horasSuma/cantidad

print("")
print("---------------------------------------")
print("")
print("Empleado que mas gana y el empleado que menos gana")
print("")
print("---------------------------------------")


#Desarrollado por: Alan Ramirez - T.I. 1096702159