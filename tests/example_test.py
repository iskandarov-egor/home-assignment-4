# -*- coding: utf-8 -*-

import unittest
import os
from page import *
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class LoginLogoutTest(unittest.TestCase):
    # PASSWORD = os.environ['TTHA2PASSWORD']

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        browser = "FIREFOX"

        # self.driver = Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        # )
        self.driver = webdriver.Firefox()
        self.driver.get("https://cars.mail.ru/")


    def tearDown(self):
        self.driver.quit()

    def testLoginLogout(self):
        main_page = MainPage(self.driver)
        main_page.login_button.click()
        main_page.username_field.set_value("testcarspetr")
        main_page.password_field.set_value("seleniumcars")
        main_page.submit_login_form()

        self.assertEqual(main_page.email_field.get_value(), "testcarspetr@mail.ru")

        main_page.logout_button.click()
        self.assertEqual(main_page.email_field.get_value(), '')
