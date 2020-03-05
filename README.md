# liveStockChart
Two Python scripts work together to pull the current stock price per set interval and create a live chart. 
If ran outside of market hours, a 50 Day Chart is shown

The current generator creates a csv file and adds the current price when called from the main function.
The original generator ran an infinite loop to keep the file updated while the chart pulls data from the csv.
I'm currently working on making the program asyncronous so the generator can run infinitely while the chart continues to update.
