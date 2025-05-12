# Clase dia 6
#
# Diccionarios
# Terminar el ejercicio

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

booleanito = True
while(booleanito):
    print("#################")
    print("--- Librería de personas ---")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#################")
        print("--- Crear Persona ---")
        print("#################")
        diccionarioVacio={
    "id":int(input("Ingrese el ID de la nueva persona: ")),
    "nombre":str(input("Ingrese el Nombre de la nueva persona: ")),
    "apellido":str(input("Ingrese el Apellido de la nueva persona: ")),
    "edad":int(input("Ingrese la Edad de la nueva persona: ")),
}
        diccionarioVacio["telefonos"]=[]

        for i in range(0, int(input("Ingrese cuantos números telefonicos desea ingresar: "))):
            diccionarioVacio["telefonos"].append({f"codigo":int(input(f"Ingrese el Codigo del número {i+1} de la nueva persona: ")),"numero":int(input(f"Ingrese el Número {i+1} de la nueva persona: ")),"tipo":str(input(f"Ingrese el Tipo del número {i+1} de la nueva persona: "))})
        listaRobusta.append(diccionarioVacio)
        print(diccionarioVacio)
        print("=====================")
        print(listaRobusta)

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                print("#### - Tipo:",listaRobusta[i]["telefonos"][q]["tipo"])
                
                print("---------------------------")

            
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

