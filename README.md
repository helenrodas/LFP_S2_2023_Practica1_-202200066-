# Manual Tecnico
## Helen Rodas - 202200066 - Practica 1

El proyecto consta de tres documentos de python, el primero es el main que es el principal, el segundo es el readFile que es en donde estan definidas las funciones y el tercero es la clase CPoducto que es donde guardo los datos de cada producto a ingresar y asi cada nuevo objeto del tipo clase lo guardo en una lista la cual ya puedo manejar en todas mis funciones.

## CProducto.py
Dentro de esta clase incluimos cada caracteristica que pueda tener cada producto a ingresar en el constructor.
```python
def __init__(self,nombre,cantidad,precio,ubicacion):
        self.nombre=nombre
        self.cantidad=cantidad
        self.precio=precio
        self.ubicacion=ubicacion

```
## main.py
Esta clase es la principal en donde se desarrolla el menu principal
Funcion clear limpia la consola.
```python
def clear():
    os.system('cls')
```
Funcion menu_principal, imprime todas las opciones del menu
```python
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
```
- Opcion 1: cargarInventario() sirve para que el usuario pueda cargar el inventario inicial desde la clase readFile
```python
def cargarInventario():
    clear()
    ruta = input("Ingrese ruta del archivo: ")
    clear()
    print("--------------Inventario Inicial--------------")
    readFile_handler.leer_archivo_inv(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()
```

- Opcion 2: cargarMovimientos() sirve para que el usuario pueda cargar el archivo que tiene las acciones de agregar y vender desde la clase readFile
```python
def cargarMovimientos():
    clear()
    ruta = input("Ingrese ruta del archivo: ")
    clear()
    print("--------------Instrucciones movimientos--------------")
    readFile_handler.leer_archivo_mov(ruta,'r')
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()
```
- Opcion 3: crearInventarioTxt() crea un archivo txt donde tiene la informacion del inventario actualizada desde la clase readFile
```python
def crearInventarioTxt():
    clear()
    ruta = input("Ingrese nombre del archivo a crear: ")
    clear()
    readFile_handler.crear_archivo_txt(ruta)
    print("----------------------------------------------")
    input("Presione enter para continuar...")
    clear()
```
- Opcion 4: salir del programa
```python
def salir():
    print("Programa finalizado")
```

## readFile
En esta clase se realizan todas las funciones a desarrollar para la edicion y lectura de archivos

- El constructo de la clase donde se inicializa la lista donde se guardara cada objeto del tipo CProducto
```python
def __init__(self):
    self.listaProductos = []
```

- Funcion verificarListaProductos va a verificar que la lista de productos contenga datos, en caso contrario no va a proceder a realizar las acciones con los archivos. 
```python
def verificarListaProductos(self):
        if len(self.listaProductos) == 0:
            print("Error! No hay datos para mostrar")
            return False
        
        return True
```

- Funcion leer_archivo_inv va a pedir que se le envie el nombre del archivo tipo .inv para abrir el documento y leer cada linea, hace la separacion de cada categoria del producto y muestra el inventario.
```python
def leer_archivo_inv(self, ruta):
        self.listaProductos = []
        
        with open(f"{ruta}.inv", "r") as archivo:
            lineasArticulos = archivo.readlines()

            for linea in lineasArticulos:
                    linea = linea.replace("crear_producto", "")
                    articulo = linea.strip().split(";")
                    producto = CProoducto(articulo[0], articulo[1], articulo[2], articulo[3])
                    self.listaProductos.append(producto)

        for producto in self.listaProductos:
            print("Nombre: ", producto.nombre)
            print("Cantidad: ", producto.cantidad)
            print("Precio: ", producto.precio)
            print("Ubicacion: ", producto.ubicacion)
```

- Funcion leer_archivo_mov va a pedir que se le envie el nombre del archivo tipo .mov para abrir el documento y leer cada linea, hace la separacion de que tipo de accion se va a realizar ya sea agregar_stock o vender_producto y dependiendo que ocpion sea va a realizar lo que se le pide, mostrando al final cuales fueron los cambios realizados.
```python
def leer_archivo_mov(self, ruta):
        
    if ( self.verificarListaProductos()) == False:
         return

    with open(f"{ruta}.mov", "r") as archivo:
        lineasMovimientos = archivo.readlines()

            for linea in lineasMovimientos:
                actionSplit = linea.split()
                action = actionSplit[0] #Aqui guarda solo la accion que va a realizar
                articulo = actionSplit[1]
                articuloSplit = articulo.split(";") #Aqui separa cada punto y coma y guarda toda la informacion del producto en un array

                if action == "agregar_stock":
                    for producto in self.listaProductos:
                        if articuloSplit[0] == producto.nombre and articuloSplit[2] == producto.ubicacion:
                            cantidadActualizada = int(articuloSplit[1]) + int(producto.cantidad)
                            producto.cantidad = str(cantidadActualizada)
                            print("Producto:", producto.nombre, "---", "Nueva cantidad:", producto.cantidad)
                            break
                    else:
                        print("No se encontro producto")
                elif action == "vender_producto":
                    for producto in self.listaProductos:
                        if articuloSplit[0] == producto.nombre and articuloSplit[2] == producto.ubicacion:
                            cantidadActualAsInt = int(producto.cantidad)
                            cantidadAVenderAsInt = int(articuloSplit[1])
                            if cantidadAVenderAsInt < cantidadActualAsInt:
                                nuevaCantidad = cantidadActualAsInt - cantidadAVenderAsInt
                                producto.cantidad = str(nuevaCantidad)
                                print("Producto Vendido:", producto.nombre, "---", "Nueva cantidad en stock:", producto.cantidad)
                                break
                            else:
                                print("Venta invalida! No hay:", producto.nombre, "En stock")
                                break
                    else:
                        print("No se encontro producto")
                else:
                    print("Opcion no valida")
```
- Funcion crear_archivo_txt va a pedir que se le envie un nombre para crear el archivo de tipo .txt el cual va a contenter la informacion del inventario actualizado despues de realizar las funciones anteriores.
```python
 def crear_archivo_txt(self, ruta):
        ruta_carpeta = "P:\Programacion\PracticasPython\Practica1LF\Resultados"
        ruta_completa = os.path.join(ruta_carpeta, f"{ruta}.txt")
        
        if ( self.verificarListaProductos()) == False:
            return
        
        with open(ruta_completa, "w") as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("{:<14} {:<14} {:<14} {:<14} {:<29}\n".format("Producto", "Cantidad", "Precio", "Bodega","Valor total"))
            archivo.write("-" * 70 + "\n")

            for producto in self.listaProductos:
                valorTotalAsInt = int(producto.cantidad) * float(producto.precio)
                valorTotalAsFloat = round(valorTotalAsInt,2)
                archivo.write("{:<14} {:<14} {:<14} {:<14} {:<29}\n".format(str(producto.nombre), str(producto.cantidad), str(producto.precio), str(producto.ubicacion), str(valorTotalAsFloat)))
```