'''
Volume Divergence: Divergence occurs when the price of a stock moves in one direction while volume moves in the opposite direction.
For instance, if a stock is experiencing a significant upward price movement but volume is decreasing, it might signal a lack
of conviction behind the rally, potentially leading to a reversal.
'''

def calculate_volume_divergence(df):
    df['Volume_Divergence'] = None

    for i in range(1, len(df)):
        if df['Close'][i] > df['Close'][i-1] and df['Volume'][i] < df['Volume'][i-1]:
            df['Volume_Divergence'][i] = 'Bearish_Divergence'
        elif df['Close'][i] < df['Close'][i-1] and df['Volume'][i] > df['Volume'][i-1]:
            df['Volume_Divergence'][i] = 'Bullish_Divergence'
        else:
            df['Volume_Divergence'][i] = 'No_Divergence'

    return df