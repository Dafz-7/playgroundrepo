import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#* Sample data
df = pd.read_csv('Mall_Customers.csv')

df_cleaned = df.drop(columns=["CustomerID"])
df_cleaned['Gender'] = df_cleaned['Gender'].map({'Male': 0, 'Female': 1})

#* Standardized the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_cleaned)

#* Elbow method to find the optimal number of clusters
inertia = []
for i in range(1, 11): #* Testing 1 to 10 clusters
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)


#* Plot Elbow method
plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

#* Elbow method for Gender vs Annual income
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

print(df)

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-means Clustering (Annual income vs Spending score (1-100))')
plt.show()