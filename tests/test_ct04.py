class Test1:

    def test_newsletter(self, open_browser):
        self.home_page = open_browser
        assert self.home_page.has_newsletter(), 'Campo Newsletter indisponível'
        assert self.home_page.empty_newsletter_warn(), 'Alerta de campo Newsletter vazio indisponível'
        import time
        time.sleep(4)
        assert self.home_page.registered_email_warn(), 'Alerta de email já cadastrado indisponível'
        import time
        time.sleep(4)
        assert self.home_page.successfull_newsletter_warn(), 'Alerta de email cadastrado com sucesso indisponível'
        import time
        time.sleep(4)
