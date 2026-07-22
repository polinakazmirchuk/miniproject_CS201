import pandas as pd
import matplotlib.pyplot as plt

def calculate_p_and_l(df: pd.DataFrame):
    data = df.copy() #зробили копію щоб випадково не змінити дані
    data['Market return'] = data['Close'].pct_change() #розрахнок зміни ціни акції за день длч колонки Close
    data['Strategy return'] = data['Market return']*data['Signal'].shift(1) #множимо зміну на стан магазину за минулий день
    data['Strategy return'] = data['Strategy return'].fillna(0) #перший день після зміщення має значення NaN. Замінюємо NaN на 0
    data['Accumulated return'] = (1 + data['Strategy return']).cumprod() #рахуємо накопичений прибуток
    return data



def visualize(df):
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Close'], label='Closing Price', color='purple') #сторили лінію на графіку для closing price
    ax.plot(df.index, df['SMA_fast'], label='Fast MA', color='lightblue') #сторили лінію на графіку для короткострокових ковзних середніх
    ax.plot(df.index, df['SMA_slow'], label='Slow MA', color='lightgreen') #сторили лінію на графіку для довгострокових ковзних середніх

    buy = df[df['Action'] == 1] #знаходимо дні, коли купували акцію
    sell = df[df['Action'] == -1] #знаходимо дні, коли продавали акцію
    ax.scatter(buy.index, buy['Close'], marker = '^', color = 'green', label = 'Buy signal', s=100) #точки купівлі
    ax.scatter(sell.index, sell['Close'], marker = 'v', color = 'red', label = 'Sell signal', s=100) #точки продажу
    ax.set_title('Strategy for NFLX')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    plt.show()



