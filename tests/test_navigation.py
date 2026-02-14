from .locators import button_login_main, link_register, input_name_register, input_email_register, input_password_register, button_register, input_email_login, input_password_login, button_login, button_personal_account, button_logout, button_constructor, logo, tab_sauces, label_email_login, label_name_register, button_place_order
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .urls import BASE_URL

def test_navigate_to_personal_account(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Войти в аккаунт"    
    driver.find_element(*button_login_main).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михаил")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Дождаться перехода на страницу входа после регистрации
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_login))

# 12.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 13.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 14.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 15.Дождаться перехода на главную страницу после входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 16.Кликнуть на кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 17.Дождаться загрузки личного кабинета кнопка "Выйти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_logout))

# 18.Проверить, что кнопка "Выйти из аккаунта видна 
    login_button = driver.find_element(*button_logout)
    assert login_button.is_displayed()


def test_navigate_to_constructor_from_profile(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Войти в аккаунт"    
    driver.find_element(*button_login_main).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_email_login))
 
# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михаил")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Дождаться перехода на страницу входа после регистрации
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_login))

# 12.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 13.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 14.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 15.Дождаться перехода на главную страницу после входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 16.Кликнуть на кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 17.Дождаться загрузки личного кабинета кнопка "Выйти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_logout))

# 18.Кликнуть на кнопку "Конструктор"
    driver.find_element(*button_constructor).click()

# 19.Дождаться появления Соуса
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(tab_sauces))

# 20.Проверить, что кнопка "Выйти из аккаунта видна 
    tab_sauces_button = driver.find_element(*tab_sauces)
    assert tab_sauces_button.is_displayed()


def test_navigate_to_constructor_via_logo(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Войти в аккаунт"    
    driver.find_element(*button_login_main).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(label_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михаил")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Дождаться перехода на страницу входа после регистрации
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_login))

# 12.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 13.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 14.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 15.Дождаться перехода на главную страницу после входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 16.Кликнуть на кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 17.Дождаться загрузки личного кабинета кнопка "Выйти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_logout))

# 18.Кликнуть по логотипу
    driver.find_element(*logo).click()

# 19.Дождаться перехода на главную страницу после входа кнопка "Оформить заказ"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_place_order))

# 20.Проверить, что кнопка "Оформить заказ" видна на главной странице
    button_order = driver.find_element(*button_place_order)
    assert button_order.is_displayed()
