# CS6785_project
Generative deep learning for SARS-CoV-2 drug discovery.

# Data
* ChEMBL: "chembl_30_chemreps.txt" from https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/
* MOSES: From MOSES Github/data/dataset_v1.csv
  * cleaned with ```sed -i "s/[keyword]//g", keyword=[_scaffolds, train, test]```
* Intersection of molecules between MOSES and ChEMBL (done by code/utils/coverage.py):
  * ![coverage_moses_chembl](https://user-images.githubusercontent.com/11462123/163604506-2a534bc6-4a94-495f-870b-7257ee9ffa1b.png)
  * **NOTE: This result is based on canonicalized SMILES, should also try with Inchikey14.**

# Notes
* 0414 (Ian): I reorganize the files since we are going to have more files/outputs.
* 0415 (Ian): According to the intersection of molecules between MOSES and ChEMBL, we can exlude the overlapping from ChEMBL and train the model with cleaned ChEMBL (for transfer learning). **My concern is, why does ChEMBL not containing most of the molecules from MOSES (ZINC)???**
