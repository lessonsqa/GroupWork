from Src.Pages.Navigation_bar_file import NavigationBarClass
from Src.Pages.Base_page_file import BasePageClass
<<<<<<< HEAD
from Common.Find.Custom_find_file import CustomFindClass
from selenium.webdriver.common.by import By


=======
from selenium.webdriver.common.by import By
>>>>>>> f928922049d1b17e75a7e19d454a96f43c098099


class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()
        self.navigationBarObj = NavigationBarClass(driver)  # added to use "get_cart_number" function in remove_all_elements :)

    def remove_first_element_from_cart(self):
<<<<<<< HEAD
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

=======
        """Removes first element from cart"""
        deleteButtonElement = self.find.custom_find_element(self.locators.firstProductDeleteButtonLocator)
        self.click_to_element(deleteButtonElement)

    def remove_all_elements_from_cart(self):
        """Removes all elements from cart"""
        while self.navigationBarObj.get_cart_products_quantity() > 0:
            self.remove_first_element_from_cart()


class CartPageLocatorsClass():
    firstProductDeleteButtonLocator = (By.XPATH, "//input[@value='Delete']")
>>>>>>> f928922049d1b17e75a7e19d454a96f43c098099
