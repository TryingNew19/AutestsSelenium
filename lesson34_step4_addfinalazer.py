#этот тест не работает!
import pytest
import requests
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # этот код выполнится после завершения теста
    def quiting():
        print("\nquit browser..")
        browser.quit()
    request.addfinalizer(quiting)


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")