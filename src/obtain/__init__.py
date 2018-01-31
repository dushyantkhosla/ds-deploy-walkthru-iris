import os
os.chdir("/home/")

import numpy as np
import pandas as pd

from sklearn.datasets import load_iris

def get_raw_data():
    """If file exists, recover from backup
    If it doesn't, import it again
    """
    if os.path.exists("/home/data/raw/iris.csv"):
        print("Loading from backup")
        return pd.read_csv("/home/data/raw/iris.csv")
    else:
        print("Downloading data")
        df_iris = \
        (pd.concat([
            pd.DataFrame(load_iris().get('data'), columns=load_iris().get('feature_names')),
            pd.DataFrame(load_iris().get('target'), columns=['iris_type'])
        ], axis=1)
         .assign(iris_type = lambda fr: fr['iris_type'].replace({k:v for k, v in enumerate(load_iris().get('target_names'))}))
        )
        return df_iris

    
def get_clean_data():
    """If file exists, recover from backup
    If it doesn't, import and clean it again
    """
    if os.path.exists("/home/data/processed/iris.csv"):
        df = pd.read_csv("/home/data/processed/iris.csv")
        return df
    else:
        df = get_raw_data()
        df.columns = \
        map(lambda i: ''.join([x for x in i.lower() if x not in './()& ']).replace('cm', ''),
            df.columns)
        return df
    