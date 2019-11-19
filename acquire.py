#Garret does not read the comments. I guarantee it.
import pandas as pd

def get_fitbit_data():
    """
    Reads a xlsx document in the PWD. Makes it a dataframe.
    """
    blob = pd.read_excel('fitbit_data.xlsx')
    return blob
