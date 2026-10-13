#---------------------------- Primer Parcial de Francisco Gerardi ----------------------------#

#-----------------------------------------------------------#
# 1 | Generar contraseñas

def generar_contrasenias(cant_contrasenias:int, lista_contra_creadas:list):
    """
    Función que genera contraseñas aleatorias que cumplan con dos condiciones:
    \n1| Que tengan estas 3 otras condiciones (esto se logra gracias a otra función dentro de esta):
        a) Tener al menos una mayúscula
        b) Tener al menos una minúscula
        c) Tener al menos un número entero del 0-9
    2| Que tengan una longitud de 8 a 15 (Incluidos ambos) en total.
    
    Tiene dos parámetros, la cantidad de contraseñas a crear, y la lista donde se guardan:
            cant_contrasenias (int) |   lista_contra_creadas (list)
    """
    from funciones import confirmar_caracteres_contrasenia
    import random
    #-------------------------------------------#
    contrasenia_nueva = ""
    for i in range (0, cant_contrasenias):
        while (confirmar_caracteres_contrasenia(contrasenia_nueva) == False and
               contrasenia_nueva == lista_contra_creadas[i]):
            contrasenia_nueva = ""
            for j in range (0, random.randint(8, 15)):
                num_random = (random.randint(1,3))
                if num_random == 1:
                    contrasenia_nueva += (chr(random.randint(48, 57)))
                elif num_random == 2:
                    contrasenia_nueva += (chr(random.randint(65, 90)))
                elif num_random == 3:
                    contrasenia_nueva += (chr(random.randint(97, 122)))
        lista_contra_creadas += [contrasenia_nueva]
        contrasenia_nueva = ""
    #-------------------------------------------#

#-------#
# 1 (bis) | Asegurarse que las contraseñas creadas cumplan con las 3 condiciones:
#         |     1) Tener al menos una mayúscula
#         |     2) Tener al menos una minúscula
#         |     3) Tener al menos un número entero del 0-9

def confirmar_caracteres_contrasenia(contrasenia_nueva:str)->bool:
    """
    Función que confirma si las contraseñas creadas en la función {generar_contrasenias}contienen al menos:
        - Una mayúscula
        - Una minúscula
        - Un número entero entre el 0-9
    
    Como parámetro tiene la contraseña creada: contrasenia_nueva (str)

    Retorna un bool que confirma si se cumplen o no las 3 condiciones: triple_condicion (bool)
    """
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    triple_condicion = False
    #-------------------------------------------#
    for i in contrasenia_nueva:
        caracter = ord(i)
        if caracter >= 65 and caracter <= 90:
            tiene_mayus = True
        elif caracter >= 97 and caracter <= 122:
            tiene_minus = True
        elif caracter >= 48 and caracter <= 57:
            tiene_num = True
    #-------------------------------------------#
    if tiene_mayus == True and tiene_minus == True and tiene_num == True:
        triple_condicion = True
    #-------------------------------------------#
    return triple_condicion

#-----------------------------------------------------------#
# 2 | Buscar contraseña

def buscar_contrasenias(contrasenia_a_buscar:str, lista_contra_creadas:list):
    """
    Función que busca y valida contraseñas ingresadas por el usuario. Si existen o no en el programa, esta función lo comunica

    Pide dos parámetros, la contraseña ingresada por el usuario, y la lista con las contraseñas creadas aleatoriamente:
        contrasenia_a_buscar (str)  |   lista_contra_creadas (list)
    """
    #-------------------------------------------#
    from funciones import confirmar_caracteres_contrasenia
    contrasenia_existe_en_programa = False
    formato_valido = False
    #-------------------------------------------#
    if (confirmar_caracteres_contrasenia(contrasenia_a_buscar) == True) and (
        len(contrasenia_a_buscar) >= 8 and len(contrasenia_a_buscar) <= 15):
        formato_valido = True
    #-------------------------------------------#
    if formato_valido == False:
        print("""La contraseña ingresada debe cumplir con las siguientes condiciones:
        1| Que tengan estas 3 otras condiciones (esto se logra gracias a otra función dentro de esta):
            a) Tener al menos una mayúscula
            b) Tener al menos una minúscula
            c) Tener al menos un número entero del 0-9
        2| Que tenga una longitud de 8 a 15 (Incluidos ambos) caracteres en total.""")
    #-------------------------------------------#
    elif formato_valido == True:
        for i in lista_contra_creadas:
            if contrasenia_a_buscar == i:
                contrasenia_existe_en_programa = True
                break
        if contrasenia_existe_en_programa == True:
            print("La contraseña ingresada existe en el sistema.\nAcceso Concedido.")
        elif contrasenia_existe_en_programa == False:
            print("La contraseña ingresada no existe en el sistema.\nAcceso Denegado.")
    #-------------------------------------------#

