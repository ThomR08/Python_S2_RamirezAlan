# Clase dia 4
# CustomRappi
# ###############

subTotal=0
print('Bienvenido a CustomRappi \n')
numHamb=int(input("Por favor ingrese cuantas hamburguesas desea: "))

for i in range(0,numHamb,1):

    opc=int(input("\nSeleccione el tipo de pan \n1. Pan de centeno ($1000) \n2. Pan de avena ($1500) \n\n"))
    if opc==1:
        subTotal=subTotal+1000
    else:
        if opc==2:
            subTotal=subTotal+1500
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")

    opc=int(input("\nSeleccione la cantidad de carne \n1. 250G ($5000) \n2. 300G ($7000)\n\n"))
    if opc==1:
        subTotal=subTotal+5000
    else:
        if opc==2:
            subTotal=subTotal+7000
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")

    opc=int(input("\nSeleccione la cantidad de pechuga asada \n1. 250G ($4500) \n2. 350G ($5500)\n\n"))
    if opc==1:
        subTotal=subTotal+4500
    else:
        if opc==2:
            subTotal=subTotal+5500
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")
    
        opc=int(input("\nSeleccione la cantidad de pollo desmechado \n1. 250G ($6500) \n2. 300G ($7500)\n\n"))
    if opc==1:
        subTotal=subTotal+6500
    else:
        if opc==2:
            subTotal=subTotal+7500
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")

        opc=int(input("\nSeleccione la cantidad de tocineta \n1. Una lonja ($1500) \n2. Dos lonjas ($2500)\n\n"))
    if opc==1:
        subTotal=subTotal+1500
    else:
        if opc==2:
            subTotal=subTotal+2500
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")


         opc=int(input("\nSeleccione el tipo de papa frita \n1. A la fracesa ($5000) \n2. En cascos ($6000)\n\n"))
    if opc==1:
        subTotal=subTotal+5000
    else:
        if opc==2:
            subTotal=subTotal+6000
        else:
            print("\nNo selecciono ninguna opcion, no se le añade el ingrediente")       

         opc=int(input("\nSeleccione la bebida \n1. Gaseosa ($5000) \n2. Cerveza Club Colombia ($8000) \n3. Naranjada ($9000)\n\n"))
    if opc==1:
        subTotal=subTotal+5000
    else:
        if opc==2:
            subTotal=subTotal+8000
        else:
            if opc==3:
               subTotal=subTotal+8000 
            else:
                print("\nNo selecciono ninguna opcion, no se le añade el ingrediente") 
  

#Desarrollado por: Alan Ramirez - T.I. 1096702159