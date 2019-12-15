
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

print("----------------------------------------------------------")
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
print("¿Que hacemos cuando faltan valores?¿Cómo los tratamos?","\n")
print("La primera opcion es el borrado de los valores que faltan, bien la columna, bien la fila", "\n")
print("Borramos la fila")
data.dropna(axis=0, how="all") 
# axis=0 borraría toda la fila, y axis=1 borraría toda la columna
# con how le indicamos las filas que tiene que borrar
#   - all, una fila es borrada, si todas sus columnas contienen valores Na
#   - any, una fila es borrada, si al menos una columna contiene un valor Na
print("----------data------------------------")
print(data.dropna(axis=0, how="all"))
print("----------data2-----------------------")
data2=data
print(data2.dropna(axis=0, how="any"))

print("\n\nLa segunda opcion es inferir los datos.\n",
	"El método del Cómputo de los valores faltantes: consite en añadir o reeplazar los valores faltantes por otros.\n",
	"La elección del método dependerá del contexto en el que se encuentren los datos\n")

data3=data
print("Reemplaza los valores que faltan por un cero")
print(data3.fillna(0))
print("---------------------------------")
print("Reemplaza los valores que faltan por una palabra")
print(data3.fillna("Desconocido"))
print("---------------------------------")
print("Otra opcion sería cambiar en función de la columna")
data5=data
data5["body"]=data5["body"].fillna(0)#Sobreescribimos la variable
data5["home.dest"]=data5["home.dest"].fillna("Desconocido")
print(data5.head(50))
print("\nOtra opcion sería cambiar el valor que falta por el promedio de la columna.\nSe utiliza en combinación con el método fillna")

print(pd.isnull(data5["age"]).values.ravel().sum())
data5["age"].fillna(data5["age"].mean())
print(data5.head(50))
print("---------------------------------\n")
print(data5["age"])
print("\nOtra opcion sería cambiar el valor que falta por el inmediato posterior backfill")
print(data5["age"][1291])
print(data5["age"].fillna(method="backfill"))
print("---------------------------------")
print("\nOtra opcion sería cambiar el valor que falta por el inmediato anterior ffill")
print(data5["age"].fillna(method="ffill"))
print("---------------------------------")


print("\n\n\n\nVariables dummy\n")
print(data["sex"])
print("\nLa columna sex es una variable categórica que podemos transformarla en dos columnas: dumificación.")
dummy_sex=pd.get_dummies(data["sex"], prefix="sex")
print("Mostramos las dos columnas que hemos creado.")
print(dummy_sex)

print("\nAhora lo que se suele hacer es elimnar la columna original, para dejar paso a las dos nuevas columnas.\n")
column_name=data.columns.values.tolist()
print("Mostramos el nombre de las columnas originales.")
print(column_name)

print("\nNos cargamos la columna sex.")
data=data.drop(["sex"], axis=1)
column_name=data.columns.values.tolist()
print("\nMostramos el nombre de las columnas, ahora sin sex.")
print(column_name)
print("\nAhora añadimos las variables dummy al data set.")
data=pd.concat([data, dummy_sex], axis=1)#axis=1 significa que lo hacemos por columnas	
print(data)

print("\n\n\nPodemos crear una función que elimine columnas y las convierta en dummies")

def createDummies(df, var_name):
	dummy=pd.get_dummies(df[var_name], prefix=var_name)
	df=df.drop(var_name, axis=1)
	df=pd.concat([df, dummy], axis=1)
	return print(df)

createDummies(data3, "sex")