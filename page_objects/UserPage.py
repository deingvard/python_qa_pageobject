from locators import Common, User


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, email, password):
        browser = self.driver
        browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys(email)
        browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys(password)
        browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()

    def open_wishlist(self):
        self.driver.find_element_by_css_selector(User.right_menu.wish_list['css']).click()

    def verify_payment_form(self):
        self.driver.find_elements_by_css_selector(User.paymnet_form.it['css'])

    def verify_product(self, name):
        self.driver.find_element_by_link_text(name)
