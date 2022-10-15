from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CartPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=order'
    class_cart_title = "navigation_page"
    txt_cart_summary = "Your shopping cart"
    class_cart_quantity_input = "cart_quantity_input"
    class_button_minus = "cart_quantity_down"

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_cart_page(self):
        return self.is_page(self.url)

    def has_cart_summary(self):
        print(self.driver.find_element(By.CLASS_NAME, self.class_cart_title).text.lower())
        print(self.txt_cart_summary.lower())
        return self.driver.find_element(By.CLASS_NAME, self.class_cart_title).text.lower() == \
               self.txt_cart_summary.lower()

    def subtract_item_quantity(self):
        self.scroll_to_half()
        self.driver.find_element(By.CLASS_NAME, self.class_button_minus).click()

    def get_item_quantity(self):
        self.scroll_to_half()
        return int(self.driver.find_element(By.CLASS_NAME, self.class_cart_quantity_input).get_attribute("value"))

