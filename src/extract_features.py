import numpy as np

def extract_features(
    flux
):

    features = {

        "mean_flux":
        np.mean(flux),

        "std_flux":
        np.std(flux),

        "amplitude":
        np.max(flux)
        -
        np.min(flux),

        "median_flux":
        np.median(flux)

    }

    return features
