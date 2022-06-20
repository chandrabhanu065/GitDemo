import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestComplete(BaseClass):

    def test_completion(self):
        #homepage = HomePage(self.driver)
        #checkoutpage = homepage.shopItem()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()
        homepage = HomePage(self.driver)
        #homepage.shopItem().click()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #checkoutpage = CheckOutPage(self.driver)
        checkoutpage = homepage.shopItem()
        products = checkoutpage.getcardTitles()
        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        for product in products:
            #productName = product.find_element_by_xpath("div/h4/a").text
            productName = product.text
            if productName == "Blackberry":
                # Add item into cart
                #product.find_element_by_xpath("div/button").click()
                checkoutpage.productFooter.click()

        #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutpage.getcheckoutbutton().click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")
