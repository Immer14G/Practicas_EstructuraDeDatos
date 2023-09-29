class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def iniciar_sesion(self, password_ingresada):
        if password_ingresada == self.password:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta. Inicio de sesión fallido.")

    def cerrar_sesion(self):
        print("Cierre de sesión exitoso.")

class CuentaUsuario:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def iniciar_sesion(self, username, password_ingresada):
        for usuario in self.usuarios:
            if usuario.username == username:
                usuario.iniciar_sesion(password_ingresada)
                return
        print("Usuario no encontrado. Inicio de sesión fallido.")

    def cerrar_sesion(self):
        for usuario in self.usuarios:
            usuario.cerrar_sesion()

cuenta = CuentaUsuario()

# Agregar usuarios
usuario1 = Usuario("usuario1", "contraseña1")
usuario2 = Usuario("usuario2", "contraseña2")

cuenta.agregar_usuario(usuario1)
cuenta.agregar_usuario(usuario2)

while True:
    print("1: Iniciar sesión")
    print("2: Cerrar sesión")
    print("3: Cerrar programa")

    opcion = int(input("Ingresa una opción 1, 2, 3: "))

    if opcion == 1:
        username = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu contraseña: ")
        cuenta.iniciar_sesion(username, password)
    elif opcion == 2:
        cuenta.cerrar_sesion()
    elif opcion == 3:
        break
