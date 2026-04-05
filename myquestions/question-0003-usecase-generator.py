import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def generar_caso_de_uso_mejor_k_clustering():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función mejor_k_clustering.
    """

    # ---------------------------------------------------------
    # 1. Generar datos aleatorios
    # ---------------------------------------------------------
    X = np.random.rand(20, 3)

    # ---------------------------------------------------------
    # 2. INPUT
    # ---------------------------------------------------------
    input_data = {
        "X": X.copy()
    }

    # ---------------------------------------------------------
    # 3. OUTPUT esperado
    # ---------------------------------------------------------

    resultados = {}

    for k in [2, 3, 4]:
        modelo = KMeans(n_clusters=k, n_init=10)
        labels = modelo.fit_predict(X)
        score = silhouette_score(X, labels)
        resultados[k] = score

    mejor_k = max(resultados, key=resultados.get)

    output_data = mejor_k

    return input_data, output_data
