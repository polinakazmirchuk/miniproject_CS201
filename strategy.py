import pandas as pd
import numpy as np

def genarate_signals(df: pd.DataFrame, short: int = 20, long: int = 100)-> pd.DataFrame:
    data = df.copy() # копія таблиці данних з main
    # рахуємо швидке та повілье просте ковзне середнє
    data["SMA_fast"] = data["Close"].rolling(window=short).mean()
    data["SMA_slow"] = data["Close"].rolling(window=long).mean()

    # визначаємо стан ринку(чи він росте, чи падає)
    data["Signal"] = 0.0
    data["Signal"] = np.where(data["SMA_fast"] > data["SMA_slow"], 1.0, 0.0)

    # визначаємо коли треба продавати(-1), коли купувати(+1), а коли чекати(0)
    data["Action"] = data["Signal"].diff()
    return data


