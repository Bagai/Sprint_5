from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import random
import uuid


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def correct_email_generator():
    return f"{uuid.uuid4()}@mail.com"


@pytest.fixture
def wrong_email_generator():
    return f"{uuid.uuid4()}@mail"
