from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productFooter = (By.XPATH, "div/button")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getproductFooter(self):
        return self.driver.find_element(*CheckOutPage.productFooter)

    def getcheckoutbutton(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)