from locators import Product, Common


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_wishlist(self):
        self.driver.find_element_by_css_selector(Product.add_to_wishlist['css']).click()

    def add_to_cart(self):
        self.driver.find_element_by_css_selector(Product.add_to_cart['css']).click()
