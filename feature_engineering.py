import pandas as pd
import numpy as np
from data_analysis import data_analysis
from scipy import stats
from pandas.api.types import is_numeric_dtype

def feature_engineering():

    data = data_analysis()
    data = data.drop(columns=['Asset_ID', 'Asset_Type'],axis=1)
    def remove_outliers(data,par):
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data=data.drop(index=i,inplace=True)
        return data 
    
    for j in data.columns:
        if is_numeric_dtype(data[j]): 
            data = remove_outliers(data,j)
    data = data.resample('D').mean().fillna(method='ffill')
    print(data.head())
    data.to_csv("cleaned_power_distribution_data.csv",index=True)
    return data

feature_engineering()