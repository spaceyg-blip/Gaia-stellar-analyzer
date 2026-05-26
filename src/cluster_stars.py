from sklearn.cluster import KMeans
import pandas as pd

def cluster_stars(
    bp_rp,
    abs_mag,
    n_clusters=3
):

    table = pd.DataFrame({

        "bp_rp": bp_rp,

        "abs_mag": abs_mag

    })

    table = table.dropna()

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42
    )

    labels = model.fit_predict(
        table
    )

    table[
        "cluster"
    ] = labels

    return table
