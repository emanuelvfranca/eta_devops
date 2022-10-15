from Pages.UserPage import UserPage


class Test3:

    def test_user_pages_without_user(self, open_browser):
        self.home_page = open_browser
        assert not self.home_page.is_user_logged(), "There is a user logged in"
        self.home_page.scroll_to_bottom()

        my_account_pages = self.home_page.get_my_account_pages()
        assert ["My orders", "My credit slips", "My addresses", "My personal info"] == \
               [link.text for link in my_account_pages], "User pages are not correct displayed"
        for page in my_account_pages:
            page.find_element_by_link_text(page.text).click()
            self.login_page = UserPage(self.home_page.driver)
            assert self.login_page.is_user_page(), "Login page was not opened"
            self.login_page.back()
