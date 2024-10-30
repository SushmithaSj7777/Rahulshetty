from selenium.webdriver.common.by import By
from PageObjects.CheckOutPage import checkoutPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        logging = self.test_logging()
        homepageobj = HomePage(self.driver)
        logging.info("Click on shop")
        homepageobj.click_on_shop_link().click()
        self.explicit_wait("Shop")
        #dropdown = Select(homepage.form_filling())
        #dropdown.select_by_visible_text("Female")

        # homepage.click_on_shop_link().click()
        #checkoutpageobj = homepage.click_on_shop_link()
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Shop")))
        self.explicit_wait("Shop")
        checkoutpageobj = checkoutPage(self.driver)

        mobiles = []
        #phones = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        #checkoutpageobj = checkoutPage(self.driver)

        phones = checkoutpageobj.phones_func()
        # driver.execute_script("window.scrollBy(0,500);")
        number_of_phones = len(phones)
        logging.info("number_of_phones"+str(number_of_phones))
        print("number_of_phones ", number_of_phones)
        for phone in phones:
            # phonename = checkoutpageobj.phone_name_function_is().text
            phonename = phone.find_element(By.XPATH, "div/h4/a").text
            mobiles.append(phonename)
            if phonename == 'Blackberry':
                # checkoutpageobj.choosen_phone_func().click()
                phone.find_element(By.XPATH, "div/button").click()

        for items in mobiles:
            print(items)
        #elf.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpageobj.checkout_btn_func()
        self.driver.get_screenshot_as_file("screen.png")

        #confirmpage = ConfirmPage(self.driver)

        #driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        #driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")

        confirmpage.checkout().click()
        confirmpage.delivery_country().send_keys("Ind")
        #wait = WebDriverWait(self.driver, 7)
        #wait.until(expected_conditions.visibility_of_element_located(confirmpage.india))
        self.explicit_wait("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpage.india_function().click()
        #self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        confirmpage.checkbox_tick().click()

        # driver.find_element(By.CLASS_NAME,"checkbox checkbox-primary").click()
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmpage.submit_btn().click()
        #successtext = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        successtext = confirmpage.alert_success_func().text
        assert "Success! Thank you!" in successtext
