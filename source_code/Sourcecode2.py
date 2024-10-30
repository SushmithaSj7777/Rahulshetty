import time

import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
title = driver.title
assert title == "ProtoCommerce"
driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Sushmitha Sj")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("sushmithasj777@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("1234567")
checkbox = driver.find_element(By.CSS_SELECTOR, ".form-check-input:nth-child(1)")
checkbox.click()
assert checkbox.is_selected()
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
radiobtn = driver.find_element(By.XPATH, "//div/input[@value='option2']")
radiobtn.click()
assert radiobtn.is_selected()
driver.find_element(By.XPATH, '//input[@name="bday"]').send_keys("09/09/1996")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)
allure.attach(driver.get_screenshot_as_png(), name="test login screen",
              attachment_type=AttachmentType.PNG)
