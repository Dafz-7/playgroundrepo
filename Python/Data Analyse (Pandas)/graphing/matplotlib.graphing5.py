import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Bar chart
data['Category'].value_counts().plot(kind='barh', figsize=(10,10))
plt.show()