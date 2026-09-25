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

#Predict selling prices using the test data
y_pred = model.predict(X_test)

#Display the predicted selling prices 
print("\nPredicted selling prices:")
print(y_pred)

# Compare actual and predicted selling prices
results = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price": y_pred
})

print("\nActual vs Predicted Prices:")
print(results.head(10))


# Import regression evaluation metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# Display model performance
print("\nModel Evaluation Results:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)

results = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price":y_pred
})

# Calculate the difference between actual and predicted prices
results["Error"] = results ["Actual Price"] - results["Predicted Price"]

print("\nPrediction Errors:")
print(results.head(10))

# Calculate the magnitude of each prediction error 
results["Absolute Error"] = results["Error"].abs()

print("\nPrediction Errors with Absolute Values:")
print(results.head(10))

#Find the five predictions with the largest absolute errors 
largest_errors = results.sort_values(
    by="Absolute Error",
    ascending=False
)

print("\nTop 5 Largest Prediction Errors:")
print(largest_errors.head(5))


# Get the row indexes of the five largest prediction errors
worst_indices = largest_errors.head(5).index

# Use those indexes to find the original car information
worst_cars = df.loc[worst_indices]

print("\nCars with the Largest Prediction Errors:")
print(worst_cars)