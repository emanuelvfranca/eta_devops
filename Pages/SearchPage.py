from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.PageObject import PageObject
from selenium.common.exceptions import NoSuchElementException

from random import randint


class SearchPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=search'
    id_sort_selector = "selectProductSort"
    css_products_container = ".product_list .product-container .right-block"
    class_name_product_price = "price"
    class_name_old_product_price = "old-price"
    css_sort_selector_value = ".select .selector"

    xpath_products_list = "//*[@id=\"center_column\"]/ul"
    id_quantity_wanted = "quantity_wanted"
    id_group_size = "group_1"
    xpath_add_to_cart_item = "//*[@id=\"add_to_cart\"]/button"
    xpath_proceed_to_checkout = "//*[@id=\"layer_cart\"]/div[1]/div[2]/div[4]/a"

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver=driver)

    def is_search_page(self):
        return self.is_page(self.url)

    def sort_products(self, sort):
        select_element = self.driver.find_element(By.ID, self.id_sort_selector)
        select_object = Select(select_element)
        select_object.select_by_visible_text(sort)

    def get_current_sort(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_sort_selector_value).text.splitlines()[0]

    def get_products(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.css_products_container)

    def get_prices(self, discounted=True):
        """

        :param discounted: whether to count discounted prices or not in the list
        :return: list of all product prices in current search screen
        """
        prices = []
        products = self.get_products()
        for product in products:
            if discounted:
                prices.append(float(product.find_element(By.CLASS_NAME,
                                                         self.class_name_product_price).text.replace('$', '')))
            else:
                try:
                    prices.append(float(
                        product.find_element(By.CLASS_NAME, self.class_name_old_product_price).text.replace('$', '')))
                except NoSuchElementException:
                    prices.append(
                        float(product.find_element(By.CLASS_NAME, self.class_name_product_price).text.replace('$', '')))
        return prices

    #####

    def add_item_to_cart(self):
        self.choose_item_in_product_list()
        self.choose_item_quantity()
        self.choose_item_size()

    def choose_item_in_product_list(self):
        products_list = self.driver.find_elements(By.XPATH, self.xpath_products_list)
        random_item_index = randint(0, len(products_list) - 1)
        products_list[random_item_index].click()

    def choose_item_quantity(self):
        random_quantity = randint(2, 100)
        self.driver.find_element(By.ID, self.id_quantity_wanted).send_keys(random_quantity)

    def choose_item_size(self):
        self.scroll_to_half()
        self.driver.find_element(By.ID, self.id_group_size).click()
        sizes_list = self.driver.find_elements(By.ID, self.id_group_size)
        random_size = str(randint(1, len(sizes_list)))
        xpath_size = "//*[@id=\"group_1\"]/option[" + random_size + "]"
        self.driver.find_element(By.XPATH, xpath_size).click()

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.xpath_add_to_cart_item).click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, self.xpath_proceed_to_checkout).click()
