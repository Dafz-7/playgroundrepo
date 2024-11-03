import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Bar chart
data1 = data[data['Type']=='Paid'].groupby(by='Content Rating')['Rating'].agg(['mean', 'median', 'max', 'min'])
data1.plot(kind='barh', grid=True)
plt.show()