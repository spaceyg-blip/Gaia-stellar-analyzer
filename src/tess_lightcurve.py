import lightkurve as lk

def load_lightcurve(
    target
):

    search = lk.search_lightcurve(
        target,
        mission="TESS"
    )

    lc = search.download()

    return lc
