
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

print("---------VALORES PERDIDOS---------------------------------")
#Metodo para comprobar si faltan valores
print(pd.isnull(data["body"]))#Nos muestra verdadero si faltan valores
print(pd.notnull(data["body"]))#Muestra  verdadero si hay valor

#Si quiero que me devuelva un array
print(pd.isnull(data["body"]).values)
print("------------------------------------------")
#la funcion ravel() permite construir u unico array de datos, a los que les puedo aplicar una función como sum()
print("Número de registros sin valor en la columna de 'body':",pd.isnull(data["body"]).values.ravel().sum()) #Cuenta el numero de valores que son isnull
print("Número de registros con valor en la columna de 'body':",pd.notnull(data["body"]).values.ravel().sum())
print("------------------------------------------")
print("Por tanto, sabemos que faltan valores")
print("Los valores que faltan en un dataset pueden ser debidos a dos razones","\n","   - Primer motivo: la propia extracción de los datos"
	,"\n", "   - Segundo motivo: la recolección de los datos")

print("------------------------------------------")
print("¿Que hacemos cuando faltan valores?¿Cómo los tratamos?")

