import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    print('/n EDA Report /n')
    print(df.shape)           # Rows & columns
    print(df.columns)         # Column names
    print(df.info())
    print("Missing values:\n", df.isnull().sum())  # Check for missing values
    print("Data types:\n", df.dtypes)  # Check data types
    print("Unique values:\n", df.nunique())  # Check unique values in each column

    return df

def preprocess_data(df):
    df = df.copy()

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

    # Drop string label column if it exists
    if 'AQI_Bucket' in df.columns:
        df = df.drop(columns=['AQI_Bucket'])

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # One-hot encode 'City' if it exists
    if 'City' in df.columns:
        df = pd.get_dummies(df, columns=['City'], drop_first=True)

    # Features to scale
    feature_cols = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']
    scaler = StandardScaler()
    
    # Only scale columns that are present in the data
    for col in feature_cols:
        if col in df.columns:
            df[[col]] = scaler.fit_transform(df[[col]])

    return df
