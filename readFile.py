from CProoducto import CProoducto

class readFile:
    def __init__(self):
        self.listaProductos = []


    def leer_archivo(self, ruta, modo):
        self.listaProductos = []
        with open(ruta, modo) as archivo:
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
