from astropy.timeseries import LombScargle
import numpy as np

def find_period(
    time,
    flux
):

    mask = (
        np.isfinite(time)
        &
        np.isfinite(flux)
    )

    time = time[
        mask
    ]

    flux = flux[
        mask
    ]

    frequency, power = LombScargle(
        time,
        flux
    ).autopower(
        minimum_frequency=0.05,
        maximum_frequency=2
    )

    best_frequency = frequency[
        power.argmax()
    ]

    period = (
        1 /
        best_frequency
    )

    return (
        period,
        frequency,
        power
    )
