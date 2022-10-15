from Pages.UserPage import UserPage


class Test1:

    def test_user_validation(self, open_browser):
        self.home_page = open_browser
        assert self.home_page.has_sign_in_btn(), 'Botão de Sign In indisponível'
        self.home_page.sign_in_btn()
        import time
        time.sleep(3)
        self.user_page = UserPage(self.home_page.driver)
        assert self.user_page.has_sign_in_info(), 'Opção de login indisponível'
        time.sleep(3)
        self.user_page.user_sign_in()
        assert self.user_page.has_user_signed_in(), 'Usuário não conseguiu efetuar login'
        time.sleep(3)
        self.user_page.user_info_btn()
        time.sleep(3)
        assert self.user_page.has_user_information(), 'Informações do usuário indisponíveis'
        time.sleep(3)
        assert self.user_page.user_sign_out(), 'Usuário não conseguiu efetuar logout'
