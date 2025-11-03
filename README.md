import pandas as pd

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []


for index, row in dataFile.iterrows():
	if row['FIGURA'] ==t:
		area = triangulo(row['MEDIDA'], row['MEDIDA2'])
	elif row['FIGURA'] == r:
		area = rectangulo(row['MEDIDA'], row['MEDIDA2'])
	elif row['FIGURA'] == c:
		area = circulo(row['MEDIDA'])

	
        print(f"Fila {index}: FIGURA = {row['FIGURA']}, Medida1 = {row['MEDIDA']}, Medida2 = {row['MEDIDA2']}")
