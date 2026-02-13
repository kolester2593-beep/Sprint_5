from selenium.webdriver.common.by import By

# Кнопки навигации
personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")
login_account = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Вкладки конструктора
bread_constructor = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")
sauces_constructor = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")
filling_constructor = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")

# Логотип
logo_click = (By.XPATH, "//a[@href='/' and not(contains(@class, 'AppHeader_header__link'))]")