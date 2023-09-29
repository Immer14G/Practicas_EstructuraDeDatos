class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
carnet = input("Ingrese el carnet del estudiante: ")
carrera = input("Ingrese la carrera del estudiante: ")

# Crear un estudiante con los datos proporcionados
estudiante = Estudiante(nombre, apellido, carnet, carrera)

# Imprimir los datos del estudiante
print("  Datos del estudiante:")
print("Nombre:", estudiante.nombre)
print("Apellido:", estudiante.apellido)
print("Carnet:", estudiante.carnet)
print("Carrera:", estudiante.carrera)


opcion = input("\n¿Desea actualizar los datos del estudiante? (S/N): ").strip().lower()
if opcion == "s":
    nuevo_nombre = input("Nuevo nombre: ")
    estudiante.actualizar_nombre(nuevo_nombre)

    nuevo_apellido = input("Nuevo apellido: ")
    estudiante.actualizar_apellido(nuevo_apellido)

    nuevo_carnet = input("Nuevo carnet: ")
    estudiante.actualizar_carnet(nuevo_carnet)

    nueva_carrera = input("Nueva carrera: ")
    estudiante.actualizar_carrera(nueva_carrera)

   
    print("  Datos actualizados del estudiante:")
    print("Nombre:", estudiante.nombre)
    print("Apellido:", estudiante.apellido)
    print("Carnet:", estudiante.carnet)
    print("Carrera:", estudiante.carrera)
else:
    print("  Un nuevo estudiante Bienvenido ",nombre)
