from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def get_default_chrome_options():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    return options


options = get_default_chrome_options()
driver = webdriver.Chrome(options=options)

driver.get(
    "https://www.ozon.ru/search/?text=%D0%93%D0%B0%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9+%D0%BD%D0%B0%D0%BF%D0%B8%D1%82%D0%BE%D0%BA+%D0%94%D0%BE%D0%B1%D1%80%D1%8B%D0%B9+%D0%9B%D0%B8%D0%BC%D0%BE%D0%BD-%D0%BB%D0%B0%D0%B9%D0%BC%2C+1%2C5+%D0%BB&from_global=true"
)
sleep(5)

with open("target_name.txt", "r", encoding="utf-8") as f:
    product_name = f.read().strip()

element = driver.find_elements(By.XPATH, "//span[contains(text(), '₽')]")
for el in element:
    text = el.text
    if "до" not in text and "–" not in text:
        with open("costproduct.txt", "w", encoding="utf-8") as f:
            f.write(text[:-2])
            f.flush()
        break
driver.quit()
