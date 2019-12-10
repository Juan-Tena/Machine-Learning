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

EONIA_url="https://www.emmi-benchmarks.eu/assets/modules/rateisblue/file_processing/publication/processed/hist_EONIA_2019.xls"
EONIA_xls=pd.read_excel(EONIA_url, "EONIA")
print(EONIA_xls)
print("===================================")