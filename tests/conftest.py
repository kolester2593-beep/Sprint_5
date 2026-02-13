import pytest
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