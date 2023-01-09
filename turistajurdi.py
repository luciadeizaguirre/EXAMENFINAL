import numpy as np
import pandas as pd

from tsp_solver.greedy import solve_tsp #la libreria tsp sirve para calcular problemas tpicos del caminos
#utiliza matrices numpy y reduce el uso de la memoria
from tsp_solver.util import path_cost

import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

#Distancias
#Esto crea una matriz con distancias entre ciudades (con el print veras la matriz)
df = pd.DataFrame({
    'Ciudad A': [0,	2507,	9775,	9843,	16691],
    'Ciudad B': [2507,	0,	7706,	10689,	14900],
    'Ciudad C': [9775,	7706,	0,	15925,	7252],
    'Ciudad D': [9843,	10689,	15925,	0,	12917],
    'Ciudad E': [16691,	14900,	7252,	12917,	0]
}, index=['Ciudad A','Ciudad B','Ciudad C','Ciudad D','Ciudad E'])

print(df)
# Como puedes ver, la matriz es simetrica (Distancia de A a B es la misma que de B a A)
# Asi que nos quedamos solo con una de las partes de la matriz para evitar redundancia

#He llamado a la variable lower porque me quedo la parte de abajo
df_lower = pd.DataFrame(np.tril(df), columns = df.columns, index = df.index)
print(df_lower)
#Utilizamos np.tril para hallar el triangulo de una matriz con el valor más pequeño

#Tenemos que salir y volver a la misma ciudad 
#endpoints - (0,0) indica que salimos de ciudad A y volvemos a ella
#Si quisieras cambiar ciudades solo tienes que cambiar el indice por la ciudad que quieras
#Ex: si quiero salir de B y volver a A seria (1,0), de C a B seria (2,1)...
path =  solve_tsp(df_lower.to_numpy(), endpoints=(0,0))
path_len = path_cost(df_lower.to_numpy(), path) #Nos devolverá el valor de la cadena
path_labels = df.columns[path].to_numpy()

print("La ruta mas corta es:", path_labels)
print("La ruta es en total:", path_len, "km")
print("la ruta mas corta cuesta:",(path_len*0.2),"euros") #Para la ultima parte hemos establecido que el kilómetro cuesta 0.20 €
