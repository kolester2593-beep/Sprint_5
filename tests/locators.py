from selenium.webdriver.common.by import By

# === ГЛАВНАЯ СТРАНИЦА ===

# Кнопка "Личный Кабинет" на главной странице
button_personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")

# Кнопка "Войти в аккаунт" на главной странице
button_login_main = (By.XPATH, "//button[text()='Войти в аккаунт']")


# === СТРАНИЦА ВХОДА (Login) ===

# Плейсхолдер эмейла на странице входа
label_email_login = (By.XPATH, "//label[text()='Email']")

# Плейсхолдер пароля на странице входа
label_password_login = (By.XPATH, "//label[text()='Пароль']")

# Поле ввода эмейла на странице входа
input_email_login = (By.XPATH, "//input[@name='name']")

# Поле ввода пароля на странице входа
input_password_login = (By.XPATH, "//input[@name='Пароль']")

# Кнопка "Войти" на странице входа 
button_login = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Зарегистрироваться" на странице входа
link_register = (By.XPATH, "//a[text()='Зарегистрироваться']")

# Ссылка "Восстановить пароль" на странице входа
link_forgot_password = (By.XPATH, "//a[text()='Восстановить пароль']")


# === СТРАНИЦА РЕГИСТРАЦИИ (Register) ===

# Плейсхолдер "Имя" на странице регистрации
label_name_register = (By.XPATH, "//label[text()='Имя']")

# Плейсхолдер "Email" на странице регистрации
label_email_register = (By.XPATH, "//label[text()='Email']")

# Плейсхолдер "Пароль" на странице регистрации
label_password_register = (By.XPATH, "//label[text()='Пароль']")

# Поле ввода "Имя" на странице регистрации
input_name_register = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

# Поле ввода "Email" на странице регистрации
input_email_register = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле ввода "Пароль" на странице регистрации
input_password_register = (By.XPATH, "//input[@name='Пароль']")

# Кнопка "Зарегистрироваться" на странице регистрации
button_register = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Информация об ошибке "Некорректный пароль"
error_incorrect_password = (By.XPATH, "//p[text()='Некорректный пароль']")


# === ЛИЧНЫЙ КАБИНЕТ (Profile) ===

# Кнопка "Выйти" в личном кабинете
button_logout = (By.XPATH, "//button[text()='Выход']")

# Кнопка "Конструктор" в личном кабинете
button_constructor = (By.XPATH, "//p[text()='Конструктор']")

# Переход на логотип Stellar Burgers
logo = (By.XPATH, "//a[@href='/' and not(contains(@class, 'AppHeader_header__link'))]")


# === КОНСТРУКТОР ===

# Вкладка "Булки" в конструкторе
tab_buns = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")

# Вкладка "Соусы" в конструкторе
tab_sauces = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")

# Вкладка "Начинки" в конструкторе
tab_fillings = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")


# === СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ (forgot-password) ===

# Плейсхолдер "Email" на странице восстановления
label_email_forgot = (By.XPATH, "//label[text()='Email']")

# Поле ввода "Email" на странице восстановления
input_email_forgot = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Кнопка "Восстановить" на странице восстановления
button_restore = (By.XPATH, "//button[text()='Восстановить']")

# Ссылка "Войти" на странице восстановления
link_login_forgot = (By.XPATH, "//a[@href='/login' and text()='Войти']")


# === СТРАНИЦА СБРОСА ПАРОЛЯ (reset-password) ===

# Плейсхолдер "Пароль" на странице сброса
label_password_reset = (By.XPATH, "//label[text()='Пароль']")

# Плейсхолдер "Введите код из письма" на странице сброса
label_code_reset = (By.XPATH, "//label[text()='Введите код из письма']")

# Поле ввода "Пароль" на странице сброса
input_password_reset = (By.XPATH, "//input[@name='Введите новый пароль']")

# Поле ввода "Код" на странице сброса
input_code_reset = (By.XPATH, "//input[@name='name']")

# Кнопка "Сохранить" на странице сброса
button_save = (By.XPATH, "//button[text()='Сохранить']")

# Ссылка "Войти" на странице сброса
link_login_reset = (By.XPATH, "//a[@href='/login' and text()='Войти']")