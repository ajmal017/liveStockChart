import random
import time
import csv
from datetime import datetime
import yfinance as yf
import asyncio

def genFile():
    fields = ["stock", "x", "y"]

    with open ('stock.csv', 'w') as csv_data:
        writer = csv.DictWriter(csv_data, fieldnames=fields)
        writer.writeheader()
    


def generate(ticker):
    fields = ["stock", "x", "y"]

    stock = yf.Ticker(ticker)
    price = float(stock.info['ask'])

    now = datetime.now()

    x = now.strftime("%H:%M:%S")
    y  = price

    with open('stock.csv', 'a') as csv_data:

        price = float(stock.info['ask'])

        now = datetime.now() 

        writer = csv.DictWriter(csv_data, fieldnames=fields)

        data = {
            "stock": stock.info['symbol'],
            "x": x,
            "y": y
        }

        writer.writerow(data)

        print(stock.info['symbol'], x, y)

        x = now.strftime("%H:%M:%S")
        y = price



if __name__ == "__main__":
    try:
        s = "MSFT"
        generate(s)
    except KeyboardInterrupt:
        exit()
