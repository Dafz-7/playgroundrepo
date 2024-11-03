import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Bar chart
df1 = data.pivot_table(
    index = 'Content Rating',
    columns = 'Type',
    values = 'Reviews',
    aggfunc = 'mean'
)

df1.plot(kind='barh', grid=True)
plt.show