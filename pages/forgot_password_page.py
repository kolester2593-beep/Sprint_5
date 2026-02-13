from selenium.webdriver.common.by import By

# Лейблы
label_email = (By.XPATH, "//label[text()='Email']")

# Поля ввода
input_email = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Кнопки
button_restore = (By.XPATH, "//button[text()='Восстановить']")

# Ссылки
link_login = (By.XPATH, "//a[@href='/login' and text()='Войти']")