from selenium.webdriver.common.by import By

# Лейблы
label_email = (By.XPATH, "//label[text()='Email']")
label_password = (By.XPATH, "//label[text()='Пароль']")

# Поля ввода
input_email = (By.XPATH, "//input[@name='name']")
input_password = (By.XPATH, "//input[@name='Пароль']")

# Ссылки
link_register = (By.XPATH, "//a[text()='Зарегистрироваться']")
link_forgot_password = (By.XPATH, "//a[text()='Восстановить пароль']")