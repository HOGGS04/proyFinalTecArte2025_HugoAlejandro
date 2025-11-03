import pandas as pd
import math

dataFile = pd.read_csv("figuras.csv")

areas = []

for index, row in dataFile.iterrows():
    figura = row['FIGURA'].strip().lower()
    m1 = row['MEDIDA1']
    m2 = row['MEDIDA2']

    # Calcula el área
    if figura == 't':  # triángulo
        area = (m1 * m2) / 2
    elif figura == 'r':  # rectángulo
        area = m1 * m2
    elif figura == 'c':  # círculo
        area = math.pi * (m1 ** 2)

    areas.append(area)

    print(f"FIGURA = {figura}, Medida1 = {m1}, Medida2 = {m2}, Área = {area}")
