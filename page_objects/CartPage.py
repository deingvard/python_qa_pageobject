from locators import Cart


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()

    def verify_product(self, name):
        self.driver.find_element_by_link_text(name)
