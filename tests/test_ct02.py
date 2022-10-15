from Pages.CartPage import CartPage
from Pages.SearchPage import SearchPage

class Test1:

    def test_search_bar(self, open_browser):
        self.home_page = open_browser
        assert self.home_page.has_search_bar(), "Barra de pesquisa não disponível"
        self.home_page.search_item()
        self.search_page = SearchPage(self.home_page.driver)
        self.search_page.add_item_to_cart()
        self.search_page.add_to_cart()
        self.search_page.proceed_to_checkout()
        self.cart_page = CartPage(self.home_page.driver)
        assert self.cart_page.has_cart_summary(), "Título do carrinho de compras incorreto"
        old_item_quantity = self.cart_page.get_item_quantity()
        self.cart_page.subtract_item_quantity()
        import time
        time.sleep(3)
        new_item_quantity = self.cart_page.get_item_quantity()
        assert new_item_quantity == (old_item_quantity - 1), "A quantidade de itens não foi diminuída"
