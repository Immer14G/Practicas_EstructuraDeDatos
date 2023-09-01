def ejercicio4():
 Cadena = "Medir el progreso en un proyecto de programación por líneas de código, es como medir la construcción de un aeroplano por su peso."
 NuevaCadena = input("Me puedes decir tu cadena de texto a medir: ")

 FrasePalabras = len(Cadena.split())
 nuevasPalabras = len(NuevaCadena.split())
 Total = FrasePalabras + nuevasPalabras

 print("primera:", Cadena, "tiene", FrasePalabras, "palabras")
 print("segunda frase:", NuevaCadena, "tiene", nuevasPalabras, "palabras")
 print("Total de palabras:", Total)