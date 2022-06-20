import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testpage(BaseClass):
    def test_form(self, getData):
        homepage = HomePage(self.driver)
        homepage.getnameelement().send_keys(getData[0])
        homepage.getemailelement().send_keys(getData[1])
        homepage.getcheckbuttonelement().click()
        dropdown = Select(homepage.getdropdownnelement())
        dropdown.select_by_visible_text(getData[2])
        #dropdown.select_by_index(0)
        homepage.getsubmitelement().click()
        message = homepage.getmessageelement().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=[("chandra","bhanu", "Male"),("Hema","durga","Female")])
    def getData(self, request):
        return request.param
