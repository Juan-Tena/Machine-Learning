#Carga de datos a traves de la función read_csv

import pandas as pd

data = pd.read_csv("C:/Users/juan_/Documents/GitHub/Machine-Learning/Tema 1 - Titanic/titanic3.csv")#Observar como la barra está al revés
#print(data.head())
print(data)

data1= pd.read_csv(filepath_or_buffer="C:/Users/juan_/Documents/GitHub/Machine-Learning/Tema 1 - Titanic/titanic3.csv", sep=",",
	dtype=None, header=0, names=None, skiprows=None, index_col=None, skip_blank_lines=True, na_filter=False)

# ARGUMENTOS de read_csv
# sep, permite especificar el separador de campo
# dtype, nos permite especificar que tipo de dato debe contener cada columna
#     primero se carga la librería Numpy: import Numpy as np
#     a continuación se pone que tipo de dato recoge cada columna
#           dtype{"a":np.float64, "b":np.int32}
#     en el caso de utilizar None, es el propio python quien lo determina de manera automática
# header, permite establecer que fila se va a utilizar como cabecera
#     por defecto, la primera fila es la que se surle utilizar como cabecera. Para ello se utiliza 0 ó None
# names, permite intorducir el nombre de las columnas. Para ello se crea una lista o un array
#     por defecto se utilzia None, es decir, utiliza los nombre que tiene el fichero
#     ejemplo: names={"ingresos", "edad"}
# skiprows, permite saltar un determinado número de filas al leer el fichero. El valor por defecto es None ó 0
#     skiprows=12 significa que la primera fila que se leería sería la 13
# index_col, permite establecer la columna índice. Puede ser un número concreto o None. En este caso, se establece un contador numérico
# skip_blank_lines, permite excluir las líneas en blanco que contenga el fichero, en lugar de que aparezcan como none
# na_filter, permite detectar los valores que faltan dentro del dataset. Por defecto su valor es True


print("===========================")
print(data1)