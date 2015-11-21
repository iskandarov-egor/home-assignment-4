#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from page import MainPage

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://cars.mail.ru/")
main_page = MainPage(driver)
main_page.login_button.click(driver)
main_page.username_field = "testcarspetr"
main_page.password_field = "seleniumcars"
main_page.submit_login_form()

elem = driver.find_element_by_id("PH_user-email")
assert "testcarspetr@mail.ru" == elem.text
driver.close()
