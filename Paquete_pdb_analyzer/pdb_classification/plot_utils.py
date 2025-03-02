import seaborn as sns
import matplotlib.pyplot as plt

def generate_ramachandran_plot(angles_df, plot_name):
    """Genera un gráfico de Ramachandran."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="phi", y="psi", data=angles_df, s=15, color="blue", edgecolor="black")
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.xlabel("Phi (φ)")
    plt.ylabel("Psi (ψ)")
    plt.title("Ramachandran Plot")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(plot_name)

def generate_histograms_and_barplots(angles_df, output_prefix):

    hist_plot_name = f"{output_prefix}_residue_histogram.png"
    plt.figure(figsize=(8, 6))
    ax = sns.histplot(angles_df["residue"], color="lightblue")
    for p in ax.patches:
        ax.text(p.get_x() + p.get_width() / 2., p.get_height() + 0.5,
                f'{int(p.get_height())}', ha='center', va='center', fontsize=8)
    plt.xlabel("Residue")
    plt.ylabel("Frequency")
    plt.title("Frequency of Residues")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(hist_plot_name)
    plt.close()

    classification_name = f"{output_prefix}_classification.png"
    plt.figure(figsize=(8, 6))
    sns.countplot(x="classification", data=angles_df, palette="Paired",
                  order=angles_df["classification"].value_counts().index)
    plt.xlabel("Classification")
    plt.ylabel("Frequency")
    plt.title("Residue Classification")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(classification_name)
    plt.close()

    return hist_plot_name, classification_name
