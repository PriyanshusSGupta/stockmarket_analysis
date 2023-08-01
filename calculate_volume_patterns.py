'''
Volume Patterns: Traders often look for specific volume patterns to gain insights into market sentiment. For example, a
steady increase in volume over time may indicate accumulation or distribution by institutional investors. Additionally,
spikes in volume can indicate panic selling or buying frenzies, suggesting potential market extremes.
'''

def calculate_volume_patterns(df):
    # Calculate percentage change in volume
    df['Volume_Change'] = df['Volume'].pct_change()

    # Calculate moving average of volume change
    df['Volume_MA'] = df['Volume_Change'].rolling(window=5).mean()

    # Identify spikes in volume
    df['Volume_Spike'] = (df['Volume_Change'] > 2 * df['Volume_MA']).astype(int)

    # Identify steady increase in volume over time
    df['Volume_Increase'] = (df['Volume_Change'] > df['Volume_Change'].shift(1)).astype(int)
    df = df.fillna(0)
    return df