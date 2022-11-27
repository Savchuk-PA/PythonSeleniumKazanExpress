from selenium.webdriver.common.by import By


class ListProductsLocators:
    ITEM_CARD = (By.XPATH, "//div[@data-test-id = 'list__products']//div[@data-test-id = 'item__product-card']")
    TITLE_PRODUCT = (By.CSS_SELECTOR, "h1[data-test-id = 'text__product-name']")
    INPUT_MIN_PRICE = (By.CSS_SELECTOR, "input[data-test-id = 'input__min-price']")
    SELECT_SORT_BTN = (By.CSS_SELECTOR, "div[data-test-id ='button__dropdown']")
    SELECT_SORT_LIST = (By.CSS_SELECTOR, "li[data-test-id = 'list__item']")
    ITEM_CARD_PRODUCT_PRICE = (By.CSS_SELECTOR, ".products-list .product-card-price")
