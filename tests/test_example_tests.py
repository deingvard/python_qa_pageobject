from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(browser):
    browser.open()
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    browser.find_element_by_css_selector("[data-original-title='Add to Wish List']").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text('login').click()
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("input[value=Login]").click()
    browser.find_element_by_link_text('Wish List').click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))


def test_add_to_cart(browser):
    browser.open()
    feature_product = browser.find_elements_by_css_selector("#content > div.row .product-layout")[0]
    product_name = feature_product.find_element_by_css_selector(".caption h4 a").text
    feature_product.click()
    browser.find_element_by_css_selector("#button-cart").click()
    browser.find_element_by_css_selector(".alert-success").find_element_by_link_text("shopping cart").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
    browser.find_element_by_css_selector(".buttons").find_element_by_link_text("Checkout").click()
    browser.find_element_by_css_selector("#input-password").send_keys("test")
    browser.find_element_by_css_selector("#input-email").send_keys("test2@mail.ru")
    browser.find_element_by_css_selector("input[value=Login]").click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "payment-new")))
