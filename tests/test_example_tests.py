from page_objects import MainPage, UserPage, ProductPage, CartPage
from page_objects.common import Alert


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wishlist()
    Alert(browser).click_login()
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    UserPage(browser).open_wishlist()
    UserPage(browser).verify_product(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    Alert(browser).click_to_cart()
    CartPage(browser).verify_product(product_name)
    CartPage(browser).checkout()
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    UserPage(browser).verify_payment_form()
