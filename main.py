import numpy as np

from src.gaia_query import load_gaia
from src.hr_diagram import plot_hr

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

data.write(
    "gaia_sample.csv",
    overwrite=True
)
