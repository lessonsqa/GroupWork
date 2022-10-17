from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from Common.Variables.Variables_file import VariablesClass


class NavigationBarClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavigationBarLocatorsClass()

    def fill_in_search_field(self, text=VariablesClass.searchText):
        searchField = self.find.custom_find_element(self.locators.searchFieldLocator)
        searchField.clear()
        searchField.send_keys(text)

    def click_into_submit_button(self):
        submitButton = self.find.custom_find_element(self.locators.submitButton)
        submitButton.click()

    def click_on_cart_button(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        cartButtonElement.click()

    def get_cart_products_quantity(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        return int(cartButtonElement.text)


class NavigationBarLocatorsClass:
    searchFieldLocator = (By.ID, "twotabsearchtextbox")
    submitButton = (By.ID, "nav-search-submit-button")
    cartButtonLocator = (By.ID, "nav-cart-count")
