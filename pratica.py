

#Ejercicio 1
suma=0
for numero in range(1,200):
   suma=+numero

print("la suma de los numeros enteros es ",suma )  

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 2
palabra="Hola estoy programando en phyton"
vocales=["a","e","i","o","u"]
for vocal in vocales:
 print(vocal,palabra.count(vocal)) 

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercico 3
numeros=[1,4,6,7,8,10,13,2,9,10,7,3,8]
pares=[]
impares=[]

for numeros in numeros:
  if numeros%2==0:
     pares.append(numeros)
  else:
     impares.append(numeros)

print("serie",numeros)   
print("Pares",pares)
print("Impares",impares)