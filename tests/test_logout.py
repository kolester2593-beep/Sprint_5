from .locators import button_login_main, label_name_register, input_name_register, input_email_register, input_password_register, button_register, link_register, label_email_login, input_email_login, input_password_login, button_login, button_personal_account, button_logout, logo
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Возможно я тут перемудрил но тест большой я его разбил по пунктам, не ругайся)))
base_url = "https://stellarburgers.education-services.ru/"

def test_logout(driver, random_email, random_password):
# 1.Открыть главную страницу
    driver.get(base_url)

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

# 18.Кликнуть на кнопку "Выход"
    driver.find_element(*button_logout).click()

# 19. Дождаться перехода на главную страницу после выхода
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(button_login))

# 20. Проверить, что кнопка "Войти в аккаунт" видна на главной странице
    login_button = driver.find_element(*button_login)
    assert login_button.is_displayed()
