# preprocesamiento.py
# Autor: Victoria Nayely
# Proyecto: Preprocesamiento de Ciencia de Datos

import pandas as pd
import numpy as np

def cargar_datos(ruta):
    """Carga un archivo CSV en un DataFrame."""
    try:
        df = pd.read_csv(ruta)
        print(f"Datos cargados correctamente: {df.shape[0]} filas y {df.shape[1]} columnas.")
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def eliminar_nulos(df):
    """Elimina las filas con valores nulos."""
    antes = df.shape[0]
    df = df.dropna()
    print(f"Filas eliminadas: {antes - df.shape[0]}")
    return df

def normalizar_columna(df, columna):
    """Normaliza una columna numérica (Min-Max)."""
    df[columna] = (df[columna] - df[columna].min()) / (df[columna].max() - df[columna].min())
    print(f"Columna '{columna}' normalizada.")
    return df

def codificar_categorica(df, columna):
    """Aplica codificación one-hot a una columna categórica."""
    df = pd.get_dummies(df, columns=[columna])
    print(f"Columna '{columna}' codificada en variables dummy.")
    return df

if __name__ == "__main__":
    print("=== Ejecución de preprocesamiento de datos ===")
    # Ejemplo de uso con dataset ficticio
    ruta = "data/raw/StudentsPerformance.csv"
    df = cargar_datos(ruta)
    if df is not None:
        df = eliminar_nulos(df)
        df = normalizar_columna(df, "math score")
        df = codificar_categorica(df, "gender")
        df.to_csv("data/processed/datos_limpios.csv", index=False)
        print("Datos preprocesados guardados correctamente.")
