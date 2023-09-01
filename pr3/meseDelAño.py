def ejercicio_3():
 def meses(NumeroDeMes):
    if NumeroDeMes == 1:
        return "Enero"
    elif NumeroDeMes == 2:
        return "Febrero"
    elif NumeroDeMes == 3:
        return "Marzo"
    elif NumeroDeMes == 4:
        return "Abril"
    elif NumeroDeMes == 5:
        return "Mayo"
    elif NumeroDeMes == 6:
        return "Junio"
    elif NumeroDeMes == 7:
        return "Julio"
    elif NumeroDeMes == 8:
        return "Agosto"
    elif NumeroDeMes == 9:
        return "Septiembre"
    elif NumeroDeMes == 10:
        return "Octubre"
    elif NumeroDeMes == 11:
        return "Noviembre"
    elif NumeroDeMes == 12:
        return "Diciembre"
    else:
        return "Mes inválido"
 NumeroDeMes = int(input("Ingresa un número de mes (entre 1 y 12): "))
 nombre = meses(NumeroDeMes)
 print("El mes  es ",nombre)