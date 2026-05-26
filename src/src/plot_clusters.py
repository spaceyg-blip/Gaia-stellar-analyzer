import matplotlib.pyplot as plt

def plot_clusters(
    table
):

    plt.figure(
        figsize=(8,8)
    )

    plt.scatter(
        table[
            "bp_rp"
        ],

        table[
            "abs_mag"
        ],

        c=table[
            "cluster"
        ],

        s=3,

        alpha=0.5
    )

    plt.gca().invert_yaxis()

    plt.xlabel(
        "BP − RP Color"
    )

    plt.ylabel(
        "Absolute Magnitude"
    )

    plt.title(
        "Clustered Gaia HR Diagram"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        "clustered_hr.png",
        dpi=300
    )

    plt.show()
