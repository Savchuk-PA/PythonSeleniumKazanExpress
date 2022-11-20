import time

from data.data import Auth
from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def fill_form(self, login: str, password: str):
        """Используется для заполнения формы авторизации пользователя"""
        self.element_is_visible(self.locators.INPUT_PHONE_OR_EMAIL_BTN).send_keys(login)
        self.element_is_visible(self.locators.INPUT_PASSWORD_BTN).send_keys(password)
        self.element_is_clickable(self.locators.SIGN_IN_BTN).click()
