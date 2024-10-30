from selenium.webdriver.common.by import By
from PageObjects.CheckOutPage import checkoutPage
from PageObjects.HomePage import HomePage
from tests.homepage_Test import Testhomepage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestCheckoutPage(Testhomepage):

    def test_e2e(self):
        homepageobj = HomePage(self.driver)
        checkoutpageobj = homepageobj.click_on_shop_link()
        checkoutpageobj.click()
        #dropdown = Select(homepage.form_filling())
        #dropdown.select_by_visible_text("Female")

        # homepage.click_on_shop_link().click()
        #checkoutpageobj = homepage.click_on_shop_link()
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Shop")))
        self.explicit_wait("Shop")
        #checkoutpageobj = checkoutPage(self.driver)

        mobiles = []
        #phones = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        #checkoutpageobj = checkoutPage(self.driver)
        phones = checkoutpageobj.phones_func()
        # driver.execute_script("window.scrollBy(0,500);")
        number_of_phones = len(phones)
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
        confirmpageobj = checkoutpageobj.checkout_btn_func()
        self.driver.get_screenshot_as_file("screen.png")
