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


class CreatePost:
    BUTTON_CREATE_POST_XPATH = (By.XPATH, ".//button[text()='Разместить объявление']")
    FORM_WITH_TITLE_AUTH_XPATH = (
        By.XPATH,
        ".//form//h1[text()='Чтобы разместить объявление, авторизуйтесь']",
    )
    INPUT_POST_XPATH = (By.XPATH, ".//input[@name='name']")
    TEXTAREA_DESCRIPTION_FOR_ITEM_XPATH = (By.XPATH, ".//textarea[@name='description']")
    INPUT_COST_OF_ITEM_XPATH = (By.XPATH, ".//input[@name='price']")
    DROPDOWN_CITY_XPATH = (
        By.XPATH,
        ".///button[@class='dropDownMenu_arrowUp__I25Xq dropDownMenu_noDefault__wSKsP']",
    )
    CITY_TO_SELECT_XPATH = (
        By.XPATH,
        ".//div[@class='dropDownMenu_options__CmHmm'][1]/button[1]",
    )
