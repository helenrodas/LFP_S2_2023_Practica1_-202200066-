from readFile import readFile

readFile_handler=readFile()

def salir():
    print("Programa finalizado")
    

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
    #while True:
    if opcion=="1":
        print("")
        print("--------------Inventario Inicial--------------")
        readFile_handler.leer_archivo('P:\Programacion\PracticasPython\Practica1LF/inventario.inv','r')
        print("")
        input("Presione enter para continuar...")
        menuInicial()
    elif opcion=="2":
        print("Accedio a Cargar instrucciones de movimiento")
        input("Presione una enter para continuar...")
        menuInicial()
    elif opcion=="3":
        print("Accedio a cargar Crear informe de inventario")
        input("Presione una tecla para continuar...")
        menuInicial()
    elif opcion=="4":
        print("Saliendo del programa, vuevla pronto")
        salir()
    else:
        print("Indique una opción válida")
        menuInicial()
            

menuInicial()