import pandas as pd
import numpy as np
# from main import historical_data_cleaned

def generate_signals(df: pd.DataFrame, short: int = 20, long: int = 100)-> pd.DataFrame:
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

# # передаємо очищені дані в функцію
# df_with_signals = generate_signals(historical_data_cleaned)
#
# # створимо файл для перегляду повного результату
# df_with_signals.to_csv("result.csv", encoding="utf-8")

# тестовий блок, який виконується тільки при прямому запуску цього файлу
if __name__ == "__main__":
    import yfinance as yf
    raw_data = yf.download("NFLX", period="1y")
    historical_data_cleaned = raw_data.dropna()
    df_with_signals = generate_signals(historical_data_cleaned)
    # для перевірки виведемо тільки ті дані, коли купуємо або продаємо
    print("ДНІ З УГОДАМИ")
    trades = df_with_signals[(df_with_signals['Action'] != 0) & (df_with_signals['Action'].notna())]
    print(trades[['Close', 'SMA_fast', 'SMA_slow', 'Signal', 'Action']])
