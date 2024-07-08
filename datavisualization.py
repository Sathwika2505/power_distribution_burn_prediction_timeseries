import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import io
import plotly.graph_objects as go
from PIL import Image
import string
from pandas.api.types import is_numeric_dtype
import datetime as DT
from data_analysis import data_analysis

def data_visualization():
    data = data_analysis()
    columns = ['Current_Load_kW','Voltage_V','Power_Factor', 'Transformer_Temperature_C', 'Transformer_Oil_Level_Percent', 'Failure_Probability']
    
    # Define start and end times for slicing
    start = DT.datetime(2021, 1, 1, 0, 0, 0)
    end = DT.datetime(2021, 1, 31, 23, 0, 0)
    
    for col in columns:
        fig = go.Figure()
        sliced_data = data[(data.index >= start) & (data.index <= end)]
        fig.add_trace(go.Scatter(x=sliced_data.index, y=sliced_data[col], mode='lines', name=col))
        fig.update_layout(title=f"Plot of {col} January 2019", template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"series_{col}_2019_January.jpg")
    
    start = DT.datetime(2021, 2, 1, 1, 0, 0)
    end = DT.datetime(2021, 2, 28, 23, 0, 0)
    
    for col in columns:
        fig = go.Figure()
        sliced_data = data[(data.index >= start) & (data.index <= end)]
        fig.add_trace(go.Scatter(x=sliced_data.index, y=sliced_data[col], mode='lines', name=col))
        fig.update_layout(title=f"Plot of {col} February 2019", template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"series_{col}_2019_February.jpg")
    
    for col in columns:
        fig = px.box(data, y=col)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"box_{col}.jpg")
    
    '''for col in columns:
        fig = ff.create_distplot([data[col].values], group_labels=[col])
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"dist_{col}.jpg")'''
    
    df = data.loc[:, columns]
    y = df.corr().columns.tolist()
    z = df.corr().values.tolist()
    z_text = np.around(z, decimals=4)  # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z, x=y, y=y, annotation_text=z_text, colorscale=px.colors.sequential.Cividis_r, showscale=True)
    fig.update_layout(template='plotly_dark')
    fig.write_image(f"heatmap.jpg")
    
    return data

data_visualization()
