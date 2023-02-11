from pages.product_page import ProductPage
from pages.basket_page import BasketPage


def test_order_without_pay(browser):
    """
    The test checks the ability to make an order (without payment)
    """
    link = "https://www.gloria-jeans.ru/p/GDR026590-1/Zelenoe-pritalennoe-plate-v-rubcik-dla-devocki"
    page = ProductPage(browser, link)
    page.open()
    page.city_notification()
    page.add_product_in_basket()
    link = "https://www.gloria-jeans.ru/cart"
    page = BasketPage(browser, link)
    page.open()
    page.make_an_order()
