from element import *
from locators import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    username_field = BaseInputElement(MainPageLocators.USERNAME_FIELD)
    password_field = BaseInputElement(MainPageLocators.PASSWORD_FIELD)
    login_button = BaseClickableElement(MainPageLocators.LOGIN_BUTTON)

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def submit_login_form(self):
        self.driver.find_element(*MainPageLocators.USERNAME_FIELD).submit()

