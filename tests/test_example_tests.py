from locators import Cart, User
from page_objects import MainPage, UserPage, ProductPage
from page_objects.common import Alert


def test_add_to_wish_list(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wishlist()
    Alert(browser).click_login()
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    # Перейти в раздел избранного
    browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)


def test_add_to_cart(browser):
    product_name = MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    Alert(browser).click_to_cart()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)
    # Клик по кнопке Checkout на странице корзины
    browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
    # Логин с формы авторизации пользователя
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    # Ожидание отображения формы регистрации платежа
    browser.find_elements_by_css_selector(User.paymnet_form.it['css'])
