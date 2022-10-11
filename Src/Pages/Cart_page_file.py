from Src.Pages.Main_page_file import MainPageClass
from Src.Pages.Base_page_file import BasePageClass


class CartPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocatorsClass()
        self.mainPageObj = MainPageClass(driver)  # added to use "get_cart_number" function in remove_all_elements :)

    def remove_first_element_from_cart(self):
        """Removes first element from cart"""
        # TODO "Elen"
        pass

    def remove_all_elements_from_cart(self):
        """Removes all elements from cart"""
        # TODO "Elen"
        pass


class CartPageLocatorsClass:
    # TODO add deleteElementsLocator "Elen"
    pass
