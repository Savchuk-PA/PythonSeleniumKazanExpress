from locators.list_products import ListProductsLocators
from pages.base_page import BasePage


class ListProductsPage(BasePage):
    locators = ListProductsLocators()

    def item_card_click(self, num_item):
        self.elements_are_visible(self.locators.ITEM_CARD)[num_item].click()

    def get_title_product(self):
        return self.element_is_visible(self.locators.TITLE_PRODUCT).text
