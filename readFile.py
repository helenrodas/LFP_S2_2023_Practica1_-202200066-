from CProoducto import CProoducto
import os
class readFile:
    def __init__(self):
        self.listaProductos = []
    


    def leer_archivo_inv(self, ruta):
        self.listaProductos = []
        print("--------------Inventario Inicial--------------")
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

        
    def leer_archivo_mov(self, ruta):
        
        if ( self.verificarListaProductos()) == False:
            return
        print("--------------Instrucciones movimientos--------------")
        
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
                            if cantidadAVenderAsInt <= cantidadActualAsInt:
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


    def crear_archivo_txt(self, ruta):
        
        ruta_carpeta = "P:\Programacion\PracticasPython\Practica1LF\Resultados"
        ruta_completa = os.path.join(ruta_carpeta, f"{ruta}.txt")
        
        if ( self.verificarListaProductos()) == False:
            return
        
    
        
        with open(ruta_completa, "w") as archivo:
            print("Archivo creado exitosamente!")
            archivo.write("Informe de Inventario:\n")
            archivo.write("{:<14} {:<14} {:<14} {:<14} {:<29}\n".format("Producto", "Cantidad", "Precio", "Bodega","Valor total"))
            archivo.write("-" * 70 + "\n")

            for producto in self.listaProductos:
                valorTotalAsInt = int(producto.cantidad) * float(producto.precio)
                valorTotalAsFloat = round(valorTotalAsInt,2)
                archivo.write("{:<14} {:<14} {:<14} {:<14} {:<29}\n".format(str(producto.nombre), str(producto.cantidad), str(producto.precio), str(producto.ubicacion), str(valorTotalAsFloat)))
                

    def verificarListaProductos(self):
        if len(self.listaProductos) == 0:
            print("Error! No hay datos para mostrar")
            return False
        
        return True