from element import *
from locators import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.username_field = InputElement(MainPageLocators.USERNAME_FIELD, self)
        self.password_field = InputElement(MainPageLocators.PASSWORD_FIELD, self)
        self.login_button = ClickableElement(MainPageLocators.LOGIN_BUTTON, self)
        self.email_field = ClickableElement(MainPageLocators.USER_EMAIL_HREF, self)
        self.logout_button = ClickableElement(MainPageLocators.LOGOUT_BUTTON, self)

    def submit_login_form(self):
        self.driver.find_element(*MainPageLocators.USERNAME_FIELD).submit()


