
#Resumen de los datos: dimensiones y estructuras
import pandas as pd
import os

mainpath = "C:/Users/juan_/Documents/GitHub/Machine-Learning/Tema 5 - Data Cleaning - Analisis preliminar"
filename = "titanic3.csv"
fullpath = os.path.join(mainpath, filename)

urldata = "https://raw.githubusercontent.com/Juan-Tena/python-ml-course/master/datasets/titanic/titanic3.csv"

#data = pd.read_csv(fullpath)
data = pd.read_csv(urldata)

#Comprobamos que los datos se han cargado correctamente. Leemos las 10 primeras filas
print(data.head(10))
print("------------------------------------------")

#Dimensión de un data set
print(data.tail)
print("------------------------------------------")
print(data.shape)
print("------------------------------------------")
print(data.columns)
print("------------------------------------------")
print(data.columns.values)
print("------------------------------------------")
#-Resumen de los estadísticos basicos de la vables numéricas
print(data.describe())
print("------------------------------------------")
#Tipo de datos
print(data.dtypes)