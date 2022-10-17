from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass


class ItemPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageLocatorsClass()

    def select_item(self):
        itemSelectElement = self.find.custom_find_element(self.locators.itemSelectLocator)
        itemSelectElement.click()

    def click_on_add_to_cart_button(self):
        addToCartButtonElement = self.find.custom_find_element(self.locators.addToCartButtonLocator)
        addToCartButtonElement.click()

    def second_item_select(self):
        secondItemElement = self.find.custom_find_element(self.locators.secondItemSelectLocator)
        secondItemElement.click()


class ItemPageLocatorsClass:
    addToCartButtonLocator = (By.ID, "add-to-cart-button")
    itemSelectLocator = (By.XPATH, '(//div[@class="a-section a-spacing-base"])[1]')
    secondItemSelectLocator = (By.XPATH, '(//div[@class="a-section a-spacing-base"])[3]')
