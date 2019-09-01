from locators import Main
from .BasePage import BasePage


class MainPage(BasePage):

    def click_featured_product(self, number):
        index = number - 1
        self._click(Main.featured.products, index=index)

    def get_featured_product_name(self, number):
        index = number - 1
        return self._get_element_text(Main.featured.names, index=index)
