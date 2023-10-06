class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad_entero = int(edad)
            if edad_entero >= 0:
                return True
            else:
                print("La edad debe ser un número entero positivo.")
                return False
        except ValueError:
            print("Error: Debe ingresar un número entero válido para la edad.")
            return False

validador = ValidadorDeEdad()
edad_ingresada = input("Ingrese una edad: ")

if validador.validar(edad_ingresada):
    print("Edad válida.")
else:
    print("Edad no válida.")
