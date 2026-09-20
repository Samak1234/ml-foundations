import pandas as pd

df = pd.read_csv("car_prediction_data.csv")


print(df.head())
print(df.shape)
print(df.columns)
print(df.info())