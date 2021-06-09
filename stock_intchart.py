# -*- coding: utf-8 -*-
"""BBAS3-web.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qh3mgwTBvIdGk5my5YE5QkBuWssS5qe3
"""

!pip install -q chart_studio

# Importing libraries 
import pandas as pd
from pandas.testing import assert_frame_equal
from pandas_datareader import data as web
import plotly.graph_objects as go
import plotly.express as px
import chart_studio.plotly as py
import chart_studio
chart_studio.tools.set_credentials_file(username='********', api_key='********')

# Define 'dataframe' variable
df = pd.DataFrame()

# Choose stock to be analysed
stock = 'BBAS3.SA'
 
# Import data into dataframe
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

df.head()

# Create first instance - candlestick type graph 
trace1 = {
    'x': df.index,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
    'name': 'BBAS3',
    'showlegend': False
}

# Calculate and define moving average of 30 periods
avg_30 = df.Close.rolling(window=30, min_periods=1).mean()

# Calculate and define moving average of 50 periods
avg_50 = df.Close.rolling(window=50, min_periods=1).mean()

# Second instance - avg_30
trace2 = {
    'x': df.index,
    'y': avg_30,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Moving Average of 30 periods'
}

# Third instance - avg_50
trace3 = {
    'x': df.index,
    'y': avg_50,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'Moving Average of 50 periods'
}

# Aggregate all instances and define 'data' variable
data = [trace1, trace2, trace3]

# Config graph layout
layout = go.Layout({
     # Uncoment if you don't wish to plot any weekend gaps     
     #'xaxis' : {
     #   'type': 'category'
     #    },
    'title': {
        'text': 'BBAS3 - BRASIL ON',
        'font': {
            'size': 15
        }
    }
})

# Create Figure and plot
fig = go.Figure(data=data, layout=layout)
fig.write_html("./BBAS3-web.html")
fig.show()

py.iplot(fig, filename = 'BBAS3')