#-----------------------------------------------------------#
# 3 | Informar estadísticas: 
# El sistema deberá informar estadísticas sobre las contraseñas almacenadas. 
# Se deberá mostrar: 
#   a) Porcentaje de contraseñas por cantidad de caracteres, por ejemplo: 
#       8 caracteres: 12% 
#       9 caracteres: 8% 
#       10 caracteres: 5% 
#       11 caracteres: 9% 
#       … 
#       15 caracteres: 11%

#   b) Promedios: 
#       - Longitud promedio de las contraseñas almacenadas. 
#       - Promedio de caracteres mayúsculas. 
#       - Promedio de caracteres minúsculas. 
#       - Promedio de caracteres numéricos. 

#   c) Informar la cantidad de contraseñas donde los caracteres que la componen no se repiten 
#       (son únicos) y mostrarlas. 

def informar_estadisticas(lista_contra_creadas:list, cant_contrasenias:int):
    """
    Función que informa sobre determinadas estadísticas de la generación de contraseñas.

    Recibe dos parámetros, una es la lista con las contraseñas creadas y otra con la cantidad de las mismas:
        lista_contra_creadas (list) | cant_contrasenias (int)
    """
    #-------------------------------------------#
    # Declaro Variables
    lista_tipos_contrasenias = [0, 0, 0, 0, 0, 0, 0, 0]
    total_caracteres = 0
    total_mayusculas = 0
    total_minusculas = 0
    total_numeros = 0
    contrasenias_unicas = []
    contrasenia_sin_char_repetido = True
    #-------------------------------------------#
    # Bucle for donde yace todas las iteraciones a utilizar en las estadísticas
    for contrasenia in lista_contra_creadas:
        contrasenia_sin_char_repetido = True
        longitud_contrasenia = len(contrasenia)
        lista_tipos_contrasenias[longitud_contrasenia - 8] += 1
        total_caracteres += longitud_contrasenia
        #-------------------------------------------#
        for primer_caracter_contrasenia in range (0, longitud_contrasenia - 1):
            for segundo_caracter_contrasenia in range(primer_caracter_contrasenia + 1, longitud_contrasenia):
                if contrasenia[primer_caracter_contrasenia] == contrasenia[segundo_caracter_contrasenia]:
                    contrasenia_sin_char_repetido = False
        #-------------------------------------------#
        for caracter in contrasenia:
            caracter_ascii = ord(caracter)
            if caracter_ascii >= 65 and caracter_ascii <= 90:
                total_mayusculas += 1
            elif caracter_ascii >= 97 and caracter_ascii <= 122:
                total_minusculas += 1
            elif caracter_ascii >= 48 and caracter_ascii <= 57:
                total_numeros += 1
        #-------------------------------------------#
        if contrasenia_sin_char_repetido == True:
            contrasenias_unicas += [contrasenia]

    #-------------------------------------------#
    # Mini menú para mostrar las estadísticas

    # Bandera sin importancia que utiliza para generar el bucle while()
    salida_bucle_estadistica = True
    # Bucle while() que encierra todo el menú de estadísticas
    while salida_bucle_estadistica == True:
        print("""Informando sobre las estadísticas...
#--------------------------------------#
            Menú estadísticas
#--------------------------------------#
[a] Porcentaje de contraseñas por cantidad de caracteres
[b] Promedios: 
        1) Longitud promedio de las contraseñas almacenadas 
        2) Promedio de caracteres mayúsculas
        3) Promedio de caracteres minúsculas
        4) Promedio de caracteres numéricos
[c] Cantidad de contraseñas donde los caracteres que las componen no se repiten
[d] Volver al Menú Principal
#--------------------------------------#""")
        eleccion_estadística = str(input("Estadística a mostrar: "))
        print("#--------------------------------------#")
        #-------------------------------------------#
        eleccion_estadística = cambiar_mayusculas_minusculas(eleccion_estadística)
        #-------------------------------------------#
        if ((eleccion_estadística != 'a') and (eleccion_estadística != 'b') and 
            (eleccion_estadística != 'c') and (eleccion_estadística != 'd')):
            limpiar_teclado_os()
            while (eleccion_estadística != "a" and eleccion_estadística != "b" and
                    eleccion_estadística != "c" and eleccion_estadística != "d"):
                limpiar_teclado_os()
                print("""#--------------------------------------#
Seleccionar una opción válida.
#--------------------------------------#
            Menú estadísticas
#--------------------------------------#
[a] Porcentaje de contraseñas por cantidad de caracteres
[b] Promedios: 
        1) Longitud promedio de las contraseñas almacenadas 
        2) Promedio de caracteres mayúsculas
        3) Promedio de caracteres minúsculas
        4) Promedio de caracteres numéricos
[c] Cantidad de contraseñas donde los caracteres que las componen no se repiten
[d] Volver al Menú Principal
#--------------------------------------#""")
                eleccion_estadística = str(input("Elegir que estadística mostrar: "))
                eleccion_estadística = cambiar_mayusculas_minusculas(eleccion_estadística)
                print("#--------------------------------------#")
        #-------------------------------------------#
        if eleccion_estadística == "a":
            #-------------------------------------------#
            # Inciso {a}: Porcentaje de contraseñas por cantidad de caracteres.
            for i in range(0, 8):
                i_caracteres = i + 8
                porcentaje_contrasenias = ((lista_tipos_contrasenias[i] * 100) / cant_contrasenias)
                print(f"Porcentaje de contraseñas con {i_caracteres} caracteres = {porcentaje_contrasenias} %" \
                    f" -----> Cantidad = {lista_tipos_contrasenias[i]}/{cant_contrasenias}")
            print("#--------------------------------------#")
            vuelta_menu_estadistica = input("Presionar {Enter} para volver al menú de estadísticas: ")
        #-------------------------------------------#
        elif eleccion_estadística == "b":
            #-------------------------------------------#
            # Inciso {b}: Promedios: 
            #       a) Longitud promedio de las contraseñas almacenadas. 
            #       b) Promedio de caracteres mayúsculas. 
            #       c) Promedio de caracteres minúsculas. 
            #       d) Promedio de caracteres numéricos.
            a = total_caracteres / cant_contrasenias
            print(f"1) El promedio de longitud es de {a} caracteres por contraseña almacenada.")
            b = total_mayusculas / cant_contrasenias
            print(f"2) El promedio de caracteres en mayúsculas es de {b} por contraseña almacenada.")
            c = total_minusculas / cant_contrasenias
            print(f"3) El promedio de caracteres en minúsculas es de {c} por contraseña almacenada.")
            d = total_numeros / cant_contrasenias
            print(f"4) El promedio de caracteres númericos enteros positivos es de {d} por contraseña almacenada.")
            print("#--------------------------------------#")
            vuelta_menu_estadistica = input("Presionar {Enter} para volver al menú de estadísticas: ")
        #-------------------------------------------#    
        elif eleccion_estadística == "c":
        #-------------------------------------------#
            # Inciso {c}: Informar la cantidad de contraseñas donde 
            #             los caracteres que las componen no se repiten (son únicos) y mostrarlas.
            cant_contras_unicas = len(contrasenias_unicas)
            print(f"{cant_contras_unicas}/{cant_contrasenias} son la cantidad de contraseñas" \
                " donde los caracteres que las componen no se repiten.\nY son:")
            for i in range(0, cant_contras_unicas):
                print(f"{contrasenias_unicas[i]}") 
            print("#--------------------------------------#")
            vuelta_menu_estadistica = input("Presionar {Enter} para volver al menú de estadísticas: ")
        #-------------------------------------------#
        elif eleccion_estadística == "d":
            break
        #-------------------------------------------#
        limpiar_teclado_os()

