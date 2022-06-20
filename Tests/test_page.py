from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getnameelement().send_keys(getData["firstname"])
        log.info("last name is " + getData["secondname"])
        homepage.getemailelement().send_keys(getData["secondname"])
        homepage.getcheckbuttonelement().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getsubmitelement().click()
        log.info("Clicked on submit button")
        message = homepage.getmessageelement().text
        log.info("Message is %s" %message)
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.home_page_test_data)
    def getData(self,request):
        return request.param
