import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


chromeoptions = Options()
chromeoptions.add_argument('--headless')
driver = webdriver.Chrome(options=chromeoptions)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.LINK_TEXT, "Shop").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.url_matches, "https://rahulshettyacademy.com/angularpractice/shop"
           )
mobiles = []
phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#driver.execute_script("window.scrollBy(0,500);")
number_of_phones = len(phones)
for phone in phones:
    phonename = phone.find_element(By.XPATH, "div/h4/a").text
    mobiles.append(phonename)
    if phonename == 'Blackberry':
        phone.find_element(By.XPATH, "div/button").click()


for items in mobiles:
    print(items)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.get_screenshot_as_file("screen.png")
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
#driver.find_element(By.CLASS_NAME,"checkbox checkbox-primary").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successtext = driver.find_element(By.CLASS_NAME, "alert-success").text

#assert "Success! Thank you!" == successtext

assert "Success! Thank you!" in successtext
