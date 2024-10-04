import pandas as pd

f = pd.read_csv("../ACTOR_final.csv", usecols=[0, 1, 2, 3], encoding='cp1252')

f.to_csv("ACTOR_final.csv", index=False)
