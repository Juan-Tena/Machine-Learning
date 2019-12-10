#Carga de datos a traves de la función read_csv

import pandas as pd
import os

#Establecemos dos direcciones y las unimos
mainPath="C:/Users/juan_/Documents/GitHub/Machine-Learning/"
filepathTitanic="Tema 1 - Titanic/titanic3.csv"
fullpathTitanic=mainPath+filepathTitanic
#Utilizamos el paquete os y unimos las dos direcciones. Esta opción es más eficiente.
fullpathTitanic_os=os.path.join(mainPath, filepathTitanic)

#Escribimos la dirección completa sin opciones
data = pd.read_csv("C:/Users/juan_/Documents/GitHub/Machine-Learning/Tema 1 - Titanic/titanic3.csv")#Observar como la barra está al revés
#print(data.head())
print(data)

#Escribimos la dirección completa con opciones
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
print("============ 1 ===============")

print(data1)
print("============ 2 ===============")

data2= pd.read_csv(fullpathTitanic)
print(data2)
print("============ 3 ===============")

data3= pd.read_csv(fullpathTitanic_os)
print(data3)
print("============ 4 ===============")

data4= pd.read_csv(mainPath+"Tema 1 - Titanic/Customer Churn Model.txt")
print(data4)
print("============ 5 ===============")
print(data4.columns.values)

print("============ 6 ===============")

# Vamos a cambiar el nombre de las columnas
data_cols=pd.read_csv(mainPath+"Tema 1 - Titanic/Customer Churn Columns.csv")
print(data_cols)
data_col_list=data_cols["Column_Names"].tolist()
print(data_col_list)
print("============ 7 ===============")

data5= pd.read_csv(mainPath+"Tema 1 - Titanic/Customer Churn Model.txt", header=None, names=data_col_list)
print(data5)

print("============ 8 ===============")

print(data5.columns.values)

print("============ 9 ===============")








print("===Carga de datos a través de la función open===")

data6=open(mainPath+"Tema 1 - Titanic/Customer Churn Model.txt", "r")
#r, solo lectura / rw, lectura y escritura / w, escritura
cols = data6.readline().strip().split(",")
# strip -> se utiliza para eliminar los espacios en blanco que sobran tanto al inicio como al final de la línea
# split -> divide esa línea de texto por un pequeño fragmento, por un delimitador
print(cols)
n_cols=len(cols)
print("============ 10 ===============")
counter=0
main_Dict={}
for col in cols:
	main_Dict[col]=[]

print(main_Dict)
print("============ 11 ===============")
for line in data6:
	values=line.strip().split(",") #divide cada linea en columnas en base al separador, a la coma ","
	for i in range(len(cols)): #itera sobre las columnas de cada linea
		main_Dict[cols[i]].append(values[i])
	counter+=1
print("El data set tiene %d filas y %d columnas" % (counter, n_cols))

print("============ 12 ===============")

df1=pd.DataFrame(main_Dict)
print(df1.head())

print("============ 13 ===============")
#Lectura y escritura de ficheros
infile=mainPath+"Tema 1 - Titanic/Customer Churn Model.txt"
outfile=mainPath+"Tema 1 - Titanic/Tab Customer Churn Model.txt"
with open(infile,"r") as infile1:
	with open(outfile,"w") as outfile1:
		for line in infile1:
			fields=line.strip().split(",")
			outfile1.write("\t".join(fields))
			outfile1.write("\n")
print("============ 14 ===============")
df4=pd.read_csv(outfile,sep="\t")
print(df4)