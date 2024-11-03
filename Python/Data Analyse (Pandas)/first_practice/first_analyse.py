import pandas as pd
df = pd.read_csv('GoogleApps.csv')

#! Running
print(df.info)
print()
print(df.describe())
print()
pivot_table1 = df.pivot_table(index="Price", columns="Category", values="Rating", aggfunc="mean")
print(pivot_table1)