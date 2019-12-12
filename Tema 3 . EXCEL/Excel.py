#Carga de datos a traves de la función read_csv

import pandas as pd


mainPath="C:/Users/juan_/Documents/GitHub/Machine-Learning/"
filepathTitanic_xls="Tema 3 . EXCEL/titanic3.xls"
filepathTitanic_xlsx="Tema 3 . EXCEL/titanic3.xlsx"

titanic_xls = pd.read_excel(mainPath+filepathTitanic_xls, "titanic3")
titanic_xlsx = pd.read_excel(mainPath+filepathTitanic_xlsx, "titanic3")

print(titanic_xls.head())
print("===================================")
print(titanic_xlsx.head())
print("===================================")

#Permiten convertir un dataframe en otro tipo de fichero
titanic_xls.to_csv(mainPath + "Tema 3 . EXCEL/titanic_csv.csv")
titanic_xls.to_excel(mainPath + "Tema 3 . EXCEL/titanic3_1.xlsx")
titanic_xls.to_json(mainPath + "Tema 3 . EXCEL/titanic3_1.json")
