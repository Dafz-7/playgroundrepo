# This python file is comparing three machine learning models: Logical regression, K-Nearest Neighbors, and Random Forest Classification

#* import libraries
import pandas as pd  
from sklearn.preprocessing import LabelEncoder 
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) 
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn.linear_model")
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#* load the csv file
data = pd.read_csv("student_train_transformed.csv")
print("The original data is: 'student_train.csv'")
print("Using the 'student_train_transformed.py' file, the csv file is then converted into 'student_train_transformed.csv'")
print()

print("First 5 rows of the data:")
print(data.head())
print()  

print("Number of data null in each column:")
print(data.isnull().sum())
print()

print("Data types of each column:")
print(data.dtypes)
print()

print("Check for empty values:")
print(data.isna().sum())
print()

#* machine learning model training

#* split the data int X and y
X = data.drop(columns=["result"]).values
y = data["result"].values

#* training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#* three machine learning algorithms inside a function
print("The value of accuracy (max. 1) in producing the results for the 'result' column in the csv:")
print()

# Logistic Regression
def logistic_regression_model(X_train, y_train, X_test, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Logistic Regression Accuracy: {accuracy:.2f}")
    return y_pred

# K-Nearest Neighbors
def knn_model(X_train, y_train, X_test, y_test, n_neighbors=5):
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"K-Nearest Neighbors Accuracy: {accuracy:.2f}")
    return y_pred

# Random Forest Classification
def random_forest_model(X_train, y_train, X_test, y_test, n_estimators=100):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Random Forest Accuracy: {accuracy:.2f}")
    return y_pred

#* calling the functions
logistic_predictions = logistic_regression_model(X_train, y_train, X_test, y_test)
knn_predictions = knn_model(X_train, y_train, X_test, y_test, n_neighbors=5)
random_forest_predictions = random_forest_model(X_train, y_train, X_test, y_test, n_estimators=100)

#* display the results of each machine's predictions
print("\nLogistic Regression Predictions:")
print(logistic_predictions)
print("Evaluation: This model produces mostly 1s for the 'result' column, meaning that higher student will have the chance to succeed.")
print()

print("\nK-Nearest Neighbors Predictions:")
print(knn_predictions)
print("Evaluation: This model produces mostly 0s for the 'result' column, meaning that higher student will have the chance to fail.")
print()

print("\nRandom Forest Predictions:")
print(random_forest_predictions)
print("Evaluation: This model produces mostly 0s for the 'result' column, meaning that higher student will have the chance to fail.")
print()