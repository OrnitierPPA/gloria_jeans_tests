import pytest

from pages.product_page import ProductPage


@pytest.mark.basket_tests
def test_add_to_basket_from_product_page(browser):
    link = "https://www.gloria-jeans.ru/p/GSW005760-3/Molocnyj-ukorocennyj-kardigan-s-ob%22emnymi-rukavami-dla-devoc"
    page = ProductPage(browser, link)
    page.open()
    page.city_notification()
    page.add_product_in_basket()

