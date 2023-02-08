from .base_page import BasePage
from .locators import ListPageLocators, BasketPageLocators


class ListPage(BasePage):
    def add_product_in_basket(self):
        name = self.browser.find_element(*ListPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ListPageLocators.ADD_TO_BASKET), "Basket button doesn't exist"
        self.browser.find_element(*ListPageLocators.ADD_TO_BASKET).click()
        assert self.is_element_present(*ListPageLocators.SELECT_SIZE), "Size button doesn't exist"
        self.browser.find_element(*ListPageLocators.SELECT_SIZE).click()
        assert self.is_element_present(*ListPageLocators.CONTINUE_SHOPPING), "Add notification did not appear"
        self.browser.find_element(*ListPageLocators.CONTINUE_SHOPPING).click()
        self.product_is_in_the_basket(name)
