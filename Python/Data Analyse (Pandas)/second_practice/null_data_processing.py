import pandas as pd

data = pd.read_csv("GooglePlayStore_wild.csv")

#* Check the whole entry of the data
print(data)
print(data.info())
print(data.describe())

#* Check if the data has nulls or not (using isna):
print(data.isna().sum())
print()

#* Check if the data has nulls or not (using null):
#print(data.isnull().sum())
#print()

#* Check whether the 60% of the data is null or not:
cek = data["Rating"].isna().sum() / len(data)
print("Percentage of the data that is null: " + str(cek))