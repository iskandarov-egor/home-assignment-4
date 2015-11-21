# -*- coding: utf-8 -*-

import unittest
import os
from page import *
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

class ExampleTest(unittest.TestCase):
    # PASSWORD = os.environ['TTHA2PASSWORD']

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        browser = "FIREFOX"

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def t(self):
        print 'hola'
        txt = self.driver
        print type(txt), txt
        return txt != u''

    def test(self):
        self.driver.get("https://cars.mail.ru/")
        main_page = MainPage(self.driver)
        main_page.login_button.click(self.driver)
        main_page.username_field = "testcarspetr"
        main_page.password_field = "seleniumcars"
        main_page.submit_login_form()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: (lambda: d.find_element_by_id("PH_user-email").text != "")()
        )
        elem = self.driver.find_element_by_id("PH_user-email")
        assert "testcarspetr@mail.ru" == elem.text
