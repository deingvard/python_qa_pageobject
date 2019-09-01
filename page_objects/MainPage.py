from locators import Main


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.driver.find_elements_by_css_selector(Main.featured.products['css'])[index]
        product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
        feature_product.click()
        return product_name
