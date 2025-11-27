import generar #importamos el modulo generar
import random #importamos la librearia para generar elementos aleatorios

def menu(): #funcion para mostrar el menu
    print("==Generador de contraseña==\n" \
    "1. Escriba la longitud de la contraseña\n" \
    )

def opciones(): #funcion para pedir las opciones al usuario
    mayus = input("¿Desea incluir letras mayusculas? (s/n): ").lower()
    minus = input("¿Desea incluir letras minusculas? (s/n)").lower()
    numeros = input("¿Desea incluir numeros? (s/n)").lower()
    simbolos = input("¿Desea incluir simbolos? (s/n)").lower()
    return  mayus, minus, numeros, simbolos

def main():#funcion principal
    menu()
    longo = input("Ingrese la longitud de la contraseña: ").strip() #pedimos la longitud de la contraseña
    result = [] #lista par almacenar las funciones seleccionadas

    if not longo.isdigit() or int(longo) <= 0: #validamos que la contraseña se mayor a cero
        print("La longitud debe ser un numero positivo.")
        return
    longitud = int(longo)
    mayus, minus, numeros, simbolos = opciones()
    if mayus == 's':
        result.append(generar.string_mayus) #agregamos la funcion a la lista para generar mayusculas
    if minus == 's':
        result.append(generar.string_minus) #agregamos la funcion a la lista para generar minusculas
    if numeros == 's':
        result.append(generar.ran_num) #agregamos la funcion a la lista para generar numeros
    if simbolos == 's':
        result.append(generar.string_simbol) #agregamos la funcion a la lista para generar simbolos

    if result == []:
        print("Debe seleccionar al menos un tipo de caracter.")
        return

    

    contraseña = [] #lista para almacenar los caracteres de la contraseña generada
    for _ in range(longitud): #recorremos en base a la longitud ingresada
        ran = random.choice(result) #
        contraseña.append(ran()) #agregamos el resultado de la funcion seleccionada aleatoriamente

    random.shuffle(contraseña) #se mezcla los resultados para generar la contraseña
    print("Contraseña generada: " + ''.join(contraseña)) #mostramos la contraseña generada
 

if __name__ == "__main__":
    main()



     
