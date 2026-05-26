import numpy as np

from src.gaia_query import load_gaia
from src.hr_diagram import plot_hr

from src.cluster_stars import cluster_stars
from src.plot_clusters import plot_clusters

from src.tess_lightcurve import load_lightcurve
from src.find_period import find_period
from src.phase_fold import phase_fold
from src.extract_features import extract_features

# -------------------
# Gaia Section
# -------------------

data = load_gaia()

bp_rp = data[
    "bp_rp"
]

abs_mag = (
    data[
        "phot_g_mean_mag"
    ]
    +
    5
    *
    np.log10(
        data[
            "parallax"
        ]
        /
        1000
    )
    +
    5
)

plot_hr(
    bp_rp,
    abs_mag
)

table = cluster_stars(
    bp_rp,
    abs_mag
)

plot_clusters(
    table
)

data.write(
    "gaia_sample.csv",
    overwrite=True
)

# -------------------
# TESS Section
# -------------------

target = "AB Dor"

lc = load_lightcurve(
    target
)

time = lc.time.value

flux = lc.flux.value

period, frequency, power = find_period(
    time,
    flux
)

phase = phase_fold(
    time,
    period
)

features = extract_features(
    flux
)

print(
    "Recovered Period:",
    period
)

print(
    features
)
