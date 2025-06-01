from selenium.webdriver.common.by import By
from data import name_for_post

class AuthLocators:

    BUTTON_LOGIN_AND_REGISTER_XPATH = (
        By.XPATH,
        ".//button[text()='Вход и регистрация']",
    )

    INPUT_EMAIL_XPATH = (By.XPATH, './/input[@name="email"]')
    PARENT_INPUT_EMAIL_XPATH = (By.XPATH, './/input[@name="email"]/..')
    INPUT_PASSWORD_XPATH = (By.XPATH, './/input[@name="password"]')
    PARENT_INPUT_PASSWORD_XPATH = (By.XPATH, './/input[@name="password"]/..')
    INPUT_PASSWORD_SUBMIT_XPATH = (By.XPATH, './/input[@name="submitPassword"]')
    PARENT_INPUT_PASSWORD_SUBMIT_XPATH = (
        By.XPATH,
        './/input[@name="submitPassword"]/..',
    )
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
    DROPDOWN_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'dropDownMenu_arrowDown')]",
    )
    CITY_TO_SELECT_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'dropDownMenu_options')]//span[text()='Москва']/..",
    )

    ITEM_TYPE_TO_SELECT_XPATH = (
        By.XPATH,
        ".//div[contains(@class, 'dropDownMenu_options')]//span[text()='Хобби']/..",
    )
    RADIO_BUTTON_XPATH = (
        By.XPATH,
        ".//input[@value='Б/У']/../div",
    )
    BUTTON_SUBMIT_FORM_XPATH = (By.XPATH, ".//button[text()='Опубликовать']")
    SEARCH_FIELD_XPATH = (By.XPATH, ".//input[@placeholder='Я хочу купить...']")
    PROFILE_TITLE_XPATH = (By.XPATH, ".//h1[text()='Мой профиль']")
    BUTTON_ARROW_RIGHT_XPATH = (
        By.XPATH,
        ".//button[contains(@class, 'arrowButton--right')]",
    )
    MY_POSTS_XPATH = (By.XPATH, ".//div[contains(@class, 'card')]//h2")
    MY_CREATED_POST_XPATH = (
        By.XPATH,
        f".//div[contains(@class, 'card')]//h2[text()='{name_for_post}']",
    )
