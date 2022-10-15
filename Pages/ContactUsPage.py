from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.PageObject import PageObject


class ContactUsPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=contact'
    class_name_alert = 'alert'
    id_message_btn = 'submitMessage'
    id_email = 'email'
    id_message = 'message'
    id_subject_selector = 'id_contact'

    def __init__(self, driver):
        super(ContactUsPage, self).__init__(driver=driver)

    def is_contact_us_page(self):
        return self.is_page(self.url)

    def send_message(self):
        self.driver.find_element(By.ID, self.id_message_btn).click()

    def get_alert_message(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_name_alert).text.splitlines()[-1]

    def fill_email(self, email):
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def fill_message(self, message):
        self.driver.find_element(By.ID, self.id_message).send_keys(message)

    def select_heading(self, heading):
        select_element = self.driver.find_element(By.ID, self.id_subject_selector)
        select_object = Select(select_element)
        select_object.select_by_visible_text(heading)
