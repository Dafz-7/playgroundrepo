import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GooglePlayStore_wild.csv", encoding="utf-8")

data.info()
print()

#* Pie chart
type_counts = data['Type'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Type")
plt.axis('equal')
plt.show()

#* Bar chart
grouped_data = data.groupby(['Type', 'Content Rating'])['Reviews'].agg(['mean', 'min', 'max'])
grouped_data.plot(kind='barh', figsize=(10,10), grid=True)
plt.title("Total reviews by type and content rating")
plt.xlabel('Type')
plt.ylabel('Total Reviews')
plt.show()