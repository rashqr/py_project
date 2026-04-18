import requests
import time

TOKEN = "ТВОЙ_ТОКЕН_БОТА"
CHAT_ID = "ТВОЙ_ЧАТ_ID"
PRODUCT_LINK = "https://www.ozon.ru/..."
FILE_COST = "costproduct.txt"
DELAY = 600


def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Ошибка сети: {e}")


print("Бот запущен. Буду слать отчет каждые 10 минут...")

while True:
    try:
        with open(FILE_COST, "r", encoding="utf-8") as f:
            current_price = f.read().strip()

        if current_price:
            message = (
                f"📊 Отчет по цене\n"
                f"💵 Текущая стоимость: {current_price} ₽\n"
                f"🔗 Ссылка: {PRODUCT_LINK}"
            )

            send_telegram(message)
            print(f"Отчет отправлен: {current_price} ₽")
        else:
            print("Файл с ценой пустой...")

    except FileNotFoundError:
        print(f"Файл {FILE_COST} еще не создан...")
    except Exception as e:
        print(f"Ошибка: {e}")

    time.sleep(DELAY)
