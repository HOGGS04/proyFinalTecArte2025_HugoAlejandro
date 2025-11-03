import pandas as p
import math

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []


for index, row in dataFile.iterrows():

	figura = row['FIGURA'].strip().upper()
   	m1 = row['MEDIDA1']
    	m2 = row['MEDIDA2']

    	# Calcular según la figura
    	if figura == "r":
        	area = m1 * m2


    	elif figura == "c":
        	area = math.pi * m1 ** 2
        	perimetro = 2 * math.pi * m1

    	elif figura == "t":
        	area = (m1 * m2) / 2


print(f"Fila {index}: FIGURA = {row['FIGURA']}, Medida1 = {row['MEDIDA']}, Medida2 = {row['MEDIDA2']}")	
