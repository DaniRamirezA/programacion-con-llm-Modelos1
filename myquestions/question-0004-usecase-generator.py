import numpy as np
from sklearn.decomposition import PCA

def generar_caso_de_uso_varianza_explicada_pca():
    """
    Genera un caso de prueba aleatorio (input y output esperado)
    para la función varianza_explicada_pca.
    """

    # ---------------------------------------------------------
    # 1. Generar datos
    # ---------------------------------------------------------
    X = np.random.rand(30, 5)

    # ---------------------------------------------------------
    # 2. INPUT
    # ---------------------------------------------------------
    input_data = {
        "X": X.copy()
    }

    # ---------------------------------------------------------
    # 3. OUTPUT esperado
    # ---------------------------------------------------------
    pca = PCA(n_components=2)
    pca.fit(X)

    varianza_total = pca.explained_variance_ratio_.sum()

    output_data = varianza_total

    return input_data, output_data
