import pandas as pd
import numpy as np
#Library for plotting the CandleStick chart
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
#API for getting BitCoin price history
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

coinRequired = True

while coinRequired:

    try:
        intCoin = 0
        intCoin = int(input("Please type a number between 1 and 3 to select the cryptocurrency: <1> BitCoin (BTC) <2> Ethereum (ETH) <3> Solana (SOL): "))

        match intCoin:
            case 1: 
                strCoin = 'bitcoin'
            case 2:
                strCoin = 'ethereum'
            case 3:
                strCoin = 'solana'

        if intCoin > 0 and intCoin <=3:
            #Gets the BitCoin Historical Prices
            cg = CoinGeckoAPI()
            coinData = cg.get_coin_market_chart_by_id(id=strCoin, vs_currency='usd', days=30)
            coinPricesData = coinData['prices']

            #creates DataFrame with only the relevant fields for the Candlestick chart
            data = pd.DataFrame(coinPricesData, columns=['TimeStamp', 'Price'])

            #Formats the TimeSatmp field
            data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

            candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

            fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                            open=candlestick_data['Price']['first'], 
                            high=candlestick_data['Price']['max'],
                            low=candlestick_data['Price']['min'], 
                            close=candlestick_data['Price']['last'])
                            ])

            fig.update_layout(xaxis_rangeslider_visible=False, title_text= strCoin.upper() + ' Historical CandleSctick Chart-Last 30 Days Prices', title_x=0.5)
            fig.show()

            coinRequired = False
    except ValueError:
        print("Only values 1, 2 and 3 are accepted")
