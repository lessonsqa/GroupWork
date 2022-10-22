import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Src.Pages.Cart_page_file import CartPageClass
from webdrivermanager.chrome import ChromeDriverManager
from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Item_page_file import ItemPageClass
from Src.Pages.Navigation_bar_file import NavigationBarClass


class DeleteItems(BaseTestClass):
    def setUp(self):
        self.deleteItemsPageObj = CartPageClass(self.driver)
        self.addItemsPageObj = ItemPageClass(self.driver)
        self.mainPageObj = NavigationBarClass(self.driver)

    def test_amazon_remove_items(self):
        self.driver.get(
            "https://www.amazon.com/s?k=AGV+helmet&crid=3VQ7S3GV599YW&sprefix=agv+helmet%2Caps%2C264&ref=nb_sb_noss_1")

        time.sleep(2)

        # select & add first item
        self.addItemsPageObj.select_item()
        self.addItemsPageObj.click_on_add_to_cart_button()

        # back to previous page with back()
        self.driver.back()
        self.driver.back()

        # select & add second item
        self.addItemsPageObj.second_item_select()
        self.addItemsPageObj.click_on_add_to_cart_button()
        self.mainPageObj.get_cart_number()

        # delete first item
        self.deleteItemsPageObj.remove_first_element_from_cart()
        self.deleteItemsPageObj.remove_all_elements_from_cart()

    def tearDown(self):
        self.driver.close()
