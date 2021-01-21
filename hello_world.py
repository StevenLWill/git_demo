import os
import pandas as pd

sales_df = pd.read_csv("sales_data.csv")

def plot_data(df):
    df.plot()
    return df

print('Success!')