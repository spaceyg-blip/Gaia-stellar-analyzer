from astroquery.gaia import Gaia

def load_gaia():

    query = """
    SELECT TOP 5000

    source_id,
    bp_rp,
    phot_g_mean_mag,
    parallax

    FROM gaiadr3.gaia_source

    WHERE parallax > 5
    AND bp_rp IS NOT NULL
    """

    job = Gaia.launch_job(
        query
    )

    data = job.get_results()

    return data
