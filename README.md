# Тесты для сайта Stellar Burgers

## Описание проекта
Автоматизированные тесты для сайта заказа бургеров Stellar Burgers. 
Тесты проверяют функциональность сайта: регистрацию, вход, навигацию, работу конструктора и выход из аккаунта.

## Технологии
- Python
- Selenium WebDriver
- pytest
- ChromeDriver

## Описание тестов

### 1. test_constructor.py (3 теста)
Проверка работы раздела "Конструктор":
- `test_fillings_tab` — переход к разделу "Начинки"
- `test_sauces_tab` — переход к разделу "Соусы"
- `test_buns_tab` — переход к разделу "Булки"

### 2. test_login.py (4 теста)
Проверка входа в систему через разные пути:
- `test_login_from_main_button` — вход через кнопку "Войти в аккаунт" на главной
- `test_login_from_personal_account` — вход через кнопку "Личный кабинет"
- `test_login_from_register_page` — вход через форму регистрации
- `test_login_from_forgot_password` — вход через форму восстановления пароля

### 3. test_logout.py (1 тест)
Проверка выхода из системы:
- `test_logout` — регистрация, вход и выход из аккаунта

### 4. test_navigation.py (3 теста)
Проверка навигации по сайту:
- `test_navigate_to_personal_account` — переход в личный кабинет
- `test_navigate_to_constructor_from_profile` — переход в конструктор через кнопку
- `test_navigate_to_constructor_via_logo` — переход в конструктор через логотип

### 5. test_registration.py (2 теста)
Проверка регистрации пользователей:
- `test_successful_registration` — успешная регистрация с валидными данными
- `test_incorrect_password_error` — проверка ошибки при некорректном пароле

=== test session starts ===
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\koles\Desktop\QA_Automation\Sprint_5\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\koles\Desktop\QA_Automation\Sprint_5
collected 13 items                                                                                                                                                                                                             

tests/test_constructor.py::TestConstructor::test_fillings_tab PASSED [  7%]
tests/test_constructor.py::TestConstructor::test_sauces_tab PASSED [ 15%]
tests/test_constructor.py::TestConstructor::test_buns_tab PASSED [ 23%]
tests/test_login.py::TestLogin::test_login_from_main_button PASSED [ 30%]
tests/test_login.py::TestLogin::test_login_from_personal_account PASSED [ 38%]
tests/test_login.py::TestLogin::test_login_from_register_page PASSED [ 46%]
tests/test_login.py::TestLogin::test_login_from_forgot_password [ 53%]
tests/test_logout.py::TestLogout::test_logout PASSED [ 61%]
tests/test_navigation.py::TestNavigation::test_navigate_to_personal_account PASSED [ 69%]
tests/test_navigation.py::TestNavigation::test_navigate_to_constructor_from_profile PASSED [ 76%]
tests/test_navigation.py::TestNavigation::test_navigate_to_constructor_via_logo PASSED [ 84%]
tests/test_registration.py::TestRegistration::test_successful_registration PASSED [ 92%]
tests/test_registration.py::TestRegistration::test_incorrect_password_error PASSED [100%]

=== 13 passed in 100.94s (0:01:40) ===