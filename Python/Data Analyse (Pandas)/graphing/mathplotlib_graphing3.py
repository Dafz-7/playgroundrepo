import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Histogram
plt.hist(data['Rating'])
plt.xlabel("Rating")
plt.ylabel("Jumlah masing-masing rating")
plt.title("Grafik persebaran rating")
plt.show()
print()

#* Pie chart
plt.title("Pie Diagram")
sum_category = data['Category'].value_counts().sum()
(data['Category'].value_counts()/sum_category).plot(kind='pie', autopct='%1.1f%%')
plt.show()