import matplotlib.pyplot as plt
import pandas as pd

#* Sample data:
data = {
    'Category': ['Food', 'Transport', 'Education', 'Entertainment', 'Others'],
    'Expense': [500, 300, 200, 150, 100]
}

df = pd.DataFrame(data)

#* Do the plottin on a pie chart:

plt.figure(figsize=(6,6))
plt.pie(df['Expense'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution")
plt.axis("Equal")
plt.show()