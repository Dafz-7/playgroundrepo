# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from sklearn.preprocessing import LabelEncoder  # For encoding categorical data
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  # Suppress specific warnings
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression  # For creating a linear regression model
from sklearn.metrics import mean_squared_error  # For calculating the mean squared error metric

# Load data from a CSV file named "Salary_Data.csv"
data = pd.read_csv("TSLA.csv")

# Display the first 5 rows of the data for an overview
print("First 5 rows of the data:")
print(data.head())
print()  # Print a blank line for spacing

# Display the data types of each column (helps to identify categorical vs. numerical data)
print("Data types of each column:")
print(data.dtypes)

# Preprocess the data by identifying and encoding categorical columns
# Select columns with 'object' data type (typically used for categorical data)
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

# Check for any missing values in the data
print()
print("Check for empty values:")
print(data.isna().sum())  # Display the count of missing values for each column

# Fill missing values with the mean of their respective columns (data imputation)
print()
print("Filled empty values:")
print(data.isna().sum())  # Check for missing values again to ensure they are filled

#* Applying a machine learning algorithm: Linear Regression

# Separate the features (x) and the target (y)
x = data.iloc[:, [1, 2, 3, 4]].values  # Select columns 0 to 4 as features (assuming numerical/categorical data)
y = data.iloc[:, [5]].values  # Select column 5 as the target variable

# Split the data into training and testing sets (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Create and fit a linear regression model using the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate model performance
mse = mean_squared_error(y_test, y_pred)
print()
print("Mean Squared Error:", mse)

# Predict a salary using input values (example values provided)
prediksi = model.predict([[1, 0, 177, 4]])
print()
print("Volume prediction:", (round(prediksi[0][0])))  # Round and print the predicted salary value