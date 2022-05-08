# Importations.
import pandas as pd
import numpy as np
import tdc
from tdc.single_pred import HTS
from moses_hmm import HMM

# Read data.
actives = pd.read_csv("../sars_data/actives_train.csv")
inactives = pd.read_csv("../sars_data/inactives_train.csv")

# Train HMM on actives.
hmm_active = HMM()
hmm_active = hmm_active.fit(actives.SMILES)

# Train HMM on inactives.
hmm_inactive = HMM()
hmm_inactive = hmm_inactive.fit(inactives.SMILES)

# Pickle models.
active_name = "hmm_active.pkl"
inactive_name = "hmm_inactive.pkl"
hmm_active.save(active_name)
hmm_inactive.save(inactive_name)

# Generate 1000 de novo SARS-CoV-2 "actives."
de_novo_actives = []
for i in range(1000):
    de_novo = hmm_active.generate_one()
    de_novo_actives.append(de_novo)

# Generate 1000 de novo SARS-CoV-2 "inactives."
de_novo_inactives = []
for i in range(1000):
    de_novo = hmm_inactive.generate_one()
    de_novo_inactives.append(de_novo)
    
# Export as CSV.
df_de_novo_actives = pd.DataFrame({"SMILES": de_novo_actives,
                                   "Active": [1] * len(de_novo_actives)})
df_de_novo_inactives = pd.DataFrame({"SMILES": de_novo_inactives,
                                     "Active": [0] * len(de_novo_inactives)})
df_de_novo = pd.concat([df_de_novo_actives, df_de_novo_inactives])
df_de_novo.to_csv("hmm_de_novo_2k.csv", index = False)
    
