import time
import pytest

from data.data import Search
from locators.main_page_locators import MainPageLocators
from pages.list_products_page import ListProductsPage

from pages.main_page import MainPage


class TestMain:
    locators = MainPageLocators()

    def test_catalog_products_name(self, driver):
        main = MainPage(driver)
        main.open(MainPageLocators.URL)
        main.show_catalog()
        elements = main.get_elements_list()
        s = []
        for element in elements:
            a = element.text
            s.append(a)
        assert s == self.locators.CATALOG_LIST_PRODUCT_NAME

    def test_product_search_manufacturer_name(self, driver):
        main = MainPage(driver)
        main.open(self.locators.URL)
        main.input_search(Search.manufacturers_name[1])
        list_p = ListProductsPage(driver)
        list_p.item_card_click(1)
        name = list_p.get_title_product()
        res = Search.manufacturers_name[1] in name
        assert res
