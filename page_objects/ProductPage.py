from locators import Product
from .BasePage import BasePage


class ProductPage(BasePage):

    def add_to_wishlist(self):
        self._click(Product.add_to_wishlist)
        return self

    def add_to_cart(self):
        self._click(Product.add_to_cart)
        return self
