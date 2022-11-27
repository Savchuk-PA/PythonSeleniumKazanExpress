import time

from selenium.webdriver import Keys

from locators.list_products import ListProductsLocators
from pages.base_page import BasePage


class ListProductsPage(BasePage):
    locators = ListProductsLocators()

    def item_card_click(self, num_item):
        self.elements_are_visible(self.locators.ITEM_CARD)[num_item].click()

    def get_item_card_price(self, num_item):
        return self.elements_are_visible(self.locators.ITEM_CARD_PRODUCT_PRICE)[num_item].text

    def get_title_product(self):
        return self.element_is_visible(self.locators.TITLE_PRODUCT).text

    def set_price_item(self, price):
        self.element_is_visible(self.locators.INPUT_MIN_PRICE).send_keys(price)
        self.element_is_visible(self.locators.INPUT_MIN_PRICE).send_keys(Keys.ENTER)
        time.sleep(0.5)


    def set_sort_price(self, category):
        """В качестве аргумента педать число от 0 до 5.
        0 - Популярные, 1 - Подешевле, 2 - Подоороже,
        3 - Высокий рейтинг, 4 - много заказов, 5 - Добавлены недавно"""
        self.element_is_visible(self.locators.SELECT_SORT_BTN).click()
        self.elements_are_present(self.locators.SELECT_SORT_LIST)[category].click()
