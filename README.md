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
1. **Data collection:** historical stock data for Netflix (NFLX) was downloaded from Yahoo Finance using the ```yfinance``` library. One year
of daily market data was collected.
2. **Data Preparation:** the data was stored in a Pandas DataFrame, checked for missing values, and cleaned using the ```dropna()``` method to
prepare it for further analysis.
3. **Strategy implementation and Signal generation:** We created the `generate_signals()` function using `pandas` and `numpy` to compute moving averages and determine precise market signals:
   * Computed a fast 20-day Simple Moving Average (`SMA_fast`) and a slow 100-day Simple Moving Average (`SMA_slow`).
   * Generated market state indicators (`Signal`) and detected specific buy/sell trade execution points (`Action`) using `.diff()`.
4. **Export and Verification:** Evaluated the generated trade points and saved the clean, processed dataset to a `result.csv` file for easy review and further backtesting.
5. **P&L Analysis:** We created a `calculate_p_and_l()` function to evaluate the total financial return of our strategy, tracking profit and loss based on generated trading actions.
6. **Data visualization:** We developed a `visualize()` function using  `matplotlib.pyplot` library to plot the stock's closing price alongside fast and slow moving averages, marking buy (`green triangles (^)`) and sell (`red triangles (v)`) signals directly on the chart.

### Summary of the strategy
The core logic of our project relies on the **Simple Moving Average (SMA) Crossover** strategy, which is a classic trend-following technique used in technical analysis:

* **Bullish Trend (Buy Signal : Action = +1):** Occurs when the short-term average (`SMA_fast`) crosses above the long-term average (`SMA_slow`). This indicates rising momentum and signals the algorithm to buy the stock.
* **Bearish Trend (Sell Signal : Action = -1):** Occurs when `SMA_fast` drops below `SMA_slow`. This indicates a potential price decline and signals the algorithm to sell or hold cash.
* **Hold (Action = 0):** As long as no crossover happens, we hold our current position without placing unnecessary trades.

### Strategy results
Using `iloc[-1]` for finding the result of the last trading day of the year. As we can see, according to the calculations we got the value `-5.70%`. The minus before the value indicates that the simple SMA crossover strategy was unprofitable for Netflix stock over this one-year period, likely due to false signals during sideways market trends.