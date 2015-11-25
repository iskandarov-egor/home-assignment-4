# -*- coding: utf-8 -*-

import unittest
import os

from selenium import webdriver

from page_objects_egor.buy_page import *


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
        self.driver.get("https://cars.mail.ru/sale/msk/all/")


    def tearDown(self):
        self.driver.quit()

    def testPriceSort(self):
        page = BuyPage(self.driver)
        page.price_sort_btn.click()

        cards = page.read_cards()
        prices = [x.price for x in cards]
        self.assertTrue(all(prices[i] <= prices[i + 1] for i in range(0, len(prices) - 1)))


    def testRegion(self):
        page = BuyPage(self.driver)
        page.region_btn.click()
        page.region_input.set_value(u'Казань')
        page.city_first_result.click()
        page.submit_region_btn.click()
        page.apply_filter_lnk.click()
        cards = page.read_cards()
        self.assertTrue(all(x.region == u'Казань' for x in cards))