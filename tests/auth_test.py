import time

import pytest

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

        actual_user_name = main.get_user_name()
        expected_user_name = Auth.user_name
        assert expected_user_name == actual_user_name

    @pytest.mark.parametrize('login, password, get_err_phone_or_password, actual_err_mess', [
        (Auth.valid_phone, Auth.short_pass, 'password', Auth.error_message_short_pass)
    ])
    def test_display_err_login(self, driver, login, password, get_err_phone_or_password, actual_err_mess):
        main = MainPage(driver)
        main.get_form_auth()

        auth = AuthPage(driver)
        auth.fill_form(login, password)
        ac_error = auth.get_error_login(get_err_phone_or_password)
        ex_error = actual_err_mess
        assert ex_error == ac_error
        print(ac_error)