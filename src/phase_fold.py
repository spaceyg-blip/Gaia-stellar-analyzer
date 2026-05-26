def phase_fold(
    time,
    period
):

    phase = (
        time % period
    ) / period

    return phase
