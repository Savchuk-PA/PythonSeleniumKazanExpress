from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = 'https://kazanexpress.ru/'
    LOGIN_BTN = (By.CSS_SELECTOR, "a[data-test-id = 'button__auth']")
    USER_NAME = (By.CSS_SELECTOR, "a[data-test-id = 'button__user']")
    CATALOG_BTN = (By.CSS_SELECTOR, "button[data-test-id='button__catalog']")
    CATALOG_LIST = (By.CSS_SELECTOR, "li[class='parent-category-item']")
    CATALOG_LIST_PRODUCT_NAME = ['Электроника', 'Бытовая техника', 'Одежда', 'Обувь', 'Аксессуары', 'Красота', 'Здоровье', 'Товары для дома', 'Строительство и ремонт', 'Автотовары', 'Детские товары', 'Хобби и творчество', 'Товары для взрослых', 'Спорт и отдых', 'Продукты питания', 'Бытовая химия и личная гигиена', 'Канцтовары', 'Зоотовары', 'Книги', 'Дача, сад и огород']
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test-id = 'input__search']")
