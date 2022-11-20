from selenium.webdriver.common.by import By


class MainPageLocators:
    url = 'https://kazanexpress.ru/'
    LOGIN_BTN = (By.CSS_SELECTOR, "a[data-test-id = 'button__auth']")
    USER_NAME = (By.CSS_SELECTOR, "a[data-test-id = 'button__user']")