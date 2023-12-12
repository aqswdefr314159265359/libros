#Se solicita incluir la siguiente información acerca de un libro: 
#Titulo
#Autor
#Debes imprimir la información en el siguiente formato:
#Proporciona el titulo:
#Proporciona el autor:
#titulo fue escrito por autor
import os
import time

respuesta = ""
aNBook = ["El mago", "El lobo", "harry potter"]
aNameAutor = ["aa12", "el aed", "nose"]
top = "#" * 50
one = "#"
space = " "


def index():
    top = "#" * 50
    one = "#"
    space = " "
    print(top)
    print(one,(space*46),one)
    print(one,(space*12),"Datos de los libros",(space*13),one)
    print(one,(space*46),one)
    print(one,(space*2),"Ingresa una de las siguientes opciones",(space*4),one)
    print(one,(space*2),"1. Ingresa los datos de un libro.",(space*9),one)
    print(one,(space*2),"2. Lee los datos de los libros ingresados",space,one)
    print(one, (space*2),"3. Salir",(space* 34),one)
    print(one,(space*46),one)
    print((one*50))
    respuesta = int(input(""))

    if(respuesta == 1):
        ingresarDatos()
    elif(respuesta == 2):
        consultaDatos()
    elif(respuesta == 3):
        salir()
    else:
        print("Ingresa una opcion valida")
        os.system("cls")
        index()
        

def ingresarDatos():
    os.system("cls")
    nameBook = input("Ingresa el nombre del libro\n")
    autorName = input("Ingresa el nombre del autor\n")
    aNameAutor.append(autorName)
    aNBook.append(nameBook)
    back = input("Quieres regresar al menu principal?\n")
    if(back == "yes" or back == "Yes" or back == "YES"):
        os.system("cls")
        index()
    else:
        salir()
    
def consultaDatos():
    os.system("cls")
    rangeNameAutor = len(aNameAutor)
    number = 0
    print(top)
    print(one,(space*46),one)
    print(one,(space*12),"Libros ingresados",(space*15),one)
    print(one,(space*46),one)
    print(one,(space*2),"hay ",len(aNameAutor)," libros Ingresados",(space*17),one)
    print(one,(space*2))
    for number in range(rangeNameAutor):
        print(one,(space*2),f"{number+1}.","Nombre del Libro:",aNBook[number])
        print(one, (space*5),"Nombre del autor:",aNameAutor[number])
        print(one)
        letras = len(aNBook[number])
        print(f"esta oracion tiene: {letras} caracteres")
        number = number + 1




def salir():
    os.system("cls")
    print("Good Bye!")
    time.sleep(4)
    os.system("cls")
    os.system("exit()")

consultaDatos()