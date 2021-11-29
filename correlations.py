# Raw Package
import numpy as np
import pandas as pd
from tabulate import tabulate

#Data Source
import yfinance as yf

#Data viz
#import plotly.graph_objs as go


btc = yf.download("BTC", start="2020-01-01", end="2021-06-13")

eth = yf.download("ETH", start="2020-01-01", end="2021-06-13")

print(type(btc))

print(type(eth))

print(tabulate(btc, headers='keys', tablefmt='psql'))

print(tabulate(btc, headers='keys', tablefmt='psql'))

print(type(btc.Open.tolist()))

r = np.corrcoef(btc.Open.tolist(), eth.Open.tolist())

print('Correlation Coefficient of BTC and ETH for Selected Date Range is: ', r)