import pandas as pd

def process_pdb(pdb_file):
    """Lee un archivo PDB y extrae las coordenadas atómicas relevantes."""
    data = []
    with open(pdb_file) as file:
        for line in file:
            if line.startswith("ATOM"):
                atom = line[12:16].strip()
                residue = line[17:20].strip()
                chain = line[21].strip()
                res_num = int(line[22:26].strip())
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                data.append([atom, residue, chain, res_num, x, y, z])
    columns = ["atom", "residue", "chain", "residue num", "x", "y", "z"]
    return pd.DataFrame(data, columns=columns)
