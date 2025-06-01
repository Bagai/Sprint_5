from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import AuthLocators, CreatePost
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# from helpers import is_element_present, generate_title_post, open_page_with_post
from data import (
    user_login_email,
    user_login_password,
    name_for_post,
    description_for_item,
    cost_of_item,
)
from urls.urls import Urls
from time import sleep

class TestNewPost:

    def test_new_post_by_not_auth(self, driver):
        driver.get(Urls.desk_url)
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

    def test_new_post_by_auth(self, driver):

        driver.get(Urls.desk_url)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
            )
        )
        driver.find_element(*AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH).click()

        driver.find_element(*AuthLocators.INPUT_EMAIL_XPATH).send_keys(user_login_email)
        driver.find_element(*AuthLocators.INPUT_PASSWORD_XPATH).send_keys(
            user_login_password
        )
        driver.find_element(*AuthLocators.BUTTON_ENTER_XPATH).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.IMAGE_AVATAR_XPATH
            )
        )

        driver.find_element(*CreatePost.BUTTON_CREATE_POST_XPATH).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.INPUT_POST_XPATH
            )
        )
        driver.find_element(*CreatePost.INPUT_POST_XPATH).send_keys(name_for_post)
        driver.find_element(*CreatePost.TEXTAREA_DESCRIPTION_FOR_ITEM_XPATH).send_keys(
            description_for_item
        )
        driver.find_element(*CreatePost.INPUT_COST_OF_ITEM_XPATH).send_keys(
            cost_of_item
        )
        dropdown_elements = driver.find_elements(*CreatePost.DROPDOWN_XPATH)
        dropdown_elements[1].click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.CITY_TO_SELECT_XPATH
            )
        )
        driver.find_element(*CreatePost.CITY_TO_SELECT_XPATH).click()

        dropdown_elements[0].click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.ITEM_TYPE_TO_SELECT_XPATH
            )
        )
        driver.find_element(*CreatePost.ITEM_TYPE_TO_SELECT_XPATH).click()

        driver.find_element(*CreatePost.RADIO_BUTTON_XPATH).click()

        driver.find_element(*CreatePost.BUTTON_SUBMIT_FORM_XPATH).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.SEARCH_FIELD_XPATH
            )
        )

        driver.find_element(*AuthLocators.IMAGE_AVATAR_XPATH).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.PROFILE_TITLE_XPATH
            )
        )
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                CreatePost.BUTTON_ARROW_RIGHT_XPATH
            )
        )
        arrow_right_button = driver.find_element(*CreatePost.BUTTON_ARROW_RIGHT_XPATH)
        driver.execute_script("arguments[0].click();", arrow_right_button)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(CreatePost.MY_POSTS_XPATH)
        )
        is_post_found = driver.find_element(
            *CreatePost.MY_CREATED_POST_XPATH
        ).is_displayed()
        while not is_post_found:
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(
                    CreatePost.MY_POSTS_XPATH
                )
            )
            driver.find_element(*CreatePost.BUTTON_ARROW_RIGHT_XPATH).click()
            is_post_found = driver.find_element(
                *CreatePost.MY_CREATED_POST_XPATH
            ).is_displayed()

        attibute_value = driver.find_element(*CreatePost.MY_CREATED_POST_XPATH).text
        assert attibute_value == name_for_post
