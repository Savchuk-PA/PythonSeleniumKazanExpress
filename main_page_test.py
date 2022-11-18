from pages.main_page import MainPage

link = 'https://kazanexpress.ru/'


# class TestMainPage():
def test1(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.click_logo()


def test2(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.click_catalog()


def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_catalog_products()
