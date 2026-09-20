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