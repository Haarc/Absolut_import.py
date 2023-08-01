import time

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

options.add_experimental_option("detach", True)
driver.get("https://absolut-tds.com/")


def login_user():
    driver.set_window_size(1920, 1080)
    # driver.find_element(By.XPATH, "(//span[@class='content-icon'])[1]").click()
    driver.find_element(By.XPATH, "//li[@class='login-icon content']/a[2]").click()
    driver.find_element(By.ID, "login-email").send_keys("info@s-h-shop.ru")
    driver.find_element(By.ID, "login-pass").send_keys("ajhlbr\n")

    time.sleep(10)


def test_args(df):
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
