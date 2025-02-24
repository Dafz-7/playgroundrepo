import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

#* Reading the CSV file
df = pd.read_csv("/Users/dafzz07/Documents/GitHub/My-ProjectLearnings/Python/Machine learning (scikit-learn)/diabetes.csv")
print(df.head())

print()

#* Checking missing values
print(df.isna().sum())

# Handle missing values (example provided but not necessary if you have no missing values)
# Uncomment or modify as needed based on your dataset's requirements

'''
df_dropna_rows = df.dropna()  # Remove rows with missing values
df_dropna_cols = df.dropna(axis=1)  # Remove columns with >60% missing values
df['A'].fillna(df['A'].mean(), inplace=True)  # Fill with mean
df['B'].fillna(df['B'].median(), inplace=True)  # Fill with median
df['C'].fillna(df['C'].mode()[0], inplace=True)  # Fill with mode
'''

#* Convert categorical data to numeric if applicable (not relevant here since it's assumed numeric)

#* Preparing the data
x = df.iloc[:, :-1].values  # Features (assumes last column is the target)
y = df.iloc[:, -1].values  # Target variable

#* Splitting data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

#* Scaling the features
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#* Logistic Regression Model
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)

#* Making predictions
y_pred = classifier.predict(x_test)

#* Predicting a specific instance (ensure it is reshaped to match input shape)
prediksi = classifier.predict(sc.transform([[6, 148, 72, 35, 0, 55.6, 0.625, 50]]))  # Rescale input data
print("Apakah seseorang akan terindikasi Diabetes? (1 = ya, 0 = tidak):", prediksi)

#* Evaluating the model
print("Akurasi:", accuracy_score(y_test, y_pred))
print("Metric Performa Machine Learning")
print(classification_report(y_test, y_pred))