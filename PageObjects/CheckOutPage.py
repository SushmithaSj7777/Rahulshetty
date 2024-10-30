from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class checkoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.phones = (By.XPATH, "//div[@class='card h-100']")

    phones = (By.XPATH, "//div[@class='card h-100']")
    phone_name_is = (By.XPATH, "div/h4/a")
    choosenphone = (By.XPATH, "div/button")
    checkoutbtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def phones_func(self):
        phonesf = self.driver.find_elements(*checkoutPage.phones)
        return phonesf

    def phone_name_function_is(self):
        phones = self.driver.find_element
        return self.phones.find_element(*checkoutPage.phone_name_is)

    def choosen_phone_func(self):
        return self.phones.find_element(*checkoutPage.choosenphone)

    def checkout_btn_func(self):
        self.driver.find_element(*checkoutPage.checkoutbtn).click()
        confirmpageobj = ConfirmPage(self.driver)
        return confirmpageobj

