import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import time  # для уникальности логина

# === Фикстура 1: браузер ===
@pytest.fixture(scope="function")
def driver():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    yield driver
    driver.quit()

# === Фикстура 2: генератор логина (email) ===
#@pytest.fixture(scope="function")
#def generate_login():
    # логика генерации: имя + временная метка + @example.com
#    return сгенерированный_email

# === Фикстура 3: генератор пароля ===
#@pytest.fixture(scope="function")
#def generate_password():
    # логика генерации: буквы + цифры + спецсимволы
#    return сгенерированный_пароль