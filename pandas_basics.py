import pandas as pd

df = pd.DataFrame({"name": ["Filip", "Ana", "Marko", "Sara", "Ivan"],
                   "age": [32, 28, 35, 26, 40],
                   "city": ["Graz", "Vienna", "Zagreb", "Graz", "Vienna"],
                   "salary": [3500, 4200, 3800, 3100, 5000]})

print(df.shape)
print(df[["name", "salary"]])
print(df[df["city"] == "Graz"])
print(df[df["salary"] > 3700])
print(df.describe())