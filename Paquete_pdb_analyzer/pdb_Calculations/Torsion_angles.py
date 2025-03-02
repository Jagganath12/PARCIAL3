import numpy as np

def get_atom_coords(df, chain, residue, atom):
    try:
        atom_row = df[(df["chain"] == chain) & (df["residue num"] == residue) & (df["atom"] == atom)]
        return atom_row[['x', 'y', 'z']].values[0]
    except IndexError:
        return None

def torsion_angle(a, b, c, d):
    """Calcula el ángulo de torsión entre cuatro puntos en el espacio tridimensional."""
    u1 = np.array(b) - np.array(a)
    u2 = np.array(c) - np.array(b)
    u3 = np.array(d) - np.array(c)
    e = (np.linalg.norm(u2) * u1)
    f = np.cross(u2, u3)
    g = np.cross(u1, u2)
    y = np.dot(e, f)
    x = np.dot(g, f)
    ang = np.arctan2(y, x)
    return np.degrees(ang)

def calculate_phi_psi_omega(df):
    """Calcula ángulos phi, psi y omega para todos los residuos en un DataFrame."""
    angles = []
    for chain in df["chain"].unique():
        for residue in df[df["chain"] == chain]["residue num"].unique():
            residue_name = df[(df["chain"] == chain) & (df["residue num"] == residue)]["residue"].values[0]

            C_ant = get_atom_coords(df, chain, residue - 1, "C")
            N = get_atom_coords(df, chain, residue, "N")
            CA = get_atom_coords(df, chain, residue, "CA")
            C = get_atom_coords(df, chain, residue, "C")
            N_next = get_atom_coords(df, chain, residue + 1, "N")
            C_next = get_atom_coords(df, chain, residue + 1, "CA")

            phi, psi, omega = float(), float(), float()

            if C_ant is not None and N is not None and CA is not None and C is not None:
                phi = round(torsion_angle(C_ant, N, CA, C), 2)

            if N is not None and CA is not None and C is not None and N_next is not None:
                psi = round(torsion_angle(N, CA, C, N_next), 2)

            if CA is not None and C is not None and N_next is not None and C_next is not None:
                omega = round(torsion_angle(CA, C, N_next, C_next), 2)

            if phi != 0.00 and psi != 0.00 and omega != 0.00:
                angles.append((chain, residue, residue_name, phi, psi, omega))

    return angles
