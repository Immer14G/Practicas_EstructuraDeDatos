class Divisor:
    def dividir(self, numerador, denominador):
        try:
            resultado = numerador / denominador
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero."

divisor = Divisor()


resultado1 = divisor.dividir(10, 2)
print(resultado1)  # Debe imprimir: 5.0


resultado2 = divisor.dividir(5, 0)
print(resultado2)  
