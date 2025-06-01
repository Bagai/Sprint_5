import uuid
from selenium.common.exceptions import NoSuchElementException

def is_element_present(webdriver, xpath):
    try:
        webdriver.find_element(*xpath)
    except NoSuchElementException:
        return False
    return True


def correct_email_generator():
    return f"{uuid.uuid4()}@mail.com"


def wrong_email_generator():
    return f"{uuid.uuid4()}@mail"


def generate_title_post():
    return f"Я тут был ({uuid.uuid4()})"
