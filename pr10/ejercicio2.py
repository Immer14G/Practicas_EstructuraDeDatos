import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('puntajes.csv')

plt.fill_between(df.index, df['Examen1'], df['Examen2'], alpha=0.7)
plt.xlabel('Estudiantes')
plt.ylabel('Puntajes')
plt.title('Relación entre Puntajes en Examen 1 y Examen 2')

plt.show()
