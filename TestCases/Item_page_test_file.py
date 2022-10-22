import time
import unittest

from selenium import webdriver
from Common.Variables.Variables_file import VariablesClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Src.Pages.Item_page_file import ItemPageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from webdrivermanager.chrome import ChromeDriverManager
from TestCases.Base_test_file import BaseTestClass


class AddItems(BaseTestClass):
    def setUp(self):
        self.addItemsPageObj = ItemPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_add_items(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        # Password Part
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        time.sleep(2)  # added to not get robot check
        self.signInPageObj.click_into_sign_in_button()

        # select & add first item
        self.addItemsPageObj.select_item()
        self.addItemsPageObj.click_on_add_to_cart_button()

        # back to previous page with back()
        self.driver.back()
        self.driver.back()

        # select & add second item
        self.addItemsPageObj.second_item_select()
        self.addItemsPageObj.click_on_add_to_cart_button()

        time.sleep(2)

    def tearDown(self):
        self.driver.close()
