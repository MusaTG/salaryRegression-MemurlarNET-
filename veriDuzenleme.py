#%%
import pandas as pd
data = pd.read_excel("output_derKademeSelenium6.xlsx",sheet_name="liste200_cocuk3")
data
# %%
data.maas = data.maas.str.split(".",expand=True)[0]
data.maas = data.maas.str.replace(",","")
sayac=0

takim = data.iloc[:,1:2].values
print(takim)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
takim[:,0] = le.fit_transform(takim[:,0])
print(takim)
#%%
# gosterge=[]
# for i in data.derece:
#     j=data.kademe[sayac]
#     sayac+=1
#     gosterge.append(str(i)+"/"+str(j))
df = pd.DataFrame()
df["Mezun"] = takim[:,0]
df["Derece"] = data.derece
df["Kademe"] = data.kademe
df["HizmetYili"] = data.hizmet
df["72denKucuk"] = data.kcocuk
df["72denBuyuk"] = data.bcocuk
df["Maas"] = data.maas
# df.to_excel("MemurlarNetMaas1.xlsx",index=False)
df
# %%
