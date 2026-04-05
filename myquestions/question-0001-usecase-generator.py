import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_calcular_ratio_alto_valor():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función calcular_ratio_alto_valor.
    """

    # ---------------------------------------------------------
    # 1. Configuración aleatoria de dimensiones
    # ---------------------------------------------------------
    n_rows = random.randint(10, 20)

    # ---------------------------------------------------------
    # 2. Generar datos aleatorios
    # ---------------------------------------------------------
    df = pd.DataFrame({
        "precio": np.random.randint(10, 100, size=n_rows),
        "cantidad": np.random.randint(1, 10, size=n_rows),
        "categoria": np.random.choice(["A", "B", "C"], size=n_rows)
    })

    # ---------------------------------------------------------
    # 3. Construir INPUT
    # ---------------------------------------------------------
    input_data = {
        "df": df.copy()
    }

    # ---------------------------------------------------------
    # 4. Calcular OUTPUT esperado (Ground Truth)
    # ---------------------------------------------------------

    # A. Calcular valor_total
    valor_total = df["precio"] * df["cantidad"]

    # B. Percentil 75
    p75 = np.percentile(valor_total, 75)

    # C. Filtrar altos valores
    altos = valor_total > p75

    # D. Calcular proporción
    ratio = altos.sum() / len(df)

    output_data = ratio

    return input_data, output_data
