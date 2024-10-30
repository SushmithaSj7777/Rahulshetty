import time

import pytest
from selenium.webdriver.support.select import Select
from PageObjects.HomePage import HomePage
from Test_Data.HomePageData import home_pageData
from utilities.BaseClass import BaseClass


class Testhomepage(BaseClass):

    def test_formSubmission(self, getdata):
        log = self.test_logging()
        #log.info("launching website")
        #self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        title = self.driver.title
        log.info("page title is"+title)
        assert title == "ProtoCommerce"
        homepageobj = HomePage(self.driver)
        log.info("Entering name email pwd")
        homepageobj.enter_name().send_keys(getdata[1]["Name"])
        homepageobj.enter_email().send_keys(getdata[1]["Email"])
        homepageobj.enter_password().send_keys(getdata[1]["Pwd"])
        checkbox = homepageobj.tick_checkbox()
        checkbox.click()
        assert checkbox.is_selected()

        dropdown = Select(homepageobj.select_gender())
        dropdown.select_by_visible_text("Female")
        radiobtn = homepageobj.select_radiobtn()
        radiobtn.click()
        assert radiobtn.is_selected()

        homepageobj.select_dob().send_keys("09/09/1996")
        homepageobj.click_submit_btn().click()
        successtext = homepageobj.success_test_verify().text
        # assert "Success! Thank you!" == successtext
        assert "Success! The Form" in successtext
        log.info("Page successfully submited")
        #checkoutpageobj = homepageobj.click_on_shop_link()

        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Shop")))
        #self.explicit_wait("Shop")

    #@pytest.fixture(params=[("Sushmitha Sj", "sushmithasj777@gmail.com", "1234567"),("SRI AKHIL Sj", "sriakhilsj@gmail.com", "1234567")])
    #@pytest.fixture(params=[{"Name": "Sushmitha", "Email": "sushmithasj777@gmail.com", "Pwd": "1234567"},
                         #   {"Name": "AKHIL", "Email": "akhil@gmail.com", "Pwd": "1234567"}])
    @pytest.fixture(params=[home_pageData.test_home_page_data])
    def getdata(self, request):
        return request.param
