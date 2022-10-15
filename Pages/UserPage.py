from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class UserPage(PageObject):
    url = 'http://automationpractice.com/index.php?controller=authentication'
    class_name_page_heading = 'page-heading'
    class_already_registered_question = "page-subheading"
    id_email = "email"
    id_password = "passwd"
    id_submit_login = "SubmitLogin"
    user_email = "a@a.com"
    user_password = "123456"
    user_full_name = "Fulano de Ciclano"
    user_first_name = "Fulano"
    user_last_name = "de Ciclano"
    user_birth_date = "24"
    user_birth_month = "January"
    user_birth_year = "1989"
    class_user_account = "account"
    txt_account_title_page = "My account - My Store"
    class_icon_user = "icon-user"
    id_firstname = "firstname"
    id_lastname = "lastname"
    id_days = "uniform-days"
    id_month = "uniform-months"
    id_years = "uniform-years"
    tag_selected = "selected"
    class_logout = "logout"
    txt_login_page = "Login - My Store"
    class_header_user_info = "header_user_info"

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def is_user_page(self):
        return self.is_page(self.url) and \
               self.driver.find_element(By.CLASS_NAME, self.class_name_page_heading).text.lower() == "authentication"

    def sign_in_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.class_header_user_info).click()

    def has_sign_in_info(self):
        self.scroll_to_half()
        self.scroll_to_half()
        is_already_registered_available = self.driver.find_element_by_class_name(
            self.class_already_registered_question).is_displayed()
        is_email_available = self.driver.find_element(By.ID, self.id_email).is_displayed()
        is_password_available = self.driver.find_element(By.ID, self.id_password).is_displayed()
        return is_already_registered_available and is_email_available and is_password_available

    def user_sign_in(self):
        self.driver.find_element(By.ID, self.id_email).click()
        self.driver.find_element(By.ID, self.id_email).send_keys(self.user_email)
        self.driver.find_element(By.ID, self.id_password).click()
        self.driver.find_element(By.ID, self.id_password).send_keys(self.user_password)
        self.driver.find_element(By.ID, self.id_submit_login).click()

    def has_user_signed_in(self):
        user_log = self.driver.find_element(By.CLASS_NAME,
                                            self.class_user_account).text.lower() == self.user_full_name.lower()
        account_page_title = self.driver.title.lower() == self.txt_account_title_page.lower()
        return user_log and account_page_title

    def user_info_btn(self):
        self.scroll_to_half()
        self.driver.find_element(By.CLASS_NAME, self.class_icon_user).click()

    def has_user_information(self):
        self.scroll_to_half()
        self.scroll_to_half()
        is_first_name_correct = self.driver.find_element(By.ID, self.id_firstname).get_attribute(
            "value").lower() == self.user_first_name.lower()
        is_last_name_correct = self.driver.find_element(By.ID, self.id_lastname).get_attribute(
            "value").lower() == self.user_last_name.lower()
        is_birth_date_correct = self.driver.find_element(By.ID, self.id_days).text.splitlines()[0].replace(" ",
                                                                                                           "") == self.user_birth_date
        is_birth_month_correct = self.driver.find_element(By.ID, self.id_month).text.splitlines()[0].replace(" ",
                                                                                                             "") == self.user_birth_month
        is_birth_year_correct = self.driver.find_element(By.ID, self.id_years).text.splitlines()[0].replace(" ",
                                                                                                            "") == self.user_birth_year
        return is_first_name_correct and is_last_name_correct and is_birth_date_correct and is_birth_month_correct and is_birth_year_correct

    def user_sign_out(self):
        self.scroll_to_top()
        self.driver.find_element(By.CLASS_NAME, self.class_logout).click()
        return self.has_user_signed_out()

    def has_user_signed_out(self):
        return self.driver.title.lower() == self.txt_login_page.lower()
