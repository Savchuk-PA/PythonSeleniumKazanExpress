import time

import pytest
from data.data import Auth
from locators.main_page_locators import MainPageLocators
from pages.auth_page import AuthPage
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
