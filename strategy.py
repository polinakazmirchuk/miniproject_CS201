import pandas as pd
import numpy as np
import yfinance as yf
raw_data = yf.download("NFLX", period="1y")
historical_data_cleaned = raw_data.dropna()

def generate_signals(df: pd.DataFrame, short: int, long: int)-> pd.DataFrame:
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

# тестовий блок, який виконується тільки при прямому запуску цього файлу
if __name__ == "__main__":
    # проведемо перевірки по різним періодам
    strategies_to_test = [
        {"short": 9, "long": 50, "file": "result_9_50.csv"},
        {"short": 20, "long": 100, "file": "result_20_100.csv"},
    ]
    for strat in strategies_to_test:
        s_period = strat["short"]
        l_period = strat["long"]
        file_name = strat["file"]

        # генеруємо сигнали для конкретної пари параметрів
        df_signals = generate_signals(historical_data_cleaned, short=s_period, long=l_period)

        # зберігаємо результат у CSV
        df_signals.to_csv(file_name, encoding="utf-8-sig")

        # для перевірки виведемо тільки ті дані, коли купуємо або продаємо
        print(f"ДНІ З УГОДАМИ ДЛЯ СТРАТЕГІЇ SMA ({s_period} / {l_period})")
        trades = df_signals[(df_signals['Action'] != 0) & (df_signals['Action'].notna())]
        print(trades[['Close', 'SMA_fast', 'SMA_slow', 'Signal', 'Action']])
