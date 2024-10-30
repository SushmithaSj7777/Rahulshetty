import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="type1"
    )


@pytest.fixture(scope="class")
def setup(request):

   # browsername = request.config.getoption("--browsername")
   # if browsername == "chrome":
    driver = webdriver.Chrome()
   # elif browsername == "firefox":
        #driver = webdriver.Firefox()

    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
