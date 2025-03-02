aminoacids = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS",
              "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]
polar = ["ASN", "CYS", "GLN", "SER", "THR"]
polar_pos = ["ARG", "HIS", "LYS"]
polar_neg = ["ASP", "GLU"]
nonpolar_ali = ["ALA", "ILE", "GLY", "LEU", "MET", "PRO", "VAL"]
nonpolar_aro = ["PHE", "TYR", "TRP"]

def classify_residue(residue):
    """Clasifica un residuo según sus propiedades químicas."""
    if residue in polar:
        return "Polar"
    elif residue in polar_pos:
        return "Polar positive charged"
    elif residue in polar_neg:
        return "Polar negative charged"
    elif residue in nonpolar_ali:
        return "Non polar aliphatic"
    elif residue in nonpolar_aro:
        return "Non polar aromatic"
    else:
        return "Unknown"
