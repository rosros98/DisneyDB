import pandas as pd

f = pd.read_csv("../DIRECTOR_final.csv", usecols=[0, 1, 2], encoding='cp1252')

f.to_csv("DIRECTOR_final.csv", index=False)