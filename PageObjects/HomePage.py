from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import checkoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//div/input[@name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[placeholder='Password']")
    checkbox = (By.CSS_SELECTOR, ".form-check-input:nth-child(1)")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    radiobtn = (By.XPATH, "//div/input[@value='option2']")
    bday = (By.XPATH, '//input[@name="bday"]')
    submit = (By.XPATH, "//input[@type='submit']")
    alert_text = (By.CLASS_NAME, "alert-success")
    shop = (By.LINK_TEXT, "Shop")

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def tick_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def select_radiobtn(self):
        return self.driver.find_element(*HomePage.radiobtn)

    def select_dob(self):
        return self.driver.find_element(*HomePage.bday)

    def click_submit_btn(self):
        return self.driver.find_element(*HomePage.submit)

    def success_test_verify(self):
        return self.driver.find_element(*HomePage.alert_text)

    def click_on_shop_link(self):
        return self.driver.find_element(*HomePage.shop)
        #checkoutpageobj = checkoutPage(self.driver)
        #return checkoutpageobj
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Shop")))
        #return checkoutpageobj
        #self.explicit_wait("Shop")
        #checkoutpageobj = checkoutPage(self.driver)
       # return checkoutpageobj
