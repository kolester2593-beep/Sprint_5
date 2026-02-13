from selenium.webdriver.common.by import By

# Лейблы
label_password = (By.XPATH, "//label[text()='Пароль']")
label_code = (By.XPATH, "//label[text()='Введите код из письма']")

# Поля ввода
input_password = (By.XPATH, "//input[@name='Введите новый пароль']")
input_code = (By.XPATH, "//input[@name='name']")

# Кнопки
button_save = (By.XPATH, "//button[text()='Сохранить']")

# Ссылки
link_login = (By.XPATH, "//a[@href='/login' and text()='Войти']")