from locators import Common, Main, Product, Cart, User


def test_add_to_wish_list(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
    product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
    feature_product.click()
    # Клик по кнопке на странице Product
    browser.find_element_by_css_selector(Product.add_to_wishlist['css']).click()
    # Клик по ссылке в блоке alert-success
    browser.find_element_by_css_selector(Common.alert.success.login['css']).click()
    # Логин с формы авторизации пользователя
    browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test2@mail.ru")
    browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test")
    browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
    # Перейти в раздел избранного
    browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)


def test_add_to_cart(browser):
    browser.open()
    # Клик по первому элементу в блоке featured
    feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
    product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
    feature_product.click()
    # Клик по кнопке на странице Product
    browser.find_element_by_css_selector(Product.add_to_cart['css']).click()
    # Клик по ссылке в блоке alert-success
    browser.find_element_by_css_selector(Common.alert.success.to_cart['css']).click()
    # Проверка ссылки с текстом выбранного продукта
    browser.find_element_by_link_text(product_name)
    # Клик по кнопке Checkout на странице корзины
    browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
    # Логин с формы авторизации пользователя
    browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test2@mail.ru")
    browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test")
    browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
    # Ожидание отображения формы регистрации платежа
    browser.find_elements_by_css_selector(User.paymnet_form.it['css'])
