from locators import Cart
from .BasePage import BasePage

class CartPage(BasePage):

    def checkout(self):
        self._click(Cart.bottom_btn.checkout)

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
