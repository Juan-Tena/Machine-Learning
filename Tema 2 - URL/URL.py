#Carga de datos a traves de la función read_csv

import pandas as pd


medals_url="http://winterolympicsmedals.com/medals.csv"
medals_data=pd.read_csv(medals_url)
print(medals_data.head())




