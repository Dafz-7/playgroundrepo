import pandas as pd

data = pd.read_csv("GooglePlayStore_wild.csv")

print("Data introduction:")
print()
print(data)
print()
print(data.describe())
print()
print(data.info())
print()

print("Check data nullification:")
print(data.isnull().sum())
print()

print("A. Filling (Rating)'s nullified data with the mean of itself:")
mean_rating = data["Rating"].mean()
data["Rating"] = data["Rating"].fillna(mean_rating)
print()
print("mean_rating = data[\"Rating\"].mean()")
print("data[\"Rating\"] = data[\"Rating\"].fillna(mean_rating)")
print()

print("B. Filling (Type)'s nullified data with the mode of itself:")
print()
mode_type = data["Type"].mode()[0]
data["Type"] = data["Rating"].fillna(mode_type)
print("mode_type = data[\"Type\"].mode()[0]")
print("data[\"Type\"] = data[\"Rating\"].fillna(mode_type)")
print()

print("C. Filling (Current Ver)'s nullified data with the mode of itself:")
print()
mode_currentver = data["Current Ver"].mode()[0]
data["Current Ver"] = data["Rating"].fillna(mode_currentver)
print("mode_currentver = data[\"Current Ver\"].mode()[0]")
print("data[\"Current Ver\"] = data[\"Rating\"].fillna(mode_currentver)")
print()

print("D. Filling (Android Ver)'s nullified data with the mode of itself:")
print()
mode_androidver = data["Android Ver"].mode()[0]
data["Android Ver"] = data["Rating"].fillna(mode_androidver)
print("mode_androidver = data[\"Android Ver\"].mode()[0]")
print("data[\"Android Ver\"] = data[\"Rating\"].fillna(mode_androidver)")
print()

print("Repeat data nullification check:")
print(data.isnull().sum())