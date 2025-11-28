import generar #importamos el modulo generar
import random #importamos la librearia para generar elementos aleatorios
import hashlib #importamos la libreria para hashear la contraseña
import csv #importamos la libreria para manejar archivos csv
import datetime #improtamos la libreria para usar fechas
import os #importamos la libreria para manejar archivos y rutas

def menu(): #funcion para mostrar el menu
    print("==Generador de contraseña==\n" \
    "1. Generar contraseña segura\n" \
    "2. Verificar contraseña\n" \
    )

def opciones(): #funcion para pedir las opciones al usuario
    usu = input("Ingrese el nombre de usuario:").strip().upper()
    mayus = input("¿Desea incluir letras mayusculas? (s/n): ").lower()
    minus = input("¿Desea incluir letras minusculas? (s/n)").lower()
    numeros = input("¿Desea incluir numeros? (s/n)").lower()
    simbolos = input("¿Desea incluir simbolos? (s/n)").lower()
    return  usu ,mayus, minus, numeros, simbolos

def main():#funcion principal
    menu()
    option = input("Seleccione una opcion:").strip() #pedimos la opcion al usuario
    if option == '1':
        longo = input("Ingrese la longitud de la contraseña: ").strip() #pedimos la longitud de la contraseña
        result = [] #lista par almacenar las funciones seleccionadas
        if not longo.isdigit() or int(longo) <= 0: #validamos que la contraseña se mayor a cero
            print("La longitud debe ser un numero positivo.")
            return
        longitud = int(longo)
        usu, mayus, minus, numeros, simbolos = opciones()
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
            ran = random.choice(result) #funcion para generar un caracter aleatorio de las funciones seleccionadas
            contraseña.append(ran()) #agregamos el resultado de la funcion seleccionada aleatoriamente

        random.shuffle(contraseña) #se mezcla los resultados para generar la contraseña
        print("Contraseña generada:",''.join(contraseña)) #mostramos la contraseña generada
        salt = generar.salt_gen() #generamos una salt aleatoria
        print("Salt generada:",salt) #mostramos la salt generada
        contraseña_hash = hashlib.sha256((''.join(contraseña) + salt).encode()).hexdigest() #hasheamos la contraseña con la salt
        print("Contraseña hasheada:",''.join(contraseña_hash)) #mostramos la contraseña hasheada
        
        
        fecha = datetime.datetime.now() #obtenemos la fecha actual
        ruta_carpeta = os.path.dirname(__file__)
        ruta_csv = os.path.join(ruta_carpeta, 'pass_gen.csv') #obtenemos la ruta de el archivo .csv


        with open(ruta_csv, 'a', newline='', encoding= 'utf-8') as file: #abrimos el archivo csv
            write = csv.writer(file)
            write.writerow([usu, salt, contraseña_hash, fecha]) #escribimos una nueva fila con los datos

    elif option == '2': #condicion de verificacion de contraseña
        usu = input("Ingrese el nombre de usuario:").strip().upper() #input para ingresar el usuario
        ruta_carpeta = os.path.dirname(__file__)
        ruta_csv = os.path.join(ruta_carpeta, 'pass_gen.csv')

        #b9O6e1r7
        with open(ruta_csv, 'r', newline='', encoding = 'utf-8') as file: #abrimos en modo lectura
            read = csv.reader(file) #creamos variable para manejar los datos del archivo
            for row in read: #bucle para recorrer el archivo
                if row[0] == usu: #validamos el usuario
                    contraseña = input("Ingrese la contraseña a verificar:").strip()
                    salt = row[1]
                    pass_hash = row[2]
                    new_hash = hashlib.sha256((contraseña + salt).encode()).hexdigest() #creamos un hash para ver si es igual
                    if new_hash == pass_hash: #validacion para saber si es igual
                        print("Contraseña es correcta.")
                    else:
                        print("Datos incorrectos.")
                else:
                    print("Usuario no encontrado.")
                

if __name__ == "__main__":
    main()



     
