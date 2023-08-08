from readFile import readFile
import os

readFile_handler=readFile()

def salir():
    print("Programa finalizado")

def clear():
    os.system('cls')


def cargarInventario():
    clear()
    ruta = input("Ingrese ruta del archivo: ")
    clear()
    print("--------------Inventario Inicial--------------")
    readFile_handler.leer_archivo_inv(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()


def cargarMovimientos():
    clear()
    ruta = input("Ingrese ruta del archivo: ")
    clear()
    print("--------------Instrucciones movimientos--------------")
    readFile_handler.leer_archivo_mov(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()
    

def crearInventarioTxt():
    clear()
    ruta = input("Ingrese nombre del archivo a crear: ")
    clear()
    readFile_handler.crear_archivo_txt(ruta)
    print("Archivo creado exitosamente!")
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()

def menuInicial():
    print("")
    print("-------------------------------------------------")
    print("Practica 1 - Lenguajes formales y de programacion")
    print("-------------------------------------------------")
    print("# Sistema de inventario")
    print("1. Cargar Inventario Inicial")
    print("2. Cargar instrucciones de movimiento")
    print("3. Crear informe de inventario")
    print("4. Salir")
    print("")
    opcion=input("Ingrese una opción del menú: ")
    if opcion=="1":
        try:
            cargarInventario()
            menuInicial()
        except:
            clear()
            print("----Error! Archivo no encontrado----")
            menuInicial()
    elif opcion=="2":
        try:
            cargarMovimientos()
            menuInicial()
        except:
            clear()
            print("----Error! Archivo no encontrado----")
            menuInicial()
    elif opcion=="3":
        try:
            crearInventarioTxt()
            menuInicial()
        except:
            clear()
            print("----Error! Archivo no pudo ser creado----")
            menuInicial()
    elif opcion=="4":
        salir()
    else:
        clear()
        print("Indique una opción válida")
        menuInicial()


menuInicial()