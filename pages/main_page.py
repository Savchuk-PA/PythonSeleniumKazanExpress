import time

from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()
    locatorsAuth = AuthPageLocators()

    def click_login_btn(self):
        """click_login_btn() Клик на кнопку авторизации"""
        self.element_is_visible(self.locators.LOGIN_BTN).click()

    def get_form_auth(self):
        """get_form_auth() Вызывает форму авторизавции пользователя"""
        self.open(MainPageLocators.url)
        self.element_is_clickable(self.locators.LOGIN_BTN).click()

    def get_user_name(self):
        """get_user_name() Возвращает имя авторизованного пользователя"""
        return self.element_is_visible(self.locators.USER_NAME).text
