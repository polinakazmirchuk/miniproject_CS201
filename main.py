import yfinance as yf #імпортували бібліотеку для роботи з фін.даними з YahooFinance

#витягнули з YahooFinance дані про акції Netflix за рік, тикер - код інструменту на біржі (NFLX)
historical_data = yf.download("NFLX", period="1y")
# print(historical_data)

#перевіряємо DataFrame, на наявність відсутніх значень, і видаляємо їх
historical_data_cleaned = historical_data.dropna()

