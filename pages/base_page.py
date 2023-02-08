from .locators import BasePageLocators, BasketPageLocators

from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def city_notification(self):
        self.browser.find_element(*BasePageLocators.ZONE_CHOICE).click()

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET).click()

    def product_is_in_the_basket(self, name):
        self.go_to_basket()
        assert self.is_element_present(*BasketPageLocators.PRODUCT_BOX), "Product not in the basket"
        assert self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text.lower() == name.lower(), "Product names do not match"
