from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time


class LoginPage(BasePage):
    def user_login(self):
        self.email = "testhookah"
        self.password = "Test12345!"
        self.input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        self.input_email.send_keys(self.email)
        login_button = self.browser.find_element(
            *LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        self.input_password = self.browser.find_element(
            *LoginPageLocators.PASSWORD)
        self.input_password.send_keys(self.password)
        login_button = self.browser.find_element(
            *LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        
