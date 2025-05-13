# Clase dia 6
#
# Diccionarios
# Terminar el ejercicio

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)
print("")
print("Bienvenido a la Librería de personas")
print("")
booleanito = True
while(booleanito):
    print("-----------------------------")
    print("--- Librería de personas ---")
    print("-----------------------------")
    print("")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica): "))
    print("")
    if(opcionUsuario==1):
        print("-----------------------------")
        print("--- Crear Persona ---")
        print("-----------------------------")
        diccionarioVacio={
    "id":int(input("Ingrese el ID de la nueva persona: ")),
    "nombre":str(input("Ingrese el Nombre de la nueva persona: ")),
    "apellido":str(input("Ingrese el Apellido de la nueva persona: ")),
    "edad":int(input("Ingrese la Edad de la nueva persona: ")),
}
        diccionarioVacio["telefonos"]=[]
        

        for i in range(0, int(input("Ingrese cuantos números telefonicos desea ingresar: "))):
            diccionarioVacio["telefonos"].append({f"codigo":int(input(f"Ingrese el Codigo del número {i+1} de la nueva persona: ")),"numero":int(input(f"Ingrese el Número {i+1} de la nueva persona: ")),"tipo":str(input(f"Ingrese el Tipo del número {i+1} de la nueva persona: "))})
            print("")
        listaRobusta.append(diccionarioVacio)
        

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("-----------------------------")
            print("--- Persona #",i+1," ---")
            print("-----------------------------")
            print("")
            print("Id:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print(f"Telefono #{q+1}:")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                print("#### - Tipo:",listaRobusta[i]["telefonos"][q]["tipo"])
            print("")
    elif(opcionUsuario==3):
        numBuscar = int(input("Ingresa el Id de la persona a mostrar: "))
        persona = next((i for i in listaRobusta if i["id"] == numBuscar), None)
        print("")
        if persona:
            print("-----------------------------")
            print("--- Persona encontrada ---")
            print("-----------------------------")
            print("")
            print("Id:", persona["id"])
            print("Nombre:", persona["nombre"])
            print("Apellido:", persona["apellido"])
            print("Edad:", persona["edad"])

            for q in range(len(persona["telefonos"])):
                print(f"Teléfono #{q+1}:")
                print("#### - Código:", persona["telefonos"][q]["codigo"])
                print("#### - Número:", persona["telefonos"][q]["numero"])
                print("#### - Tipo:", persona["telefonos"][q]["tipo"])
                print("")
        else:
            print("Persona no encontrada.")
            print("")
    elif(opcionUsuario==4):
        numBuscar = int(input("Ingresa el Id de la persona a editar: "))
        persona = next((i for i in listaRobusta if i["id"] == numBuscar), None)
        print("")
        if persona:
            print("-----------------------------")
            print("--- Persona encontrada ---")
            print("-----------------------------")
            print("")
            print("Acontinuación ingrese los nuevos valores de la persona:")
            print("")
            persona["id"]=int(input("Id: "))
            persona["nombre"]=str(input("Nombre: "))
            persona["apellido"]=str(input("Apellido: "))
            persona["edad"]=int(input("Edad: "))

            for q in range(len(persona["telefonos"])):
                print(f"Teléfono #{q+1}:")
                persona["telefonos"][q]["codigo"]=int(input("#### - Código: "))
                persona["telefonos"][q]["numero"]=int(input("#### - Número: "))
                persona["telefonos"][q]["tipo"]=str(input("#### - Tipo: "))
                print("")
            print("")
            print("*******************************")
            print("LOS DATOS HAN SIDO ACTUALIZADOS")
            print("*******************************")
            print("")
        else:
            print("Persona no encontrada.")
            print("")
                   
    elif(opcionUsuario==5):
        numBuscar = int(input("Ingresa el Id de la persona a eliminar: "))
        persona = next((i for i in listaRobusta if i["id"] == numBuscar), None)
        if persona:
            print("Estas seguro que quieres ELIMINAR a Id:", persona["id"], persona["nombre"], persona["apellido"])
            print("1. Sí")
            print("2. No")
            if int(input("Escoja una opción (Numérica): "))==1:
                listaRobusta.remove(persona)
                print("")
                print("La Persona ha sido ELIMINADA")
                print("")
            else:
                print("La Persona no se ha eliminado")
                print("")
        else:
            print("")
            print("Persona no encontrada.")
            print("")

    elif(opcionUsuario==6):
        print("Chaousssss")
        print("")
        booleanito=False
    else:
        print("No es una opción válida")
        print("")