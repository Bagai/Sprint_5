from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import AuthLocators, CreatePost
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import is_element_present
from data import (
    user_login_email,
    user_login_password,
    name_for_post,
    description_for_item,
    cost_of_item,
)


class TestNewPost:

    def test_new_post_by_auth(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                CreatePost.BUTTON_CREATE_POST_XPATH
            )
        )
        driver.find_element(*CreatePost.BUTTON_CREATE_POST_XPATH).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                CreatePost.FORM_WITH_TITLE_AUTH_XPATH
            )
        )
        assert driver.find_element(
            *CreatePost.FORM_WITH_TITLE_AUTH_XPATH
        ).is_displayed()
