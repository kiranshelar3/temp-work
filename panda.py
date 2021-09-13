import pandas as pd

df = pd.read_csv('sample.csv',sep=(","))

print(df)
print(df.head())

df.columns=['Date','log']

df.describe()

df.info()

