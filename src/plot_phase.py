import matplotlib.pyplot as plt

def plot_phase(
    phase,
    flux
):

    plt.figure(
        figsize=(8,5)
    )

    plt.scatter(
        phase,
        flux,
        s=2
    )

    plt.xlabel(
        "Phase"
    )

    plt.ylabel(
        "Flux"
    )

    plt.title(
        "Phase Folded Light Curve"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "phase_curve.png",
        dpi=300
    )

    plt.show()
