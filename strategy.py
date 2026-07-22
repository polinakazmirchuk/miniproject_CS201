import pandas as pd
import numpy as np

def genarate_signals(df: pd.DataFrame, short: int = 20, long: int = 100)-> pd.DataFrame:
    data = df.copy() #копія таблиці данних з main
    #рахуємо швидке та повілье просте ковзне середнє
    data["SMA_fast"] = data["Close"].rolling(window=short).mean()
    data["SMA_slow"] = data["Close"].rolling(window=long).mean()


