from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class PageObject:
    class_name_title = 'title'

    def __init__(self, browser=None, driver=None):
        if driver:
            # ProductsPage
            self.driver = driver
        else:
            if browser == 'chrome':
                chrome_driver = Service(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=chrome_driver)
            elif browser == 'firefox':
                firefox_driver = Service(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=firefox_driver)
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            else:
                raise Exception("Browser nao suportado")

            self.driver.implicitly_wait(2)

    def close(self):
        self.driver.quit()

    def is_page(self, url):
        return url in self.driver.current_url

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_half(self):
        self.driver.execute_script("window.scrollTo(0, 250);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def back(self):
        self.driver.back()
