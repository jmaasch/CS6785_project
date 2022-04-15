################################################################################
# Filename: coverage.py
# Author: Yi-Yuan Lee
# Date: 04.14.2022
# Update: 04.15.2022
# Description: coverage.py examines the coverage of MOSES molecules in chEMBL.
################################################################################
import pandas as pd
from rdkit import Chem
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
import pickle
from tqdm import tqdm
from os.path import exists

# return a list of intersection
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def main():
    # read file 
    print("Program Start...")
    if exists("../../data/moses_canonical.pkl") and exists("../../data/chembl_canonical.pkl"):
        print("# Caches exists, loading...")
        with open("../../data/moses_canonical.pkl", "rb") as file:
            moses = pickle.load(file)
        with open("../../data/chembl_canonical.pkl", "rb") as file:
            chembl = pickle.load(file)
    else:
        print("# Reading db...")
        moses = pd.read_csv("../../data/db/moses_dataset_v1.csv")["SMILES"].tolist()
        chembl = pd.read_csv("../../data/db/chembl_30_chemreps.txt", sep="\t")["canonical_smiles"].tolist()
        
        # make sure every molecule is in canonical format, remove the ones that 
        # rdkit cannot process.
        to_remove = []
        print("# Cleaning moses...")
        for i in tqdm(range(len(moses))):
            moses[i] = Chem.MolToSmiles(Chem.MolFromSmiles(moses[i]), canonical=True)
        print("# Cleaning chembl...")
        for i in tqdm(range(len(chembl))):
            try:
                chembl[i] = Chem.MolToSmiles(Chem.MolFromSmiles(chembl[i]), canonical=True)
            except:
                print("# Error in canonicalizing: " + chembl[i])
                to_remove.append(chembl[i])
        for ele in to_remove:
            chembl.remove(ele)

        # TODO: should try inchikey, that is more accurate

        # pickle the processed molecules
        with open("../../data/moses_canonical.pkl", "wb") as file:
            pickle.dump(moses, file)
        with open("../../data/chembl_canonical.pkl", "wb") as file:
            pickle.dump(chembl, file)

    # # calculate the intersection
    # print("# Calculating the intersection...")
    # inter = intersection(moses, chembl)
    # print(len(moses), len(set(moses)), len(chembl), len(set(chembl)), len(inter))

    # plot venn
    venn2([set(moses), set(chembl)], set_labels = ('MOSES', 'ChEMBL'))
    plt.savefig("../../outputs/coverage_moses_chembl.pdf")
    venn2([set(moses), set(chembl)], set_labels = ('MOSES', 'ChEMBL'))
    plt.savefig("../../outputs/coverage_moses_chembl.png", dpi=300)

if __name__ == "__main__":
    main()
