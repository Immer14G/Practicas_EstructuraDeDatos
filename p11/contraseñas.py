
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña


import contraseñas


longitud_contraseña = 10
contraseña_generada = contraseñas.generar_contraseña(longitud_contraseña)

print(f"Contraseña generada: {contraseña_generada}")
