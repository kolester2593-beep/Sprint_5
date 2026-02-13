import pytest
import string
from random import randint, choices
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Фикстура для браузера
@pytest.fixture(scope="function")
def driver():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура Генерация уникального логина/email
@pytest.fixture(scope="function")
def generate_email():
    value = randint(1000, 9999)
    email = f'konstantin_45_FQA{value}@yandex.ru'
    return email

#Фикстура Генерация пароля
@pytest.fixture(scope="function")
def generate_password():
    combine = string.ascii_letters + string.digits
    random_string = ''.join(choices(combine, k=7))
    return random_string