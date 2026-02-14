from .locators import tab_buns, tab_sauces, tab_fillings, logo
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

base_url = "https://stellarburgers.education-services.ru/"

def test_fillings_tab(driver):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))
    driver.find_element(*tab_fillings).click()
    fillings_element = driver.find_element(*tab_fillings)
    fillings_classes = fillings_element.get_attribute("class")
    assert "tab_tab_type_current" in fillings_classes


def test_sauces_tab(driver):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))
    driver.find_element(*tab_sauces).click()
    sauces_element = driver.find_element(*tab_sauces)
    sauces_classes = sauces_element.get_attribute("class")
    assert "tab_tab_type_current" in sauces_classes

def test_buns_tab(driver):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))
    driver.find_element(*tab_sauces).click() # т.к. тесты должны быть автономны и запускаются по отдельности и булки открыты изначально при загрузке страницы я добавил первый клик на соусы что бы проверка прошла.
    driver.find_element(*tab_buns).click()
    buns_element = driver.find_element(*tab_buns)
    buns_classes = buns_element.get_attribute("class")
    assert "tab_tab_type_current" in buns_classes