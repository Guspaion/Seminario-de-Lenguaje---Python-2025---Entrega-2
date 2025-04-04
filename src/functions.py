#Ejercicio 1
def segunda_palabra_vocal(linea):
    palabras = linea.split()
    if len(palabras) > 1 and palabras[1][0].lower() in "aeiou": 
        return True
    return False

#Ejercicio 4
def validar_nombre_usuario(nombre):
    digitos = 0
    mayusculas = 0

    if(len(nombre) < 5):
        print("El nombre debe tener al menos 5 caracteres")
        return False

    for caracter in nombre:
        if caracter.lower() not in string.ascii_lowercase and caracter not in "0123456789":
            print("Se ingresaron caracteres no válidos (Solo debe tener letras y números)")
            return False
        if caracter in string.digits:
            digitos += 1
            continue
        if caracter in string.ascii_uppercase:
            mayusculas += 1
    if digitos == 0:
        print("El nombre debe tener al menos un número")
        return False
    if mayusculas == 0:
        print("El nombre debe contener al menos una mayúscula")
        return False
    return True

#Ejercicio 5
def velocidad_reaccion(ms):
    if ms < 200:
        return("Bueno")
    elif ms < 500:
        return("Normal")
    else:
        return("Lento")
    
#Ejercicio 6
def contarPalabra(palabra_a_contar, descriptions):
    cant = 0
    for linea in descriptions:  # Iteramos sobre cada string en la lista
        for palabra in linea.split():  # Dividimos cada línea en palabras
            if palabra.lower() == palabra_a_contar.lower():
                cant += 1
    return cant

#Ejercicio 7
import random
import datetime
import string

def validar_nombre(nombre):
    if(len(nombre) > 15 or " " in nombre):
        return False
    return True

def ingresar_nombre():
    valido = False
    while(not valido):
        user_name = input("Ingrese su nombre de usuario: ")
        if validar_nombre(user_name):
            return user_name.upper()
        print("El nombre no puede tener más de 15 caracteres ni contener espacios")

def generar_codigo(nombre):
    fecha_hoy = datetime.date.today()
    base = f"{nombre}-{fecha_hoy.year}{str(fecha_hoy.month).zfill(2)}{str(fecha_hoy.day).zfill(2)}"
    codigo = random.choices(string.ascii_uppercase + string.digits, k = 30 - len(base))
    cod_final = f"{base}-"
    for caracter in codigo: 
        cod_final += caracter
    return cod_final

#Ejercicio 8
def es_anagrama(palabra, otra_palabra):
    if len(palabra) != len(otra_palabra):
        return False
    otra_palabra = list(otra_palabra)
    for letra in palabra:
        if letra in otra_palabra:
            otra_palabra.remove(letra)
        else:
            return False
    return True

#Ejercicio 9
def es_dato_vacio(nombre):
    if(nombre is None) or (nombre.strip() == ""):
        return True
    return False

def eliminar_espacios(nombre):
    return " ".join(nombre.split())

def capitalizar_nombre(nombre):
    nombre_separado = nombre.split()
    nombre_capitalizado = [termino.capitalize() for termino in nombre_separado]
    return " ".join(nombre_capitalizado)

def esta_duplicado(nombre, lista):
    if nombre in lista:
        return True
    return False

def normalizar_nombre(nombre):
    tildes = "áéíóú"
    sin_tildes = "aeiou"
    nombre_normalizado = ""
    for letra in nombre:
        if letra in tildes:
            nombre_normalizado += sin_tildes[tildes.index(letra)]
        else:
            nombre_normalizado += letra
    return nombre_normalizado

def procesar_lista(lista):
    lista_final = []
    for nombre in lista:
        if es_dato_vacio(nombre):
            continue
        nombre = eliminar_espacios(nombre)
        nombre = capitalizar_nombre(nombre)
        nombre = normalizar_nombre(nombre)
        if not esta_duplicado(nombre, lista_final):
            lista_final.append(nombre)
        lista_final.sort()
    return lista_final

#Ejercicio 10
def inicializar_ronda_act():
    ronda_act = {
        'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0},
        'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0},
        'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0},
        'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0},
        'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0}
    }
    return ronda_act

def contabilizar_puntos(player):
    puntos = 0
    puntos += player['kills'] * 3
    puntos += player['assists']
    if player['deaths']:
        puntos -= 1
    return puntos

def determinar_MVP(round):
    puntos_MVP = 0
    nombre_MVP = ""
    for player, stats in round.items():
        if puntos_MVP == 0 or stats['puntos'] > puntos_MVP:
            puntos_MVP = stats['puntos']
            nombre_MVP = player
    return nombre_MVP, puntos_MVP

def generar_tabla_ronda_act(round, ronda_act):
    for player, stats in round.items():
        if player not in ronda_act:
            ronda_act[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0}
        ronda_act[player]['kills'] += stats['kills']
        ronda_act[player]['assists'] += stats['assists']
        if( stats['deaths']):
            ronda_act[player]['deaths'] = "Si"
        else:
            ronda_act[player]['deaths'] = "No"
        ronda_act[player]['puntos'] = contabilizar_puntos(stats)
    return ronda_act

def generar_tabla_total(ronda_act, total_rondas, nombre_MVP):
    for player, stats in ronda_act.items():
        total_rondas[player]['kills'] += stats['kills']
        total_rondas[player]['assists'] += stats['assists']
        if stats['deaths'] == "Si":
            total_rondas[player]['deaths'] += 1
        total_rondas[player]['puntos'] += stats['puntos']
    total_rondas[nombre_MVP]['MVP'] += 1
    return total_rondas

def imprimir_estadisticas_ronda(ronda_act):
    for player, stats in ronda_act.items():
        print(
            player.ljust(10) + 
            str(stats['kills']).ljust(10) + 
            str(stats['assists']).ljust(15) + 
            str(stats['deaths']).ljust(10) + 
            str(stats['puntos']).ljust(10)
        )

def imprimir_estadisticas_finales(total_rondas):
    for player, stats in total_rondas.items():
        print(
            player.ljust(10) + 
            str(stats['kills']).ljust(10) + 
            str(stats['assists']).ljust(15) + 
            str(stats['deaths']).ljust(10) + 
            str(stats['MVP']).ljust(10) + 
            str(stats['puntos']).ljust(10)
        )