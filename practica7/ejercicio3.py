class ValidadorContraseña:
    def __init__(self, longitud_minima):
        self.longitud_minima = longitud_minima

    def validar(self, contraseña):
        try:
            if len(contraseña) >= self.longitud_minima:
                return True
            else:
                raise ValueError("La contraseña es demasiado corta. .".format(self.longitud_minima))
        except ValueError as e:
            print("Error:", e)
            return False

longitud_minima = 8  
validador = ValidadorContraseña(longitud_minima)
contraseña_ingresada = input("Ingrese una contraseña: ")

if validador.validar(contraseña_ingresada):
    print("Contraseña válida.")
else:
    print("Contraseña no válida.")
