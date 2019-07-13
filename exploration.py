#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'valeurs_foncieres'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# <a href="https://colab.research.google.com/github/bapronx/valeurs_foncieres/blob/master/valeurs_foncieres.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#%% [markdown]
# #Analyse des valeurs foncières
#%% [markdown]
# On commence par importer les modules d'analyse et télécharger les fichiers

#%%
import numpy as np
import pandas as pd

# get_ipython().system('wget https://www.data.gouv.fr/fr/datasets/r/1be77ca5-dc1b-4e50-af2b-0240147e0346')
# fname = "1be77ca5-dc1b-4e50-af2b-0240147e0346"
fname = "valeursfoncieres-2018.txt"

fid = open(fname, 'r')
df=pd.read_csv(fname,sep='|')
fid.close()


#%%
df.sample(5)
df.columns

#%%
def proc(s):
  if isinstance(s, str):
    return float(s.replace(',', '.'))
  else:
    return s


def remove_out(d):
  m = d.median()
  s = np.abs(d-m).median()
  selec = (d<=(m+2*s)) & (d>=(m-2*s))
  return d[selec]

#%%
key_to_proc = ("Valeur fonciere", "Surface reelle bati", "Code postal")
for key in key_to_proc:
    df[key] = df[key].apply(proc)
df["surf"] = df["Surface reelle bati"]
df["prix"] = df["Valeur fonciere"]
#%%
selec = (df["Type local"]=="Appartement") & (df["Code departement"]==75) & (df["surf"]<200) & (df["prix"]<4e6) & (df["surf"]>20) & (df["prix"]>4e3)
df["prix au m2"] = df["prix"] / df["surf"]

selec2 = (df["Type local"]=="Appartement") & (df["Code departement"]==75)
remove_out(df["prix au m2"][selec]).hist()

selec_app = df["Type local"] == "Appartement"
selec = selec_app & (df["Commune"] == "BOURG-EN-BRESSE")
#%%

def extract_address(df):
    pass

#%%
import numpy as np

#%%


df["Code postal"][np.isnan(df["Code postal"])]=-9999
def clean_str_nan(s):
    if isinstance(s, float) and np.isnan(s):
        return ""
    return s
df["Type de voie"] = df["Type de voie"].apply(clean_str_nan)
df["Voie"] = df["Voie"].apply(clean_str_nan)


#%%
remove_out(df["prix au m2"][selec]).describe()



