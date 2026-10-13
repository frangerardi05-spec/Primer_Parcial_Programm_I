#---------------------------- Primer Parcial de Francisco Gerardi ----------------------------#

#Importo las funciones
import funciones
from funciones import mostrar_menu_principal
from funciones import generar_contrasenias
from funciones import buscar_contrasenias
from funciones import informar_estadisticas
from funciones import ordenar_contrasenias
from funciones import mostrar_contrasenias

from funciones import limpiar_teclado_os
#-----------------------------------------------------------#
# Variables a utilizar:
listas_contra_creadas = []
cant_contrasenias_total = 0

salida_bucle_principal = True

while salida_bucle_principal == True:
    mostrar_menu_principal()

    opcion = int(input("Elegir opción: "))

    while opcion != None:
        limpiar_teclado_os()
        match opcion:
    #-------------------------------------------#
    # case {1} que ejecuta la función que genera contraseñas
            case 1:
                while opcion != None:
                    print(f"Total de contraseñas creadas actualmente: {cant_contrasenias_total}\n")
                #-------------------------------------------#
                    cant_contrasenias = int(input("Cantidad de contraseñas a crear: "))
                    #-------------------------------------------#
                    if cant_contrasenias > 0:
                        cant_contrasenias_total += cant_contrasenias
                        generar_contrasenias(cant_contrasenias, listas_contra_creadas)
                        print("\n#--------------------------------------#\n")
                        print(f"Total de contraseñas creadas actualmente: {cant_contrasenias_total}\n")
                        print("Desea...\n")
                        primera_opcion = int(input("[1] Crear más contraseñas\n[2] Volver al menú principal\n\n--------> "))
                        print("\n#--------------------------------------#\n")
                        #-------------------------------------------#
                        while primera_opcion != 1 and primera_opcion != 2:
                            limpiar_teclado_os()
                            print("Seleccionar una opción válida.\n")
                            primera_opcion = int(input("[1] Crear más contraseñas\n[2] Volver al menú principal\n\n--------> "))
                        #-------------------------------------------#
                        if primera_opcion == 2:
                            opcion = None
                            limpiar_teclado_os()
                            print("#--------------------------------------#\nVolviendo al menú principal...")
                            break
                        limpiar_teclado_os()
                    #-------------------------------------------#
                    else:
                        print("\nLa cantidad de contraseñas a crear deben ser mayor a 0.")
                        print("\n#--------------------------------------#\n")
    #-------------------------------------------#
    # case {2} que ejecuta la función que valida y busca las contraseñas generadas
            case 2:
                if cant_contrasenias_total == 0:
                    print("#--------------------------------------#")
                    print("Todavía no se ha creado ninguna contraseña.\nPor favor seleccionar en el menú principal:" \
                    "\n\n------->   [1] Generar contraseñas\n")
                    break
                else:
                    print("Ingrese una contraseña para confirmar si existe en el sistema.\n")
                    contrasenia_a_buscar = input("Contraseña: ")
                    print("#--------------------------------------#")
                    buscar_contrasenias(contrasenia_a_buscar, listas_contra_creadas)
                    print("#--------------------------------------#")
                    vuelta_menu = input("Presionar {Enter} para volver al menú principal: ")
                    limpiar_teclado_os()
                    print("#--------------------------------------#\nVolviendo al menú principal...")
                break
    #-------------------------------------------#
    # case {3} que ejecuta la función que muestra las estadísticas de las contraseñas creadas
            case 3:
                if cant_contrasenias_total == 0:
                    print("#--------------------------------------#")
                    print("Todavía no se ha creado ninguna contraseña.\nPor favor seleccionar en el menú principal:" \
                    "\n\n------->   [1] Generar contraseñas\n")
                else:
                    while opcion != None:
                        informar_estadisticas(listas_contra_creadas, cant_contrasenias_total)
                        break
                    limpiar_teclado_os()
                    print("#--------------------------------------#\nVolviendo al menú principal...")
                break
    #-------------------------------------------#
    # case {4}
            case 4:
                #-------------------------------------------#
                if cant_contrasenias_total == 0:
                    print("#--------------------------------------#")
                    print("Todavía no se ha creado ninguna contraseña.\nPor favor seleccionar en el menú principal:" \
                    "\n\n------->   [1] Generar contraseñas\n")
                    break
                #-------------------------------------------#
                else:
                    orden = input("● Ascendente --> Asc\n● Descendente --> Desc\n\nDe que manera ordenar las listas: ")
                    limpiar_teclado_os()
                    print("#--------------------------------------#")
                    ordenar_contrasenias(listas_contra_creadas, orden)
                    print("Contraseñas creadas:\n")
                    mostrar_contrasenias(listas_contra_creadas)
                    #-------------------------------------------#
                    if orden == "asc":
                        orden = "Ordenado ascendentemente"
                    elif orden == "desc":
                        orden = "Ordenado descendentemente"
                    else:
                        orden = "Sin orden"
                    #-------------------------------------------#
                    print(f"\n{orden} | Cantidad de contraseñas creadas: {cant_contrasenias_total}")
                    print("#--------------------------------------#")
                    vuelta_menu = input("Presionar {Enter} para volver al menú principal: ")
                    limpiar_teclado_os()
                    print("#--------------------------------------#\nVolviendo al menú principal...")
                    break
    #-------------------------------------------#
    # case {5}
            case 5:
                salida_bucle_principal = False
                print("Saliendo del programa...")
                break
    #-------------------------------------------#
    # case {_} que ejecuta un bucle while() para cuando no se selecciona una de las opciones válidas
            case _:
                while opcion < 1 or opcion > 5:
                    print("""#--------------------------------------#
 Seleccionar una opción válida:
    1)  Generar contraseñas
    2)  Buscar contraseña
    3)  Informar estadísticas
    4)  Ordenar y mostrar contraseñas
    5)  Salir
#--------------------------------------#
                    """)
                    opcion = int(input("Elegir opción: "))
                    limpiar_teclado_os()
    #-------------------------------------------#    

#-----------------------------------------------------------#
