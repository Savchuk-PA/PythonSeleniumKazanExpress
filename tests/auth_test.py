import time

from data.data import Auth
from locators.main_page_locators import MainPageLocators
from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestAuth:
    locators = MainPageLocators

    def test_valid_login(self, driver):
        main = MainPage(driver)
        main.get_form_auth()

        auth = AuthPage(driver)
        auth.fill_form(Auth.valid_phone, Auth.valid_pass)
        time.sleep(2)
        auth.refresh()

        actual_user_name = main.element_is_visible(self.locators.USER_NAME).text
        expected_user_name = Auth.user_name
        assert expected_user_name == actual_user_name
