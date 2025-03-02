from protein_analysis.calculations.pdb_parser import process_pdb
from protein_analysis.calculations.torsion_angles import calculate_phi_psi_omega
from protein_analysis.classification.residue_types import classify_residue
from protein_analysis.classification.plot_utils import generate_ramachandran_plot
from protein_analysis.reports.pdf_generator import create_pdf

def main():
    pdb_file = "1ewq.pdb"
    prot_pdb = pdb_file.split(".")[0].upper()

    df = process_pdb(pdb_file)
    angles = calculate_phi_psi_omega(df)
    angles_df = pd.DataFrame(angles, columns=["chain", "residue num", "residue", "phi", "psi", "omega"])
    angles_df["classification"] = angles_df["residue"].apply(classify_residue)

    plot_name = f"{prot_pdb}_ramachandran_plot.png"
    generate_ramachandran_plot(angles_df, plot_name)

    create_pdf(prot_pdb, plot_name)

if __name__ == "__main__":
    main()
