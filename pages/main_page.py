from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_login_btn(self):
        """click_login_btn() Клик на кнопку авторизации"""
        self.element_is_visible(self.locators.LOGIN_BTN).click()

    def get_form_auth(self):
        """get_form_auth() Вызывает форму авторизавции пользователя"""
        self.open(MainPageLocators.URL)
        self.element_is_clickable(self.locators.LOGIN_BTN).click()

    def get_user_name(self):
        """get_user_name() Возвращает имя авторизованного пользователя"""
        return self.element_is_visible(self.locators.USER_NAME).text

    def show_catalog(self):
        self.element_is_clickable(self.locators.CATALOG_BTN).click()

    def get_elements_list(self):
        return self.elements_are_visible(self.locators.CATALOG_LIST)

    def input_search(self, text):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(text)
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(Keys.ENTER)

    def get_title_page(self):
        return self.element_is_visible(self.locators.TITLE_PAGE).text
