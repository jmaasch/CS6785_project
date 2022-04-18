# CS6785_project
Generative deep learning for SARS-CoV-2 drug discovery.

# Data
* ChEMBL: "chembl_30_chemreps.txt" from https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
  * ChEMBL is a manually curated database of bioactive molecules with drug-like properties. It brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs.

* MOSES: From MOSES Github/data/dataset_v1.csv
  * cleaned with ```sed -i "s/[keyword]//g", keyword=[_scaffolds, train, test]```
  * MOSES is refined from ZINC (purchasable compounds). The set is based on the ZINC Clean Leads collection. It contains 4,591,276 molecules in total, filtered by molecular weight in the range from 250 to 350 Daltons, a number of rotatable bonds not greater than 7, and XlogP less than or equal to 3.5. We removed molecules containing charged atoms or atoms besides C, N, S, O, F, Cl, Br, H or cycles longer than 8 atoms. The molecules were filtered via medicinal chemistry filters (MCFs) and PAINS filters.

* PubChem: Compounds/ contains	111,262,522	unique chemical structures extracted from contributed PubChem Substance records. (https://ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/XML/)

* Intersection of molecules between MOSES and ChEMBL (done by code/utils/coverage.py):
  * ![coverage_moses_chembl](https://user-images.githubusercontent.com/11462123/163604506-2a534bc6-4a94-495f-870b-7257ee9ffa1b.png)
  * **NOTE: This result is based on canonicalized SMILES, should also try with Inchikey14.**

# Notes
* 0414 (Ian): I reorganize the files since we are going to have more files/outputs.
* 0415 (Ian): According to the intersection of molecules between MOSES and ChEMBL, we can exlude the overlapping from ChEMBL and train the model with cleaned ChEMBL (for transfer learning). **My concern is, why does ChEMBL not containing most of the molecules from MOSES (ZINC)???**