#-----------------------------------------------------------#
# 4 (1/2) | Ordenar contraseñas

def ordenar_contrasenias(lista_contra_creadas:list, orden:str):
    """
    Función que tiene como objetivo el ordenar la lista con las contraseñas creadas, en base a los gustos del usuario (asc | desc).

    Recibe dos parámetros: listas_contra_creadas (list) | orden (str)
    """
    from funciones import cambiar_mayusculas_minusculas
    #-------------------------------------------#
    cambiar_mayusculas_minusculas(orden)
    #-------------------------------------------#
    if orden == "asc":
        orden = True
    elif orden == "desc":
        orden = False
    else:
        orden = None
    #-------------------------------------------#
    if orden != None:
        for i in range(len(lista_contra_creadas)-1):
            for j in range(i+1, len(lista_contra_creadas)):
                if (orden == True and ((lista_contra_creadas[i] > lista_contra_creadas[j]) or
                                    (lista_contra_creadas[i] == lista_contra_creadas[j])) or
                    orden == False and ((lista_contra_creadas[i] < lista_contra_creadas[j]) or
                                    (lista_contra_creadas[i] == lista_contra_creadas[j]))):
                    intercambiar_elementos(lista_contra_creadas, i, j)
    elif orden == None:
        print("Sin aclarar el ordenamiento de forma Ascendente o Descendente," \
              " las contraseñas se mostrarán en base al orden de creación.")

