import matplotlib.pyplot as plt

def plot_periodogram(
    frequency,
    power
):

    plt.figure(
        figsize=(10,5)
    )

    plt.plot(
        frequency,
        power
    )

    plt.xlabel(
        "Frequency"
    )

    plt.ylabel(
        "Power"
    )

    plt.title(
        "Lomb–Scargle Periodogram"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "periodogram.png",
        dpi=300
    )

    plt.show()
