import pandas as pd
import matplotlib.pyplot as plt

data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'Ventas': [10000, 12000, 15000, 11000, 14000]}

df = pd.DataFrame(data)

plt.barh(df['Mes'], df['Ventas'], color='skyblue')
plt.xlabel('Ventas Totales')
plt.ylabel('Mes')
plt.title('Ventas Mensuales por Mes')
plt.gca().invert_yaxis()

plt.show()