#-------#
# 4 (2/2) | Mostrar contraseñas

def mostrar_contrasenias(lista_contra_creadas:list):
    """
    Función que tiene como objetivo el mostrar, de forma que sea entendible para el usuario,
    la lista con las contraseñas creadas.
    
    Recibe un parámetro: lista_contra_creadas (list)
    """
    for i in range(0, len(lista_contra_creadas)):
        print(f"{lista_contra_creadas[i]}")

#-----------------------------------------------------------#
# Función para limpiar el teclado
def limpiar_teclado_os()->None:
    """
    Objetivo: Función con el {import os} que al convocarlo sirve para limpiar el teclado según el OS del usuario sin necesidad de repetir código.
    """
    import os 

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#-----------------------------------------------------------#
# Función para intercambiar elementos de una lista
def intercambiar_elementos(lista:list, i:int, j:int)-> None:
    """Intercambia dos valores (elementos) a traves de los indices en una misma lista.


    La lista que almacena los elementos a intercambiar, la i, j son los indices de los elementos a intercambiar.
   
    Esta función no retorna nada."""
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

#-----------------------------------------------------------#
# Función para poner palabras en mayúsculas a minúsculas y viceversa
def cambiar_mayusculas_minusculas(orden:str,cambio:int = 1)->str:
    """
    Función que tiene por objetivo el cambiar un palabra por completo a mayúscula o a minúscula.

    Recibe un parámetro obligatorio y un parámetro opcional:
        orden (str) | cambio (int) = 1

    El parametro opcional solo recibe dos opciones {1} o {2}
        cambio (int) = 1 ---> Convierte todo el texto a minúscula
        cambio (int) = 2 ---> Convierte todo el texto a mayúscula
        cambio (int) = n ---> Tira un mensaje diciendo los parámetros que se admiten

    Retorna la nueva cadena de caracteres de la variable {orden:str}
    """
    orden_nuevo = ""
    #Para pasar de mayusculas a minusculas
    for i in orden:
        match cambio:
            case 1:
                caracter_mayus = ord(i)
                if (caracter_mayus >= 65 and caracter_mayus <= 90):
                    orden_nuevo += chr(caracter_mayus + 32)
                else:
                    orden_nuevo += i
                orden = orden_nuevo
            case 2:
                caracter_minus = ord(i)
                if (caracter_minus >= 97 and caracter_minus <= 122):
                    orden_nuevo += chr(caracter_minus - 32)
                else:
                    orden_nuevo += i
                orden = orden_nuevo
            case _:
                print("Solo se admiten como parametros opcionales el 1 y el 2.")
    return orden
