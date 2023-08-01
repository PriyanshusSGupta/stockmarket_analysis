'''
Breakouts and Reversals: Volume analysis can be particularly useful when identifying breakouts and reversals. Breakouts occur when a stock's
price moves above a significant resistance level on high volume, indicating a potential trend continuation. Reversals, on the other hand,
often accompany sharp price movements accompanied by a surge in volume.
'''


def volume_analysis(df):
    # Calculate price changes and their direction
    df['Price_Change'] = df['Close'].diff()
    df['Price_Direction'] = df['Price_Change'].apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))

    # Identify breakouts
    df['Breakout'] = 0
    resistance_level = df['High'].rolling(window=5).max()
    breakout_mask = (df['Close'] > resistance_level) & (df['Volume'] > df['Volume'].shift())
    df.loc[breakout_mask, 'Breakout'] = 1

    # Identify reversals
    df['Reversal'] = 0
    sharp_price_change = df['Price_Change'].rolling(window=5).sum()
    reversal_mask = (df['Price_Direction'].diff() != 0) & (df['Volume'] > df['Volume'].shift())
    df.loc[reversal_mask, 'Reversal'] = 1

    # Remove temporary columns
    df = df.drop(['Price_Change', 'Price_Direction'], axis=1)
    df = df.fillna(0)
    return df