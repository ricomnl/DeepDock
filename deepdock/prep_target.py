"""deepdock/prep_target.py"""
import click
from rdkit import Chem

from .prepare_target.computeTargetMesh import compute_inp_surface


@click.command()
@click.option("-t", "--target_file")
@click.option("-l", "--ligand_file")
@click.option("--dist_threshold", default=10)
def main(target_file, ligand_file, dist_threshold):
    if target_file.endswith("mol2"):
        mol = Chem.MolFromMol2File(target_file)
        target_file = target_file.replace("mol2", "pdb")
        with open(target_file, "w") as f:
            f.write(Chem.MolToPDBBlock(mol))
    compute_inp_surface(target_filename=target_file, ligand_filename=ligand_file, dist_threshold=dist_threshold)


if __name__ == "__main__":
    main()