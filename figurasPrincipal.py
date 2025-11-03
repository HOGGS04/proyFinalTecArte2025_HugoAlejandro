import pandas as pd
import math

# Leer archivo CSV
dataFile = pd.read_csv("figuras.csv")

areas = []

# Recorre todas las filas del archivo
for index, row in dataFile.iterrows():
    figura = row['FIGURA'].strip().lower()
    m1 = row['MEDIDA1']
    m2 = row['MEDIDA2']

    # Calcular el área según la figura
    if figura == 't':  # triángulo
        area = (m1 * m2) / 2
    elif figura == 'r':  # rectángulo
        area = m1 * m2
    elif figura == 'c':  # círculo
        area = math.pi * (m1 ** 2)
    else:
        area = None

    areas.append(area)

    print(f"Fila {index}: FIGURA = {figura}, Medida1 = {m1}, Medida2 = {m2}, Área = {area}")

# Agrega las áreas al DataFrame
dataFile["AREA"] = areas

# Muestra los resultados finales
print("\nResultados finales:\n", dataFile)

# (Opcional) Guardar el nuevo archivo con los resultados
dataFile.to_csv("figuras_con_areas.csv", index=False)
print("\nArchivo 'figuras_con_areas.csv' creado con éxito.")

