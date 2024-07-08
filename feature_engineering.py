import pandas as pd
import numpy as np
from data_analysis import data_analysis
from scipy import stats
from pandas.api.types import is_numeric_dtype

def feature_engineering():

    data = data_analysis()
    data = data.drop(columns=['Asset_ID', 'Asset_Type'],axis=1)
    print(data.head())
    data.to_csv("cleaned_power_distribution_data.csv",index=True)
    return data

feature_engineering()
