# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locators import AuthLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import is_element_present, wrong_email_generator, correct_email_generator
from data import user_login_email, user_login_password
from urls.urls import Urls


class TestAuth:

    def test_auth_login(self, driver):
        driver.get(Urls.desk_url)

        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
            )
        )
        driver.find_element(*AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(
                AuthLocators.INPUT_EMAIL_XPATH
            )
        )
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
        name_user = driver.find_element(*AuthLocators.USER_NAME_XPATH).text
        assert (
            driver.find_element(*AuthLocators.IMAGE_AVATAR_XPATH)
            and name_user == "User."
        )

    def test_auth_create_account(self, driver):
        driver.get(Urls.desk_url)

        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
            )
        )
        driver.find_element(*AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.BUTTON_NO_ACCOUNT_XPATH
            )
        )
        driver.find_element(*AuthLocators.BUTTON_NO_ACCOUNT_XPATH).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.INPUT_PASSWORD_SUBMIT_XPATH
            )
        )
        driver.find_element(*AuthLocators.INPUT_EMAIL_XPATH).send_keys(
            correct_email_generator()
        )
        driver.find_element(*AuthLocators.INPUT_PASSWORD_XPATH).send_keys(
            user_login_password
        )
        driver.find_element(*AuthLocators.INPUT_PASSWORD_SUBMIT_XPATH).send_keys(
            user_login_password
        )
        driver.find_element(*AuthLocators.BUTTON_CREATE_ACCPUNT_XPATH).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.IMAGE_AVATAR_XPATH
            )
        )
        name_user = driver.find_element(*AuthLocators.USER_NAME_XPATH).text
        assert (
            driver.find_element(*AuthLocators.IMAGE_AVATAR_XPATH)
            and name_user == "User."
        )

    def test_auth_create_account_wrong_mask_email(self, driver):
        driver.get(Urls.desk_url)

        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
            )
        )
        driver.find_element(*AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH).click()

        driver.find_element(*AuthLocators.BUTTON_NO_ACCOUNT_XPATH).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(
                AuthLocators.INPUT_PASSWORD_SUBMIT_XPATH
            )
        )
        driver.find_element(*AuthLocators.INPUT_EMAIL_XPATH).send_keys(
            wrong_email_generator()
        )
        driver.find_element(*AuthLocators.INPUT_PASSWORD_XPATH).send_keys(
            user_login_password
        )
        driver.find_element(*AuthLocators.INPUT_PASSWORD_SUBMIT_XPATH).send_keys(
            user_login_password
        )
        driver.find_element(*AuthLocators.BUTTON_CREATE_ACCPUNT_XPATH).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.SPAN_ERROR_XPATH
            )
        )
        name_user = driver.find_element(*AuthLocators.SPAN_ERROR_XPATH).text

        style_email = driver.find_element(
            *AuthLocators.PARENT_INPUT_EMAIL_XPATH
        ).value_of_css_property("border")
        style_password = driver.find_element(
            *AuthLocators.PARENT_INPUT_PASSWORD_XPATH
        ).value_of_css_property("border")
        style_password_submit = driver.find_element(
            *AuthLocators.PARENT_INPUT_PASSWORD_SUBMIT_XPATH
        ).value_of_css_property("border")
        assert (
            style_email == "1px solid rgb(255, 105, 114)"
            and style_password == "1px solid rgb(255, 105, 114)"
            and style_password_submit == "1px solid rgb(255, 105, 114)"
            and name_user == "Ошибка"
        )


    def test_auth_logout(self, driver):
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
        driver.find_element(*AuthLocators.BUTTON_LOGOUT_XPATH).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
            )
        )
        count_elem = is_element_present(driver, AuthLocators.USER_NAME_XPATH)
        assert driver.find_element(
            *AuthLocators.BUTTON_LOGIN_AND_REGISTER_XPATH
        ).is_displayed()

