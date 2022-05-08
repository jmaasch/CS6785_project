# Importations.
import pandas as pd
import numpy as np
from moses_hmm import HMM

# Pickle models.
hmm = HMM()
hmm_active = hmm.load("hmm_active.pkl")
hmm_inactive = hmm.load("hmm_inactive.pkl")

# Generate 1000 de novo SARS-CoV-2 "actives."
de_novo_actives = []
for i in range(100000):
    de_novo = hmm_active.generate_one()
    de_novo_actives.append(de_novo)

# Generate 1000 de novo SARS-CoV-2 "inactives."
de_novo_inactives = []
for i in range(100000):
    de_novo = hmm_inactive.generate_one()
    de_novo_inactives.append(de_novo)

# Export as CSV.
df_de_novo_actives = pd.DataFrame({"SMILES": de_novo_actives,
                                   "Active": [1] * len(de_novo_actives)})
df_de_novo_inactives = pd.DataFrame({"SMILES": de_novo_inactives,
                                     "Active": [0] * len(de_novo_inactives)})
df_de_novo = pd.concat([df_de_novo_actives, df_de_novo_inactives])
df_de_novo.to_csv("hmm_de_novo_200k.csv", index = False)
