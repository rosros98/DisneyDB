import pandas as pd

f = pd.read_csv("../SHOW_final.csv", usecols=[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], encoding='cp1252')

f.to_csv("SHOW_final.csv", index=False)
