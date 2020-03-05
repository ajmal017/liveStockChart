import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf
import datetime as dt
from datetime import datetime
import asyncio

import gen


ticker = input("Enter a stock ticker: ")
gen.genFile()

now = datetime.now()

current_time = now.strftime("%H, %M, %S")
print(now.hour, now.minute)
start = dt.time(9, 30, 0)
end = dt.time(16, 0, 0)

stock = yf.Ticker(ticker)
price = float(stock.info['ask'])

print(f"{price:.2f}")
print(stock.info)

hist = stock.history(period="max")
print(hist.tail(50))
print(hist.columns)
print(hist["Close"])

# first things first let's replicate fivethirtyeight.com chart style
plt.style.use('fivethirtyeight')

def chart(i):
    print("Running Live Chart")
    
    gen.generate(ticker)

    data = pd.read_csv('stock.csv')
    x = data['x']
    y = data['y']

    #clear current axis
    plt.cla()

    plt.plot(x, y, label=stock.info['symbol'])

    plt.legend(loc='upper left')
    plt.tight_layout()

def historic():
    print("Running Historic Chart")

    y = hist['Close'].tail(50)

    #clear current axis
    plt.cla()

    y.plot(label=stock.info['symbol'], figsize=(16,8), title='50 Day Chart')

    plt.legend(loc='upper left')
    plt.tight_layout()

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

# print(time_in_range(start, end, dt.time(9, 45)))

if time_in_range(start, end, dt.time(now.hour, now.minute)) == True:
    animate = FuncAnimation(plt.gcf(), chart, interval=30000)
else:
    historic()


try:
    plt.tight_layout()
    plt.show()
    # gen.generate(ticker)
    # study ASYNCIO to run these together

except KeyboardInterrupt:
    exit()