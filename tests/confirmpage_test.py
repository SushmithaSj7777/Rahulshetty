from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from tests.checkoutpage_Test import TestCheckoutPage
from utilities.BaseClass import BaseClass


class Testconfirmpage(TestCheckoutPage):

    def test_confirmpage(self):
        #homepageobj = HomePage(self.driver)
        #homepageobj.click_on_shop_link()
        #self.confirmpageobj = ConfirmPage(self.driver)

        # driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        # driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")

        checkout = self.checkoutpageobj.checkout()
        checkout.click()
        self.checkoutpageobj.delivery_country().send_keys("Ind")
        # wait = WebDriverWait(self.driver, 7)
        # wait.until(expected_conditions.visibility_of_element_located(confirmpage.india))
        self.explicit_wait("India")
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        self.confirmpageobj.india_function().click()
        # self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.confirmpageobj.checkbox_tick().click()

        # driver.find_element(By.CLASS_NAME,"checkbox checkbox-primary").click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.confirmpageobj.submit_btn().click()
        # successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        successtext = self.confirmpageobj.alert_success_func().text
        assert "Success! Thank you!" in successtext

