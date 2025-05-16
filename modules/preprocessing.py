import pandas as pd

def preprocess_data(df):
    df = df.dropna(axis=0, how='any')
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values('Date')
    return df
