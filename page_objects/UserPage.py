from locators import Common, User
from .BasePage import BasePage


class UserPage(BasePage):

    def login_user(self, email, password):
        self._input(Common.user_login.email_input, email)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.login_button)
        return self

    def open_wishlist(self):
        self._click(User.right_menu.wish_list)
        return self

    def verify_payment_form(self):
        self._wait_for_visible(User.paymnet_form.it)
        return self

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
