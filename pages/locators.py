from typing import Tuple

from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOG = (By.CSS_SELECTOR, "[data-test-id='button__catalog']")
