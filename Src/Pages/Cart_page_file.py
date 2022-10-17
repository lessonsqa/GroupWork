from Src.Pages.Navigation_bar_file import NavigationBarClass
from Src.Pages.Base_page_file import BasePageClass
from Common.Find.Custom_find_file import CustomFindClass
from selenium.webdriver.common.by import By




class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()
        self.navigationBarObj = NavigationBarClass(driver)  # added to use "get_cart_number" function in remove_all_elements :)

    def remove_first_element_from_cart(self):
        itemDeleteElement = self.find.custom_find_element(self.locators.itemDeleteLocator)
        itemDeleteElement.click()

    def remove_all_elements_from_cart(self):
        while self.navigationBarObj.get_cart_number()>0:
            self.remove_all_elements_from_cart()
        # """Removes all elements from cart"""
        # deleteAllItems = self.find.custom_find_element(self.locators.itemDeleteLocator)
        # deleteAllItems.click()
        # deleteAllItems = 1
        # while deleteAllItems > 0:
        #     deleteAllItems +=1


class CartPageLocatorsClass:
    itemDeleteLocator = (By.NAME, "submit.delete.Cba47ad73-753b-4b67-ae96-394cda3793ab")

