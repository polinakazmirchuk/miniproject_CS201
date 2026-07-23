import yfinance as yf #імпортували бібліотеку для роботи з фін.даними з YahooFinance
from strategy import generate_signals
from analytics import calculate_p_and_l
from analytics import visualize

#витягнули з YahooFinance дані про акції Netflix за рік, тикер - код інструменту на біржі (NFLX)
historical_data = yf.download("NFLX", period="1y")
# print(historical_data)

#перевіряємо DataFrame, на наявність відсутніх значень, і видаляємо їх
historical_data_cleaned = historical_data.dropna()

signals = generate_signals(historical_data_cleaned, 9, 50)
p_and_l = calculate_p_and_l(signals)
print(f"Фінансовий результат стратегії за рік: {(p_and_l ['Accumulated return'].iloc[-1]-1)*100:.2f}%") # Беремо останній елемент з колонки Accumulated return. Вираховуємо чи приносить збиток чи прибуток.
calculate_p_and_l(signals)
visualize(signals)