import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* scatter diagram
plt.scatter(data['Size'], data['Rating'])
plt.show()