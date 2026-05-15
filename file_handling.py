import pandas as pd

df = pd.read_csv("data.csv")

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())

df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].median())
df.to_csv("output.csv", index=False)

df_output = pd.read_csv("output.csv")
print(df_output)