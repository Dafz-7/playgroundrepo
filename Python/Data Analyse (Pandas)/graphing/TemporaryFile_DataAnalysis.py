import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = pd.read_csv('GooglePlayStore_wild.csv')

plt.figure(figsize=(8, 5))
sns.boxplot(x='Type', y='Rating', data=data)
plt.title('Rating by App Type (Free vs Paid)')
plt.show()