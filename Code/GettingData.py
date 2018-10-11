# Paolo Mengano, Claude Raisaro
# September 2018

# This file downloads the last 24-hours prices and klines with 30 minutes
# interval for all the cryptocurrencies listed on Binance.com against BTC.


#-----------------------------------------
# Install the python package
# pip install python-binance
from subprocess import call
call(['pip', 'install', 'python-binance'])

#-----------------------------------------
from binance.client import Client # guess
import pandas as pd
import os
import sys
#os.chdir('/Users/paolomengano/Dropbox/1_Zurich/PhD/Second Year/Programming/Project/Code')
cmds = str(sys.argv[0])
in_path = cmds[0:5]
os.chdir(in_path)
from credentials import get_credentials # retrieving password

# Specifying API and secret key
api_key, api_secret = get_credentials()

# Setting some proxies
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}

# Inputs personal credentials into website
client = Client(api_key, api_secret)

#-----------------------------------------

# Downloading the current list of cryptocurrencies listed in binance against BTC
all_tick = client.get_all_tickers()
tick_BTC = []
for i in range(0, len(all_tick)):
    if all_tick[i]['symbol'][-3:] == 'BTC':
        tick_BTC.append(all_tick[i]['symbol'])

# # Downloading current and 24h price for all currencies listed in BTC
# #today_info = list(client.get_ticker(symbol='BTCUSDT'))
# today_info  = []
# for name in tick_BTC:
#     today_info.append(client.get_ticker(symbol=name))
# today_info.append(client.get_ticker(symbol='BTCUSDT'))
# today_prices = pd.DataFrame(today_info)
# #Save in csv format
# today_prices.to_csv('today_prices.csv')

#-----------------------------------------

# Downloading Klines
labels = [
        'Symbol',
        'OpenTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'VolumeTraded',
        'CloseTime',
        'QuoteAssetVolume',
        'NumberTrades',
        'TakerBuyBaseAssetVolume',
        'TakerBuyQuoteAssetVolume',
        'Ignore']
today_klines = pd.DataFrame(columns = labels)
tick_BTC.append('BTCUSDT')
for name in tick_BTC:
    klines = client.get_historical_klines(name, Client.KLINE_INTERVAL_30MINUTE, "1 day ago UTC")
    df_temp = pd.DataFrame(klines, columns = labels[1:len(labels)])
    df_temp['Symbol']=name
    today_klines = today_klines.append(df_temp, sort=True)
#Save in csv format
os.chdir('../')
out_file = str(sys.argv[1])
out_path = out_file[0:5]
if not os.path.exists(out_path):
    os.mkdir(out_path)
today_klines.to_csv(out_file)
