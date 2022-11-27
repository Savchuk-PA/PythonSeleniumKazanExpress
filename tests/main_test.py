import random
import time
import pytest
from data.data import Search, PageTitle
from helpers.generators import get_list_num
from helpers.help_get import get_num_in_str
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
        assert ac_title == ex_title

    def test_check_banner_advertisement(self, driver):
        main = MainPage(driver)
        main.open(self.locators.URL)
        block_is_display = main.element_is_visible(self.locators.ADVERTISEMENT_BlOCK).is_displayed()
        assert block_is_display, "Блок с рекламой не отображается на странице"

    @pytest.mark.parametrize('page_url', get_list_num(20))
    def test_check_block_for_selected_color_products_items(self, driver, page_url):
        main = MainPage(driver)
        main.open(self.locators.page_url[page_url])
        block_is_display = main.check_color_block()
        assert block_is_display, "Блок с выбором цвета отсутствует на странице"

    @pytest.mark.xfail
    def test_sort_sort_in_descending_order(self, driver):
        main = MainPage(driver)
        main.open(self.locators.page_url[1])
        list_p = ListProductsPage(driver)
        test_price = random.randint(100, 1000)
        list_p.set_price_item(test_price)
        list_p.set_sort_price(1)  # Подешевле
        ac_price = get_num_in_str(list_p.get_item_card_price(0))
        assert ac_price >= test_price, f"Цена товара долна быть равной или меньшей {test_price}," \
                                       f" фактическая цена{ac_price}"
