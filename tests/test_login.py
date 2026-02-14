from .locators import button_login_main, link_register, input_name_register, input_email_register, input_password_register, button_register, button_personal_account, input_email_login, input_password_login, button_login, button_personal_account, link_login_forgot, button_place_order, logo, link_login_register, link_forgot_password
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .urls import BASE_URL

def test_login_from_main_button(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Войти в аккаунт"    
    driver.find_element(*button_login_main).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михаилыч")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Выходим на главную через лого
    driver.find_element(*logo).click()

# 12.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_login_main))

# 13.Нажать кнопку "Войти в аккаунт"
    driver.find_element(*button_login_main).click()

# 14.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 15.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 16.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 17.Дождаться перехода на главную страницу после входа кнопка "Оформить заказ"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_place_order))

# 18.Проверить, что кнопка "Оформить заказ" видна на главной странице
    button_order = driver.find_element(*button_place_order)
    assert button_order.is_displayed()

def test_login_from_personal_account(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Личный Кабинет" на главной странице    
    driver.find_element(*button_personal_account).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михаааилл")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Выходим на главную через лого
    driver.find_element(*logo).click()

# 12.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 13.Нажать кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 14.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 15.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 16.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 17.Дождаться перехода на главную страницу после входа кнопка "Оформить заказ"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_place_order))

# 18.Проверить, что кнопка "Оформить заказ" видна на главной странице
    button_order = driver.find_element(*button_place_order)
    assert button_order.is_displayed()

def test_login_from_register_page(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Личный Кабинет" на главной странице    
    driver.find_element(*button_personal_account).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михооилл")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Выходим на главную через лого
    driver.find_element(*logo).click()

# 12.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 13.Нажать кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 14.Дождаться ссылку "Зарегистрироваться"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(link_register))

# 15.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 16.Дождаться ссылку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(link_login_register))

# 17.Кликнуть на ссылку "Войти"
    driver.find_element(*link_login_register).click()

# 18.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 19.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 20.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 21.Дождаться перехода на главную страницу после входа кнопка "Оформить заказ"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_place_order))

# 22.Проверить, что кнопка "Оформить заказ" видна на главной странице
    button_order = driver.find_element(*button_place_order)
    assert button_order.is_displayed()

def test_login_from_forgot_password(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(BASE_URL)

# 2.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(logo))

# 3.Кликнуть на кнопку "Личный Кабинет" на главной странице    
    driver.find_element(*button_personal_account).click()

# 4.Дождаться загрузки страницы входа
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_email_login))

# 5.Кликнуть на ссылку "Зарегистрироваться"
    driver.find_element(*link_register).click()

# 6.Дождаться загрузки страницы регистрации   
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(input_name_register))

# 7.Заполнить поле "Имя"
    driver.find_element(*input_name_register).send_keys("Михееаилл")

# 8.Заполнить поле "Email"
    driver.find_element(*input_email_register).send_keys(random_email)

# 9.Заполнить поле "Пароль"
    driver.find_element(*input_password_register).send_keys(random_password)

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()

# 11.Выходим на главную через лого
    driver.find_element(*logo).click()

# 12.Дождаться загрузки главной страницы
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_personal_account))

# 13.Нажать кнопку "Личный Кабинет"
    driver.find_element(*button_personal_account).click()

# 14.Дождаться ссылку "Восстановить пароль"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(link_forgot_password))

# 15.Кликнуть на ссылку "Восстановить пароль"
    driver.find_element(*link_forgot_password).click()

# 16.Дождаться ссылку "Войти"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(link_login_forgot))

# 17.Кликнуть на ссылку "Войти"
    driver.find_element(*link_login_forgot).click()

# 18.Заполнить поле "Email" на странице входа
    driver.find_element(*input_email_login).send_keys(random_email)

# 19.Заполнить поле "Пароль" на странице входа
    driver.find_element(*input_password_login).send_keys(random_password)

# 20.Кликнуть на кнопку "Войти"
    driver.find_element(*button_login).click()

# 21.Дождаться перехода на главную страницу после входа кнопка "Оформить заказ"
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_place_order))

# 22.Проверить, что кнопка "Оформить заказ" видна на главной странице
    button_order = driver.find_element(*button_place_order)
    assert button_order.is_displayed()

    