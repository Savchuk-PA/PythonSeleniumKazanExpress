import pytest
from data.data import Auth
from locators.main_page_locators import MainPageLocators
from pages.auth_page import AuthPage
from pages.main_page import MainPage


class TestAuth:
    locators = MainPageLocators

    def test_valid_login(self, driver):
        main = MainPage(driver)
        main.get_form_auth()

        auth = AuthPage(driver)
        auth.fill_form(Auth.valid_phone, Auth.valid_pass)
        auth.refresh()

        actual_user_name = main.get_user_name()
        expected_user_name = Auth.user_name
        assert expected_user_name == actual_user_name

    @pytest.mark.parametrize('login, password, get_err_login_or_password, ex_err_message', [
        (Auth.valid_phone, Auth.short_pass, 'password', Auth.error_message_short_pass),
        (Auth.short_phone, Auth.valid_pass, 'login', Auth.error_message_short_login),
        (Auth.no_valid_login, Auth.no_valid_random_password_len_8, 'login', Auth.error_message_no_valid_log_and_pas)
    ])
    def test_display_text_err_auth(self, driver, login, password, get_err_login_or_password, ex_err_message):
        main = MainPage(driver)
        main.get_form_auth()

        auth = AuthPage(driver)
        auth.fill_form(login, password)
        ac_error = auth.get_error_login(get_err_login_or_password)
        ex_error = ex_err_message
        assert ac_error == ex_error
