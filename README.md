# Algorithmic Trading Strategy Using Netflix (NFLX) Stock Data
### Team Members
- Anna Derevianko
- Mariia Bodnarchuk
- Polina Kazmirchuk

This project demonstrates the development of a simple algorithmic
trading model using historical stock market data. Historical prices are collected
from Yahoo Finance, prepared for analysis, and later used to generate
trading signals based on a moving average crossover strategy.

### Why did we choose this instrument (NFLX) for the project?
Netflix (NFLX) was selected, first of all, because we all love watching it, secondly, it is one of
the largest companies in the entertainment industry and its stock price demonstrates
noticeable market fluctuations. Such price movements make Netflix a suitable asset for
testing trading strategies based on moving averages.

### Methods we used for the task and the process of work
1. Data collection: historical stock data for Netflix (NFLX) was downloaded from Yahoo Finance using the ```yfinance``` library. One year
of daily market data was collected.
2. Data Preparation: the data was stored in a Pandas DataFrame, checked for missing values, and cleaned using the ```dropna()``` method to
prepare it for further analysis.
ДОПИСАТИ ІНШІ ІНСТРУМЕНТИ

### Summary of the strategy
пояснення стратегії