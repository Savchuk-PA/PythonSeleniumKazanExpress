from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = 'https://kazanexpress.ru/'
    LOGIN_BTN = (By.CSS_SELECTOR, "a[data-test-id = 'button__auth']")
    USER_NAME = (By.CSS_SELECTOR, "a[data-test-id = 'button__user']")
    CATALOG_BTN = (By.CSS_SELECTOR, "button[data-test-id='button__catalog']")
    CATALOG_LIST = (By.CSS_SELECTOR, "li[class='parent-category-item']")
    CATALOG_LIST_PRODUCT_NAME = ('Электроника', 'Бытовая техника', 'Одежда', 'Обувь', 'Аксессуары', 'Красота',
                                 'Здоровье', 'Товары для дома', 'Строительство и ремонт', 'Автотовары',
                                 'Детские товары', 'Хобби и творчество', 'Товары для взрослых', 'Спорт и отдых',
                                 'Продукты питания', 'Бытовая химия и личная гигиена', 'Канцтовары',
                                 'Зоотовары', 'Книги', 'Дача, сад и огород')
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test-id = 'input__search']")

    TITLE_PAGE = (By.CSS_SELECTOR, "h1[data-test-id = 'text__title']")

    # Links page site
    ELECTRONICS_URL = 'https://kazanexpress.ru/category/Elektronika-10020'
    APPLIANCES_URL = 'https://kazanexpress.ru/category/Bytovaya-tekhnika-10004'
    CLOTHES_URL = 'https://kazanexpress.ru/category/Odezhda-10014'
    SHOES_URL = 'https://kazanexpress.ru/category/Obuv-10013'
    ACCESSORIES_URL = 'https://kazanexpress.ru/category/Aksessuary-10003'
    BEAUTY_URL = 'https://kazanexpress.ru/category/Krasota-10012'
    HEALTH_URL = 'https://kazanexpress.ru/category/Zdorove-10009'
    HOUSEHOLD_GOODS_URL = 'https://kazanexpress.ru/category/Tovary-dlya-doma-10018'
    CONSTRUCTION_AND_REPAIR_URL = 'https://kazanexpress.ru/category/Stroitelstvo-i-remont-10016'
    AUTO_PRODUCTS_URL = 'https://kazanexpress.ru/category/Avtotovary-10002'
    CHILDRENS_PRODUCTS_URL = 'https://kazanexpress.ru/category/Detskie-tovary-10007'
    HOBBIES_AND_CREATIVITY_URL = 'https://kazanexpress.ru/category/Khobbi-i-tvorchestvo-10008'
    ADULT_PRODUCTS_URL = 'https://kazanexpress.ru/category/Tovary-dlya-vzroslykh-10017'
    SPORTS_URL = 'https://kazanexpress.ru/category/Sport-i-otdykh-10015'
    FOOD_PRODUCTS_URL = 'https://kazanexpress.ru/category/Produkty-pitaniya-1821'
    HOUSEHOLD_CHEMICALS_URL = 'https://kazanexpress.ru/category/Bytovaya-khimiya-i-lichnaya-10005'
    STATIONERY_URL = 'https://kazanexpress.ru/category/Kanctovary-10010'
    PET_SUPPLIES_URL = 'https://kazanexpress.ru/category/Zootovary-10019'
    BOOKS_URL = 'https://kazanexpress.ru/category/Knigi-10011'
    GARDEN_PRODUCTS_URL = 'https://kazanexpress.ru/category/Dacha-sad-i-ogorod-10006'

    page_url = (ELECTRONICS_URL, APPLIANCES_URL, CLOTHES_URL, SHOES_URL, ACCESSORIES_URL, BEAUTY_URL, HEALTH_URL,
                HOUSEHOLD_GOODS_URL, CONSTRUCTION_AND_REPAIR_URL, AUTO_PRODUCTS_URL, CHILDRENS_PRODUCTS_URL,
                HOBBIES_AND_CREATIVITY_URL, ADULT_PRODUCTS_URL, SPORTS_URL, FOOD_PRODUCTS_URL, HOUSEHOLD_CHEMICALS_URL,
                STATIONERY_URL, PET_SUPPLIES_URL, BOOKS_URL, GARDEN_PRODUCTS_URL)
