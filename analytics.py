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
    ax.plot(df.index, df['Close'], label='Closing Price', color='blue') #сторили лінію на графіку для closing price
