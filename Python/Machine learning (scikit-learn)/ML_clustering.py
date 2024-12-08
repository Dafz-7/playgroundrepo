import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#* Sample data
df = pd.read_csv('crime.csv')

df_features = df.drop('Unnamed: 0', axis=1)

#* Standardized the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_features)

#* Elbow method to find the optimal number of clusters
inertia = []
for i in range(1, 6): #* Testing 1 to 5 clusters, because we only have 5 samples
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)


#* Plot Elbow method
plt.plot(range(1, 6), inertia, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

#* Elbow method for Murder vs Rape
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)

print(df)

plt.scatter(df['Murder'], df['Rape'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Murder')
plt.ylabel('Rape')
plt.title('K-means Clustering (Murder vs Rape)')
plt.show()