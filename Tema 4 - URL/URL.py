import urllib3
import os
import pandas as pd

medals_url="http://winterolympicsmedals.com/medals.csv"

#Importamos la libreria y hacemos la conexión con la web de los datos
http = urllib3.PoolManager()
r=http.request('GET', medals_url)
print("El estado de la respuesta es %d" %(r.status)) #Hacemos esto porque es un entero
response=r.data #<-- es un string binario

#El objeto response contiene un string binario, así que lo convertimos a un string decodificándolo en UTF-8
str_data=response.decode('utf-8')

#print(str_data)
#print("--------------------------")

#Dividimos el string en un array de filas, separándolo por intros
lines=str_data.split("\n")

#La primera línea contiene la cabecera, así que la extraemos
col_names=lines[0].split(",")
n_cols=len(col_names)

#Generamos un diccionario vacío donde irá la información procesada desde la URL externa
counter=0
main_dict={}
for col in col_names:
	main_dict[col]=[]

#Procesamos fila a fila la información para ir rellenando el diccionario con los datos como hicimos antes
for line in lines:
	#Nos saltamos la primera línea que es la que contiene la cabecera y ya tenemos procesada
	if(counter>0):
		#Dividimos cada string por las comas como elemento separador
		values=line.strip().split(",")
		#Añadimos cada valor a su respectiva columna del diccionario
		for i in range(len(col_names)):
			main_dict[col_names[i]].append(values[i])
	counter +=1

print("El data set contiene %d filas y %d columnas"%(counter,n_cols))
print(col_names, n_cols)
print("-----------------------")

#Convertimos el diccionario procesado a Data Frame y comprobamos que los datos son correctos
medals_df=pd.DataFrame(main_dict)
print(medals_df.head())

#Elegimos donde guardarlo
mainpath = "C:/Users/juan_/Documents/GitHub/Machine-Learning/Tema 4 - URL/"
filename = "ejemplo."
fullpath = os.path.join(mainpath,filename)


#Lo guardamos en CSV, en JSON o en EXCEL según queramos
medals_df.to_csv(fullpath + "csv")
medals_df.to_json(fullpath + "json")
medals_df.to_excel(fullpath + "xlsx")

