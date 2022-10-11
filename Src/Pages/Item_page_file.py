from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass


class ItemPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageLocatorsClass()

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self.find.custom_find_element(self.locators.addToCartButtonLocator)
        addToCartButtonElement.click()


class ItemPageLocatorsClass:
    addToCartButtonLocator = (By.ID, "add-to-cart-button")
