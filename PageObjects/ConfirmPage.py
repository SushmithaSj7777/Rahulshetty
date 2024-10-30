from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutbtn = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    country = (By.CSS_SELECTOR, "#country")
    india = (By.LINK_TEXT, "India")
    checkbox2 = (By.XPATH, "//label[@for='checkbox2']")
    submit = (By.XPATH, "//input[@type='submit']")
    alert_success = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.checkoutbtn)

    def delivery_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def india_function(self):
        return self.driver.find_element(*ConfirmPage.india)

    def checkbox_tick(self):
        return self.driver.find_element(*ConfirmPage.checkbox2)

    def submit_btn(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def alert_success_func(self):
        return self.driver.find_element(*ConfirmPage.alert_success)


