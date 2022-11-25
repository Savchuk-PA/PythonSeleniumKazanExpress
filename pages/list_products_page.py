from locators.list_products import ListProductsLocators
from pages.base_page import BasePage


class ListProducts(BasePage):
    locators = ListProductsLocators()

    def item_card_click(self):
        self.elements_are_visible(self.locators.ITEM_CARD).click()
