from .locators import logo, button_login_main, link_register, input_name_register, input_email_register, input_password_register, button_register, button_login, error_incorrect_password, button_personal_account, label_email_login, label_name_register, input_email_login, input_password_login, button_logout
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .urls import BASE_URL

def test_successful_registration(driver, random_email, random_password):
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

# 17.Дождаться загрузки личного кабинета
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_logout))

# 20. Проверить, что кнопка "Выйти" видна на странице профиля
    button_logout_lk = driver.find_element(*button_logout)
    assert button_logout_lk.is_displayed()

def test_incorrect_password_error(driver, random_email):
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
    driver.find_element(*input_password_register).send_keys("12345")

# 10.Кликнуть на кнопку "Зарегистрироваться"
    driver.find_element(*button_register).click()  

# 11.Дождаться появлния об ошибке
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(error_incorrect_password))

# 20. Проверить, сообщение об ошибке присутствует
    error_element = driver.find_element(*error_incorrect_password)
    assert error_element.is_displayed()
    assert "Некорректный пароль" in error_element.text