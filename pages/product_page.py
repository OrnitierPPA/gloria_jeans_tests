from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_element_present(*ProductPageLocators.SELECT_SIZE)
        self.browser.find_element(*ProductPageLocators.SELECT_SIZE).click()
        self.product_is_in_the_basket(name)
