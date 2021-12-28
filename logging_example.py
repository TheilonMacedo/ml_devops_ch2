import pandas as pd
import logging


logging.basicConfig(
    filename='./logging_example.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def read_data(path):
    """
    Reads data from csv file and returns a pandas dataframe
    
    Parameters:
    path (str): path to csv file
    
    Returns:
    data: pandas dataframe
    
    """
    try:
        df = pd.read_csv(path)
        logging.info(f'SUCCESS: There are {df.shape} rows, cols in the dataframe')
        logging.info('SUCCESS: Data read successfully :)')
        return df
    
    except FileNotFoundError:
        logging.error('ERROR: File not found :(')


df = read_data('/mnt/c/Users/theil/Dropbox/desafio_suzano/vendas_preditas.csv')
df