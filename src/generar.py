import random #importakmos la libreria para generar elementos aleatorios
import string #importamos la libreria para manejar cadenas de texto

#Funcion para generar una letra mayuscula aleatoria
def string_mayus():
    return random.choice(string.ascii_uppercase)

#Funcion para generar una letra minuscula aleatoria
def string_minus():
    return random.choice(string.ascii_lowercase)

#Funcion para genera un numero aleatorio
def ran_num():
    return random.choice(string.digits)

#Funcion para generar un caracter aleatorio
def string_simbol():
    return random.choice(string.punctuation)