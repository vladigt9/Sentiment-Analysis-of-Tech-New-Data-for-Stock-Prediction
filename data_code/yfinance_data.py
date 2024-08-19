import yfinance as yf
import pandas as pd

# select companies needed
ticks = ['MSFT', 'GOOG', 'AAPL', 'META']

# go over all ticks
for t in ticks:
    
    # for each tick select period of hour
    # data is taken a bit far back (november) as some articles at the end of september require it
    tick = yf.Ticker(f'{t}')
    data = tick.history(interval='1h', start="2023-01-01", end="2023-11-01")
    # get only time and open price at that hour
    data = data[['Open']]
    data = data.reset_index()
    data['Datetime'] = data['Datetime'].apply(lambda x: x.replace(second=0).strftime("%Y-%m-%d %H:%M"))

    # save data
    data.to_csv(f'index_data/{t}_index_data.csv', index=False)