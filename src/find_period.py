from astropy.timeseries import LombScargle

def find_period(
    time,
    flux
):

    frequency, power = LombScargle(
        time,
        flux
    ).autopower(
        minimum_frequency=0.5,
        maximum_frequency=5
    )

    best_frequency = frequency[
        power.argmax()
    ]

    period = 1 / best_frequency

    return (
        period,
        frequency,
        power
    )
