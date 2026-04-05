import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_promedio_top3_por_grupo():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función promedio_top3_por_grupo.
    """

    # ---------------------------------------------------------
    # 1. Configuración aleatoria
    # ---------------------------------------------------------
    n_rows = random.randint(10, 20)

    # ---------------------------------------------------------
    # 2. Generar datos
    # ---------------------------------------------------------
    df = pd.DataFrame({
        "usuario": [f"user_{i}" for i in range(n_rows)],
        "grupo": np.random.choice(["A", "B", "C"], size=n_rows),
        "puntuacion": np.random.randint(0, 100, size=n_rows)
    })

    # ---------------------------------------------------------
    # 3. INPUT
    # ---------------------------------------------------------
    input_data = {
        "df": df.copy()
    }

    # ---------------------------------------------------------
    # 4. OUTPUT esperado
    # ---------------------------------------------------------

    # A. Ranking por grupo
    df_copy = df.copy()
    df_copy["ranking"] = df_copy.groupby("grupo")["puntuacion"]\
        .rank(ascending=False, method="min")

    # B. Filtrar top 3
    top3 = df_copy[df_copy["ranking"] <= 3]

    # C. Promedio por grupo
    promedios = top3.groupby("grupo")["puntuacion"].mean()

    # D. Convertir a numpy array
    output_data = promedios.sort_index().to_numpy()

    return input_data, output_data
