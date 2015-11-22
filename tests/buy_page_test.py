# -*- coding: utf-8 -*-

import unittest
import os
from buy_page import *
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BuyPageTest(unittest.TestCase):
    # PASSWORD = os.environ['TTHA2PASSWORD']

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        browser = "FIREFOX"

        # self.driver = Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        # )
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("https://cars.mail.ru/sale/msk/all/")

    def tearDown(self):
        self.driver.quit()

    def testTest(self):
        page = BuyPage(self.driver)
        print page.offer_cards[1].title.get_value()
