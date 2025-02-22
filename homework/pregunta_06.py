"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t", header=0)
    valores_unicos = df["c4"].unique().tolist()

    valores_mayusculas = []
    for elemento in valores_unicos:
        valores_mayusculas.append(elemento.upper())

    return sorted(valores_mayusculas)
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
