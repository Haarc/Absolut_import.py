from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.EdgeOptions()
options.add_argument("--headless")
driver = webdriver.Edge(options=options)

driver.get("https://absolut-tds.com/")


def login_user():
    # driver.find_element(By.XPATH, "(//span[@class='content-icon'])[1]").click()
    # driver.set_window_size(1920, 1080)
    driver.find_element(By.XPATH, "//li[@class='login-icon content']/a[2]").click()
    driver.find_element(By.ID, "login-email").send_keys("info@s-h-shop.ru")
    driver.find_element(By.ID, "login-pass").send_keys("ajhlbr\n")


def test_args(df):
    # Получаем значения столбцов 'Ссылка на товар' и 'Количество' из DataFrame
    urls = df["URL"].tolist()
    quantities = df["Количество"].tolist()

    for url, count in zip(urls, quantities):
        driver.get(url)

        try:
            quantity_input = driver.find_element(By.XPATH, "//*[@name='qty']")
            quantity_input.send_keys(count)

            wait = WebDriverWait(driver, 3)
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='product-qty blue']")
                )
            )

            name_product = driver.find_element(
                By.XPATH, "//h1[@class='banner-title']"
            ).text

            print(f"Товара: {name_product}, в количество: {count} - ДОБАВЛЕН")

        except:
            print(f"Товара: {name_product}\n По ссылке {url} Нет в наличии")

    driver.quit()