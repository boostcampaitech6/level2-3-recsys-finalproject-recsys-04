import pandas as pd

def df_to_dict(df: pd.DataFrame):
    columns = list(df.columns)
    data = list(df.loc[:].values.tolist())
    dict = {
        "columns":columns,
        "rows":data,
    }
    
    return dict

def list_to_dict(list: list):
    dict = {"list":list}
    
    return dict