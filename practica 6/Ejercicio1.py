class Articulos:
    def __init__(self, articulos=[]):
        self.articulos = articulos

    def mostrar_articulos(self):
        print("Nuestros Articulos son:")
        for articulo in self.articulos:
            print(articulo)

    def vender_articulo(self, nombre_articulo):
        if nombre_articulo in self.articulos:
            print("Se vendio el Articulo:", nombre_articulo, "Gracias por tu compra")
            self.articulos.remove(nombre_articulo)
        else:
            print("El Articulo no existe o ya fue vendido")


articulos = Articulos(["agua", "jugo", "gaseosa"])

while True:
    print("1: Mostrar Articulos")
    print("2: Vender Articulo")
    print("3: Cerrar")

    opcion = int(input("Ingresa una opcion 1, 2, 3: "))

    if opcion == 1:
        articulos.mostrar_articulos()
    elif opcion == 2:
        nombre_articulo = input("Ingresa el articulo a vender: ")
        articulos.vender_articulo(nombre_articulo)
    elif opcion == 3:
        break
