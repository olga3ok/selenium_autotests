from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET), ""

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
