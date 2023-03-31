from binance.client import Client
from datetime import datetime
import time

# API-ключи для подключения к Binance
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Создание клиента Binance
client = Client(api_key, api_secret)

# Получение информации о последней цене фьючерса ETHUSDT
last_price = float(client.futures_symbol_ticker(symbol="ETHUSDT")['price'])

# Список цен за последний час
prices = [last_price]

# Время начала отслеживания цен
start_time = datetime.now()

while True:
    # Получение информации о последней цене фьючерса ETHUSDT
    current_price = float(client.futures_symbol_ticker(symbol="ETHUSDT")['price'])

    # Добавление текущей цены в список цен за последний час
    prices.append(current_price)

    # Вычисление процентного изменения цены за последний час
    if len(prices) > 60:
        prices.pop(0)
    percent_change = (current_price - prices[0]) / prices[0] * 100

    # Если изменение цены больше или равно 1%, вывести сообщение в консоль
    if abs(percent_change) >= 1:
        print(f"Price change: {percent_change:.2f}% in the last 60 minutes")

    # Ожидание 1 минуты до следующего обновления цены
    time.sleep(60 - (datetime.now() - start_time).seconds % 60)
