import matplotlib.pyplot as plt

def plot_hr(
    bp_rp,
    abs_mag
):

    plt.figure(
        figsize=(8,8)
    )

    plt.scatter(
        bp_rp,
        abs_mag,
        s=2
    )

    plt.gca().invert_yaxis()

    plt.xlabel(
        "BP − RP"
    )

    plt.ylabel(
        "Absolute Magnitude"
    )

    plt.title(
        "Gaia HR Diagram"
    )

    plt.grid(
        alpha=0.3
    )

    plt.savefig(
        "hr_diagram.png",
        dpi=300
    )

    plt.show()
