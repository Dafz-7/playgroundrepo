# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from sklearn.preprocessing import LabelEncoder  # For encoding categorical data
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  # Suppress specific warnings
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression  # For creating a linear regression model
from sklearn.metrics import mean_squared_error  # For calculating the mean squared error metric

# Load data from a CSV file named "Salary_Data.csv"
data = pd.read_csv("student_train.csv")

# Display the first 5 rows of the data for an overview
print("First 5 rows of the data:")
print(data.head())
print()  # Print a blank line for spacing

categorical_cols = data.select_dtypes(include=['object']).columns

# Initialize a dictionary to store label encoders for each column
label_encoders = {}

# Loop through each categorical column and encode it using LabelEncoder
for col in categorical_cols:
    label_encoders[col] = LabelEncoder()  # Create a LabelEncoder instance for each column
    data[col] = label_encoders[col].fit_transform(data[col])  # Transform and encode the data

# Display the first 5 rows of the transformed data to check encoding
print()
print("Transformed data (first 5 rows):")
print(data.head())

# Save the transformed DataFrame to a new CSV file
data.to_csv("student_train_transformed.csv", index=False)

print("Transformed data has been saved to 'student_train_transformed.csv'.")