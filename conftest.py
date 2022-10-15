import pytest

from Pages.HomePage import HomePage
from Pages.ContactUsPage import ContactUsPage
from Pages.SearchPage import SearchPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help='Browser to run the tests')


@pytest.fixture
def browser(request):
    select_browser = request.config.getoption('--browser').lower()
    yield select_browser


@pytest.fixture()
def open_browser(browser):
    home_page = HomePage(browser=browser)
    yield home_page
    home_page.close()


@pytest.fixture()
def open_contact_us(open_browser):
    home_page = open_browser
    home_page.launch_contact_us()
    contact_us_page = ContactUsPage(home_page.driver)
    yield contact_us_page


@pytest.fixture()
def search_product(open_browser):
    home_page = open_browser
    home_page.search_item()
    search_page = SearchPage(home_page.driver)
    yield search_page




