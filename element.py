from selenium.webdriver.support.ui import WebDriverWait


class BaseElement(object):
    def __init__(self, locator):
        self.locator = locator

    def get_element(self, driver):
        return driver.find_element(*self.locator)


class BaseInputElement(BaseElement):
    def __set__(self, obj, value):
        driver = obj.driver
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        return self.get_element(driver).get_attribute("value")

    def submit(self, driver):
        self.get_element(driver).submit()


class BaseClickableElement(BaseElement):
    def __init__(self, locator):
        super(BaseClickableElement, self).__init__(locator)

    def click(self, driver):
        element = self.get_element(driver).click()
