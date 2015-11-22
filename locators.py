from selenium.webdriver.common.by import By

class BaseLocator:
    def locate(self, driver):
        pass

class DriverLocator(BaseLocator):
    def __init__(self, locator):
        self.locator = locator

    def locate(self, driver):
        return driver.find_element(*self.locator)

class MainPageLocators:
    USERNAME_FIELD = DriverLocator((By.ID, 'ph_login'))
    PASSWORD_FIELD = DriverLocator((By.ID, 'ph_password'))
    LOGIN_BUTTON = DriverLocator((By.ID, 'PH_authLink'))
    USER_EMAIL_HREF = DriverLocator((By.ID, "PH_user-email"))
    LOGOUT_BUTTON = DriverLocator((By.ID, "PH_logoutLink"))


class OfferCardLocator(BaseLocator):
    def __init__(self, id):
        self.id = id

    def locate(self, driver):
        return driver.find_elements_by_class_name("offer-card")[self.id]


class OfferCardTitleLocator(BaseLocator):
    def __init__(self, card_locator):
        self.card_locator = card_locator

    def locate(self, driver):
        card = self.card_locator.locate(driver)
        return card.find_elements_by_class_name('offer-card__title')[0]