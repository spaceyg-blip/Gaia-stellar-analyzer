import numpy as np

from src.gaia_query import load_gaia
from src.hr_diagram import plot_hr

from src.cluster_stars import cluster_stars
from src.plot_clusters import plot_clusters

# Load Gaia sample
data = load_gaia()

# Color index
bp_rp = data[
    "bp_rp"
]

# Absolute magnitude
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

# HR diagram
plot_hr(
    bp_rp,
    abs_mag
)

# Stellar clustering
table = cluster_stars(
    bp_rp,
    abs_mag,
    n_clusters=3
)

# Cluster visualization
plot_clusters(
    table
)

# Save Gaia sample
data.write(
    "gaia_sample.csv",
    overwrite=True
)
