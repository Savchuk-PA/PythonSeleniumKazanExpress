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
