import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_view_catalog_products(self):
        assert self.element_is_present(*MainPageLocators.CATALOG)

    def click_logo(self):
        time.sleep(5)
        self.browser.find_element(By.CSS_SELECTOR, "a[data-test-id='link__logo']").click()
        time.sleep(2)

    def click_catalog(self):
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.CATALOG).click()
        time.sleep(2)
