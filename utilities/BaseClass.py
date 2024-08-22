import pytest
import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("prepare_chrome_browser")
class BaseClass:
    driver = None

    def wait_for_dropdown_data(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]  # gets name from which this method will be called;
        # w\o it current file package always be in the log
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler = logging.FileHandler('pylog.txt')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # in which file I should print log, we should pass file location here
        logger.setLevel(logging.DEBUG)  # in this case we skip debug lvl
        return logger