import time

from data.data import Auth
from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage
import selenium


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def fill_form(self, login: str, password: str):
        """Используется для заполнения формы авторизации пользователя"""
        self.element_is_visible(self.locators.INPUT_PHONE_OR_EMAIL_BTN).send_keys(login)
        self.element_is_visible(self.locators.INPUT_PASSWORD_BTN).send_keys(password)
        self.element_is_clickable(self.locators.SIGN_IN_BTN).click()
        time.sleep(1)

    def get_error_login(self, log_or_phone: str):
        """Возвращает текст ошибки. В качестве параметра нужно перадать login,
        вернет ошибку логина, елси передать password, вернет ошибку пароля"""
        if log_or_phone == 'login':
            return self.elements_are_visible(self.locators.AUTH_ERROR_MESSAGE_LOGIN)[0].get_attribute("data-error")
        if log_or_phone == 'password':
            return self.elements_are_visible(self.locators.AUTH_ERROR_MESSAGE_LOGIN)[1].get_attribute("data-error")