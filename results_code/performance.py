import pandas as pd

# read articles and fix date column
articles = pd.read_csv('news_data/guardian_data.csv')
articles['date'] = pd.to_datetime(articles['date'], format='%Y-%m-%dT%H:%M:%SZ')

# read all stocks data
meta = pd.read_csv('index_data/META_index_data.csv')
apple = pd.read_csv('index_data/AAPL_index_data.csv')
goog = pd.read_csv('index_data/GOOG_index_data.csv')
msft = pd.read_csv('index_data/MSFT_index_data.csv')

# get stocks data into list for easier looping
stocks = [meta, apple, goog, msft]

# fix date for all stocks
for s in stocks:
    s['Datetime'] = pd.to_datetime(s['Datetime'], format='%Y-%m-%d %H:%M')

# filter articles to be stock specific
meta_arts = articles[articles['article'].str.contains('Meta', case=False)]
apple_arts = articles[articles['article'].str.contains('Apple', case=False)]
goog_arts = articles[articles['article'].str.contains('Google', case=False)]
msft_arts = articles[articles['article'].str.contains('Microsoft', case=False)]
arts = [meta_arts, apple_arts, goog_arts, msft_arts]

# create temporary lsits to store data of stock prices performance
meta_price_change = []
goog_price_change = []
apple_price_change = []
msft_price_change = []
price_changes = [meta_price_change, apple_price_change, goog_price_change, msft_price_change]

# loop over all indices
for m in range(len(stocks)):
    # loop over all indices for specific stock
    for i in range(len(arts[m])):
        # get prices in 3 hour range after time of publication
        date = arts[m]['date'].iloc[i]
        three_hours_range = pd.Timedelta(hours=3)
        new_prices = stocks[m][(stocks[m]['Datetime'] >= date) & (stocks[m]['Datetime'] <= date + three_hours_range)]
        old_price = stocks[m][(stocks[m]['Datetime'] < date)]
        
        # get the lastest price before article
        old_price = old_price['Open'].iloc[len(old_price)-1]
        
        # if no new prices available, go for the first 3 prices published afterwards
        if new_prices.empty or len(new_prices) == 1:
            new_prices = stocks[m][(stocks[m]['Datetime'] >= date)].head(3)
        
        # calculate average new price
        new_prices = new_prices['Open'].to_list()
        avr_new_price = sum(new_prices)/len(new_prices)
        
        # get change of price in percentage
        per_change = (avr_new_price-old_price)/old_price * 100
        
        # label data based on its performance. 2-positive, 1-neutral, 0-negative
        if per_change > 0.5:
            price_changes[m].append(2)
        elif per_change < -0.5:
            price_changes[m].append(0)
        else:
            price_changes[m].append(1)
        
#create dictionaries to save data
final_meta = {
    'index': meta_arts.index.to_list(),
    'price_changes': meta_price_change
}

final_goog = {
    'index': goog_arts.index.to_list(),
    'price_changes': goog_price_change
}
final_msft = {
    'index': msft_arts.index.to_list(),
    'price_changes': msft_price_change
}
final_apple = {
    'index': apple_arts.index.to_list(),
    'price_changes': apple_price_change
}

# save all of the data
df_meta = pd.DataFrame(final_meta)
df_goog = pd.DataFrame(final_goog)
df_apple = pd.DataFrame(final_apple)
df_msft = pd.DataFrame(final_msft)

df_meta.to_csv('performance_data/pf_meta.csv', index=False)
df_goog.to_csv('performance_data/pf_goog.csv', index=False)
df_msft.to_csv('performance_data/pf_msft.csv', index=False)
df_apple.to_csv('performance_data/pf_apple.csv', index=False)