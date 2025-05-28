from selenium.webdriver.common.by import By


class AuthLocators:

    BUTTON_LOGIN_AND_REGISTER_XPATH = (
        By.XPATH,
        ".//button[text()='Вход и регистрация']",
    )

    INPUT_EMAIL_XPATH = (By.XPATH, './/input[@name="email"]')
    INPUT_PASSWORD_XPATH = (By.XPATH, './/input[@name="password"]')
    INPUT_PASSWORD_SUBMIT_XPATH = (By.XPATH, './/input[@name="submitPassword"]')
    BUTTON_NO_ACCOUNT_XPATH = (By.XPATH, ".//button[text()='Нет аккаунта']")
    BUTTON_ENTER_XPATH = (By.XPATH, ".//button[text()='Войти']")
    BUTTON_CREATE_ACCPUNT_XPATH = (By.XPATH, ".//button[text()='Создать аккаунт']")
    IMAGE_AVATAR_XPATH = (
        By.XPATH,
        ".//button[@class='circleSmall']/*[@class='svgSmall']",
    )
    USER_NAME_XPATH = (By.XPATH, ".//*[@class='profileText name']")
    BUTTON_LOGOUT_XPATH = (By.XPATH, ".//button[text()='Выйти']")
    SPAN_ERROR_XPATH = (By.XPATH, ".//span[text()='Ошибка']")

