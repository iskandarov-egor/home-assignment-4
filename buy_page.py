from page import BasePage
from locators import BuyPageLocators, OfferCardLocator, OfferCardTitleLocator
from selenium.webdriver.common.by import By
from element import *

class BuyPage(BasePage):
    OfferCardsXpath = '//span[@class="offer-card"]'
    N_CARDS = 20
    def __init__(self, driver):
        super(BuyPage, self).__init__(driver)
        self.offer_cards = []
        for i in range(0, self.N_CARDS):
            self.offer_cards.append(OfferCard(OfferCardLocator(i), self))

class OfferCard(BaseElement):
    def __init__(self, locator, page):
        super(OfferCard, self).__init__(locator, page)
        self.title = ClickableElement(OfferCardTitleLocator(locator), page)


