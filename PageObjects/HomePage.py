from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check_button = (By.ID,"exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def getnameelement(self):
        return self.driver.find_element(*HomePage.name)

    def getemailelement(self):
        return self.driver.find_element(*HomePage.email)

    def getcheckbuttonelement(self):
        return self.driver.find_element(*HomePage.check_button)

    def getdropdownnelement(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getsubmitelement(self):
        return self.driver.find_element(*HomePage.submit)

    def getmessageelement(self):
        return self.driver.find_element(*HomePage.message)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)