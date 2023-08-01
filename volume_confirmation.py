'''
Volume Confirmation: Volume should ideally confirm the price movement. If the price of a stock is rising, higher volume
is generally considered positive, indicating increased buying pressure. Conversely, if the price is falling, higher volume
suggests greater selling pressure
'''


import pandas as pd
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

def getdata(stocksymbols):
    ticker = yf.Ticker(stocksymbols)
    end = date.today()
    start = "2020-01-01"
    df = ticker.history(interval="1d",start=start,end=end)
    df.index = df.index.strftime('%d-%m-%y')
    df.index = pd.to_datetime(df.index, format='%d-%m-%y')
    df = df.loc[:,['Open','High','Low','Close','Volume']]
    df = df.round(2)
    return df

def volume_confirmation(df):
    # Check if the price is rising or falling
    df['Price_Movement'] = df['Close'].diff().fillna(0)
    df['Volume_Confirmation'] = 'No_Volume_Confirmation'

    for i in range(1, len(df)):
        if df['Price_Movement'].iloc[i] > 0 and df['Volume'].iloc[i] > df['Volume'].iloc[i-1]:
            df['Volume_Confirmation'].iloc[i] = 'Positive_Volume_Confirmation'
        elif df['Price_Movement'].iloc[i] < 0 and df['Volume'].iloc[i] > df['Volume'].iloc[i-1]:
            df['Volume_Confirmation'].iloc[i] = 'Negative_Volume_Confirmation'

    # Remove temporary columns
    df = df.drop(['Price_Movement'], axis=1)
    df = df.fillna(0)
    return df