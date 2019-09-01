from locators import Common, Product, Cart, User
from page_objects import MainPage, UserPage


def test_add_to_wish_list(browser):
    # Клик по первому элементу в блоке featured
    product_name = MainPage(browser).click_featured_product(1)
    # Клик по кнопке на странице Product
    browser.find_element_by_css_selector(Product.add_to_wishlist['css']).click()
    # Клик по ссылке в блоке alert-success
    browser.find_element_by_css_selector(Common.alert.success.login['css']).click()
    # Логин с формы авторизации пользователя
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    # Перейти в раздел избранного
    browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)


def test_add_to_cart(browser):
    # Клик по первому элементу в блоке featured
    product_name = MainPage(browser).click_featured_product(1)
    # Клик по кнопке на странице Product
    browser.find_element_by_css_selector(Product.add_to_cart['css']).click()
    # Клик по ссылке в блоке alert-success
    browser.find_element_by_css_selector(Common.alert.success.to_cart['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)
    # Клик по кнопке Checkout на странице корзины
    browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
    # Логин с формы авторизации пользователя
    UserPage(browser).login_user(email="test2@mail.ru", password="test")
    # Ожидание отображения формы регистрации платежа
    browser.find_elements_by_css_selector(User.paymnet_form.it['css'])
