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