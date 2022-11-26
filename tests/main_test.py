import random
import time
import pytest

from data.data import Search, PageTitle
from locators.main_page_locators import MainPageLocators
from pages.list_products_page import ListProductsPage

from pages.main_page import MainPage


class TestMain:
    locators = MainPageLocators()

    def test_catalog_products_pages_name(self, driver):
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
        rnd = random.randint(0, 5)
        main = MainPage(driver)
        main.open(self.locators.URL)
        main.input_search(Search.manufacturers_name[rnd])
        list_p = ListProductsPage(driver)
        list_p.item_card_click(1)
        name = list_p.get_title_product()
        res = Search.manufacturers_name[rnd] in name
        assert res

    @pytest.mark.parametrize('page_url_num, ex_page_title', [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                                                             (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12),
                                                             (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18),
                                                             (19, 19)])
    def test_title_page(self, driver, page_url_num, ex_page_title):
        main = MainPage(driver)
        main.open(self.locators.page_url[page_url_num])
        ac_title = main.get_title_page()
        ex_title = PageTitle.title_page[ex_page_title]
        assert  ac_title == ex_title
