from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET = (By.CSS_SELECTOR, "a.header-basket.js-header-minicart")
    ZONE_CHOICE = (By.XPATH, "//div[@class='zone-choice__bottom']/button")


class ListPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//div[@class='listing-item__info'][1]/a\
    /div[@class='listing-item__info-buy-button js-listing-add-to-cart']")
    SELECT_SIZE = (By.XPATH, "//div[@class='sizes-pop-up__sizes']/div[1]")
    CONTINUE_SHOPPING = (By.XPATH, "//div[@class='pop-up-basket__buttons']/div[1]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.listing-item__info > a.listing-item__info-title")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@data-add-in-basket='Добавить в корзину']")
    SELECT_SIZE = (By.CSS_SELECTOR, "div.product-details__sizes-wrapper.custom-scroll.js-add-to-basket-sizes > \
    div.block-size__item.js-size-item:first-child")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.basic-info.js-block-for-shield > div > h1")


class BasketPageLocators:
    PRODUCT_BOX = (By.CSS_SELECTOR, "div.item-card.js-delete-block.js-order-item.js-item-card")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.item-card__description-wrapper > h4 > a > span")
    ORDER_BUTTON = (By.CSS_SELECTOR, "div.order-card.js-info-basket.js-order-info > a")


class OrderPageLocators:
    EMAIL = (By.CSS_SELECTOR, "input.wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-checkout-email")
    COURIER = (By.XPATH, "//div[@data-ext-key='STORE']/div[1]")
    ADDRESS_BOX = (By.CSS_SELECTOR, "input.wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-suggestions-addr.suggestions-input")
    APARTMENT = (By.CSS_SELECTOR, "div.text-input.checkout-recipient__apartment > div > input.wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder")
    NAME_BOX = (By.CLASS_NAME, "wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-dadata-name")
    SURNAME_BOX = (By.CLASS_NAME, "wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-dadata-surname")
    PATRONYMIC = (By.CLASS_NAME, "wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-dadata-patronymic")
    PHONE_BOX = (By.CLASS_NAME, "wrapper-text-zone__input.wrapper-text-zone__input--active-placeholder.js-mask-input")
    ONLINE_PAY = (By.CLASS_NAME, "checkout-payment__container")
    GO_TO_PAY = (By.CSS_SELECTOR, "button.checkout-information__button.press-button.press-button--red-style.press-button--font-normal.js-checkout-submit-button")

