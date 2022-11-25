from selenium.webdriver.common.by import By


class ListProductsLocators:
    ITEM_CARD = (By.XPATH, "//div[@data-test-id = 'list__products']//div[@data-test-id = 'item__product-card']")