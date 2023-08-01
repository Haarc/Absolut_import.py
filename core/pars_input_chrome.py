import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_argument(
    r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data"
)


options.add_experimental_option("detach", True)


def test_args(df):
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1280, 720)

    # Получаем значения столбцов 'Ссылка на товар' и 'Количество' из DataFrame
    urls = df["Ссылка"].tolist()
    quantities = df["Количество"].tolist()

    for url, count in zip(urls, quantities):
        driver.get(url)

        try:
            quantity_input = driver.find_element(By.XPATH, "//*[@name='qty']")
            quantity_input.send_keys(count)
            name_product = driver.find_element(
                By.XPATH, "//h1[@class='banner-title']"
            ).text
            time.sleep(1.9)

            print(f"Товара: {name_product}, в количество: {count} - ДОБАВЛЕН")

        except:
            print(f"Товара: {name_product}\n По ссылке {url} Нет в наличии")

    driver.close()
