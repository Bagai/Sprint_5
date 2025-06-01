import uuid
from selenium.common.exceptions import NoSuchElementException


def correct_email_generator():
    return f"{uuid.uuid4()}@mail.com"


def wrong_email_generator():
    return f"{uuid.uuid4()}@mail"


def generate_title_post():
    return f"Я тут был ({uuid.uuid4()})"
