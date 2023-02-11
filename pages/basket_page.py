import time

from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import BasketPageLocators, OrderPageLocators


class BasketPage(BasePage):
    def make_an_order(self):
        assert self.is_element_present(*BasketPageLocators.ORDER_BUTTON), "Order button doesn't exist"
        self.browser.find_element(*BasketPageLocators.ORDER_BUTTON).click()
        assert self.is_element_present(*OrderPageLocators.EMAIL), "Email box doesn't exist"
        self.browser.find_element(*OrderPageLocators.EMAIL).send_keys("superpochta@mail.ru")
        assert self.is_element_present(*OrderPageLocators.COURIER), "Courier box doesn't exist"
        self.browser.find_element(*OrderPageLocators.COURIER).click()
        assert self.is_element_present(*OrderPageLocators.ADDRESS_BOX), "Address box doesn't exist"
        assert self.is_element_present(*OrderPageLocators.APARTMENT), "Apartment box doesn't exist"
        assert self.is_element_present(*OrderPageLocators.PATRONYMIC), "Patronymic box doesn't exist"
        assert self.is_element_present(*OrderPageLocators.NAME_BOX), "Name box doesn't exist"
        assert self.is_element_present(*OrderPageLocators.SURNAME_BOX), "Surname box doesn't exist"
        assert self.is_element_present(*OrderPageLocators.PHONE_BOX), "Phone box doesn't exist"
        self.browser.find_element(*OrderPageLocators.ADDRESS_BOX).send_keys('г Москва, ул Таганрогская, д 8, кв')
        self.browser.find_element(*OrderPageLocators.ADDRESS_BOX).click()
        self.browser.find_element(*OrderPageLocators.ADDRESS_LIST_1).click()
        self.browser.find_element(*OrderPageLocators.APARTMENT).send_keys('7')
        self.browser.find_element(*OrderPageLocators.NAME_BOX).send_keys('Иван')
        self.browser.find_element(*OrderPageLocators.SURNAME_BOX).send_keys('Иванович')
        self.browser.find_element(*OrderPageLocators.PATRONYMIC).send_keys('Ивановский')
        self.browser.find_element(*OrderPageLocators.PHONE_BOX).send_keys('44126423329')
        assert self.is_element_present(*OrderPageLocators.ONLINE_PAY), "Online pay checkbox doesn't exist"
        self.browser.find_element(*OrderPageLocators.ONLINE_PAY).click()
        assert self.is_element_present(*OrderPageLocators.GO_TO_PAY), "Button pay doesn't exist"
        self.browser.find_element(*OrderPageLocators.GO_TO_PAY).click()
        assert self.is_element_present(*OrderPageLocators.PAYMENT), "The link for payment did not pass"