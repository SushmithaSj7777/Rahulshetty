import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def explicit_wait(self, text):
        wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.url_matches, "https://rahulshettyacademy.com/angularpractice/shop")                   )
        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, text)))

    def test_logging(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel("DEBUG")
        logger.debug("DEBUG messange")
        logger.info("INFO message")
        logger.warning("WARNING message")
        logger.error("ERROR messgae")
        logger.critical("CRITICAL message")
        return logger
