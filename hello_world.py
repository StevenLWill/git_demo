import os
import pandas as pd

sales_df = pd.read_csv("sales_data.csv")

def plot_data(df):
    df.plot()
    return df

print('All done')

def numeric_data(x):
    return x * x


my_list = [1,2,3]

print(my_list)