import pandas as pd
import sqlite3

def load_data(database_path):
    conn = sqlite3.connect(database_path)
    query = "SELECT * FROM sales_data;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    # Convert dates to datetime
    df['date'] = pd.to_datetime(df['date'])
    return df
