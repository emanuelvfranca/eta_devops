

class Test5:

    def test_sort_price(self, search_product):
        self.search_page = search_product
        assert self.search_page.is_search_page(), "Search page is not opened"
        self.search_page.sort_products("Price: Highest first")
        assert self.search_page.get_current_sort() == "Price: Highest first", "Highest first was not properly selected"

        prices = self.search_page.get_prices(discounted=False)
        print(prices)
        assert all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)), \
            "Product prices are not properly sorted from Highest to Lowest"

        self.search_page.sort_products("Price: Lowest first")
        assert self.search_page.get_current_sort() == "Price: Lowest first", "Lowest first was not properly selected"

        prices = self.search_page.get_prices(discounted=False)
        print(prices)
        assert all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1)), \
            "Product prices are not properly sorted from Lowest to Highest"
