#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://cars.mail.ru/")
elem = driver.find_element_by_id("PH_authLink")
elem.click()
elem = driver.find_element_by_id("ph_login")
elem.send_keys("testcarspetr")
elem = driver.find_element_by_id("ph_password")
elem.send_keys("seleniumcars")
elem.submit()
elem = driver.find_element_by_id("PH_user-email")
assert "testcarspetr@mail.ru" == elem.text
driver.close()
