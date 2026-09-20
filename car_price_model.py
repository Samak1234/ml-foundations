import pandas as pd

df = pd.read_csv("car_prediction_data.csv")


print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Display statistical summary
print("\nStatistical summary:")
print(df.describe())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset shape after removing duplicates:")
print(df.shape)

# Separate features and target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())

# Remove the car name column
X = X.drop("Car_Name", axis=1)

print("\nFeatures after removing Car_Name:")
print(X.head())

#Convert categorical columns into numerical columns 

X = pd.get_dummies(X,drop_first =True)

print("\n Features after encoding")
print(X.head())

print("\n Features columns")
print(X.columns)

print("\n Features data types")
print(X.dtypes)

# Split the dataset into training (80%) and testing (20%) sets
from sklearn.model_selection import train_test_split

X_train, X_test , y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Import the Linear Regression model
from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

print("Model training completed!")