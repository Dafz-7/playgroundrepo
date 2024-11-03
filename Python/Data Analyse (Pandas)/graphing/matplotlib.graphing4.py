import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Pie chart
plt.title("Pie Diagram")
sum_category = data['Category'].value_counts().sum()
(data['Category'].value_counts()/sum_category).plot(kind='pie', autopct='%1.1f%%', figsize=(20, 20))
plt.show()