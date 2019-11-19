#Garret does not read the comments. I guarantee it.
import pandas as pd
import os

def get_fitbit_data():
    """
    Reads the merged csv in the PWD. Makes it a dataframe. This dataset was made from a BASH script that 
    calls 
    """
    blob = pd.read_csv('blob.csv')
    return blob


# os.system('ls -l')

def get_data(use_cache=True):
    if use_cache and os.path.exists('blob.csv'):
        return pd.read_csv('blob.csv')
    os.system('./make_big_csv.sh')
    return pd.read_csv('blob.csv')


def clean_data(df):
    df = df.set_index('Date')
    for i in df.select_dtypes(include='object').columns:
        print(i)
        df[i] = df[i].str.replace(',', '')
        df[i] = df[i].astype('float64')
        df.info()
    # df.astype('float64',inplace=True).dtypes

    return df
