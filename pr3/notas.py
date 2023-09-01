notas = []


for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
    notas.append(nota)

print("\nNotas obtenidas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")


nota_media = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"\nNota media: {nota_media:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota menor: {nota_minima}")
