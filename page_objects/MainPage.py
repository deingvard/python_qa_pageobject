from locators import Main
from .BasePage import BasePage
from .ProductPage import ProductPage

class MainPage(BasePage):

    def click_featured_product(self, number):
        index = number - 1
        self._click(Main.featured.products, index=index)
        return ProductPage(self.driver)

    def get_featured_product_name(self, number):
        index = number - 1
        return self._get_element_text(Main.featured.names, index=index)
