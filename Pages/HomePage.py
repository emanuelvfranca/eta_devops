from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Pages.PageObject import PageObject

import random
import string


class HomePage(PageObject):
    url = "http://automationpractice.com/index.php"
    id_contact_link = 'contact-link'
    class_name_sign_in = 'login'
    id_search_bar = "search_query_top"
    obj_search_item = "Dress"
    name_search_btn = "submit_search"
    css_account_pages = "ul.bullet li"

    id_newsletter_input = "newsletter-input"
    name_submit_newsletter = "submitNewsletter"
    class_alert_danger = "alert-danger"
    txt_invalid_email_alert = "Newsletter : Invalid email address."
    already_registerd_email = "a@a.com"
    class_alert_success = "alert-success"
    class_login = "login"
    txt_already_registered_alert = "Newsletter : This email address is already registered."
    txt_successfull_email_alert = "Newsletter : You have successfully subscribed to this newsletter."

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.open_page()

    def open_page(self):
        self.driver.get(self.url)

    def launch_contact_us(self):
        self.driver.find_element(By.ID, self.id_contact_link).click()

    def is_user_logged(self):
        return not self.driver.find_element(By.CLASS_NAME, self.class_name_sign_in).text == 'Sign in'

    def get_my_account_pages(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.css_account_pages)

    def search_item(self):
        self.driver.find_element(By.ID, self.id_search_bar).send_keys(self.obj_search_item)
        self.driver.find_element(By.NAME, self.name_search_btn).click()


    #######

    def has_search_bar(self):
        try:
            self.driver.find_element(By.ID, self.id_search_bar)
            return True
        except NoSuchElementException:
            return False

    def click_search_btn(self):
        self.driver.find_element(By.NAME, self.name_search_btn).click()

    def has_newsletter(self):
        self.scroll_to_bottom()
        return self.driver.find_element(By.ID, self.id_newsletter_input).is_displayed()

    def submit_newsletter_btn(self):
        self.driver.find_element_by_name(self.name_submit_newsletter).click()

    def empty_newsletter_warn(self):
        self.scroll_to_bottom()
        self.fill_newsletter("")
        return self.has_invalid_email_address_alert()

    def has_invalid_email_address_alert(self):
        return self.driver.find_element_by_class_name(self.class_alert_danger).text.lower() == self.txt_invalid_email_alert.lower()

    def registered_email_warn(self):
        self.scroll_to_bottom()
        self.fill_newsletter(self.already_registerd_email)
        return self.has_already_registered_email_alert()

    def has_already_registered_email_alert(self):
        return self.driver.find_element_by_class_name(self.class_alert_danger).text.lower() == self.txt_already_registered_alert.lower()

    def random_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def fill_newsletter(self, text):
        self.driver.find_element(By.ID, self.id_newsletter_input).send_keys(text)
        self.submit_newsletter_btn()

    def successfull_newsletter_warn(self):
        self.scroll_to_bottom()
        email = self.generate_email()
        self.fill_newsletter(email)
        return self.has_successfull_newsletter_alert()

    def has_successfull_newsletter_alert(self):
        return self.driver.find_element_by_class_name(self.class_alert_success).text.lower() == self.txt_successfull_email_alert.lower()

    def generate_email(self):
        user = self.random_generator()
        provider = self.random_generator()
        return user + "@" + provider + ".com"

    def has_sign_in_btn(self):
        return self.driver.find_element_by_class_name(self.class_login).is_displayed()

    def sign_in_btn(self):
        self.driver.find_element_by_class_name(self.class_login).click()
