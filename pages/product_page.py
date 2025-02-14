from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_to_basket_btn()
        product_title = self.get_product_title()
        product_price = self.get_product_price()
        self.add_product_to_button()
        self.solve_quiz_and_get_code()
        self.should_be_message()
        self.should_be_correct_product_title(product_title)
        self.should_be_correct_product_price(product_price)

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket btn is not presented"

    def get_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split()[0]
        return product_price

    def add_product_to_button(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_message(self):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be "

    def should_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissapeared, but should be"

    def should_be_correct_product_title(self, product_title):
        title_in_cart = self.browser.find_element(*ProductPageLocators.TITLE_IN_CART).text
        assert title_in_cart == product_title, "Title in cart is incorrect"

    def should_be_correct_product_price(self, product_price):
        price_in_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text.split()[0]
        assert price_in_cart == product_price, "Price in cart is incorrect"
