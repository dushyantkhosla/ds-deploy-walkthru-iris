import os
import pandas as pd

def get_clean_iris():
    """
    If file exists in data/processed/, recover it
    If it doesn't, import and clean it again
    """
    if os.path.exists("data/processed/iris.csv"):
        df = pd.read_csv("data/processed/iris.csv")
        return df
    else:
        df = get_raw_iris()
        df.columns = \
        map(lambda i: ''.join([x for x in i.lower() if x not in './()& ']).replace('cm', ''),
            df.columns)
        return df
