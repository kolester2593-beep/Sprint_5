from selenium.webdriver.common.by import By

# Лейблы
label_name = (By.XPATH, "//label[text()='Имя']")
label_email = (By.XPATH, "//label[text()='Email']")
label_password = (By.XPATH, "//label[text()='Пароль']")

# Поля ввода
input_name = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
input_email = (By.XPATH, "//label[text()='Email']/following-sibling::input")
input_password = (By.XPATH, "//input[@name='Пароль']")

# Кнопки
button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Сообщения об ошибках
error_incorrect_password = (By.XPATH, "//p[text()='Некорректный пароль']")