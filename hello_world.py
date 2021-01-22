import os
import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head())

df.plot()

print('All done')

def numeric_data(x):
    return x * x