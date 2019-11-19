#Garret does not read the comments. I guarantee it.
import pandas as pd
import os

# def get_fitbit_data():
#     """
#     Reads the merged csv in the PWD. Makes it a dataframe. This dataset was made from a BASH script that 
#     calls 
#     """
#     blob = pd.read_csv('blob.csv')
#     return blob


# os.system('ls -l')

def get_data(use_cache=True):
    """
    If the 
    """
    if use_cache and os.path.exists('data.csv'):
        return pd.read_csv('data.csv')
    os.system('./make_big_csv.sh')
    return pd.read_csv('data.csv')


def clean_data(df):
    """
    This will make the date the index. It will also get rid of all the commans in the object dtypes.
    It will also make every object a float.
    Returns a clean, ready to go DataFrame
    """
    df = df.set_index('Date')
    for i in df.select_dtypes(include='object').columns:
        print(i)
        df[i] = df[i].str.replace(',', '')
        df[i] = df[i].astype('float64')
        #df.info()
    # df.astype('float64',inplace=True).dtypes

    return df
