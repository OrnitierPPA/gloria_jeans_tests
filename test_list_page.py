import pytest

from pages.list_page import ListPage

@pytest.mark.basket_tests
def test_add_to_basket_from_product_list(browser):
    link = "https://www.gloria-jeans.ru/c/girls-jeans"
    page = ListPage(browser, link)
    page.open()
    page.city_notification()
    page.add_product_in_basket()
