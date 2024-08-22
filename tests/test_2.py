""" TASK
Generalize InputDataAndLogin.py
Use DataLoad in text fixture
"""

import pytest

from pythonProject.utilities.BaseClass import BaseClass
from pythonProject.PageObjects.HomePage import HomePage
from pythonProject.TestData.HomePageData import HomePageData


class TestLogin(BaseClass):

    def test_submission(self, get_login_data):
        # ASSIGN
        log = self.get_logger()
        expected_msg = "Success! The Form has been submitted successfully!."
        home_page = HomePage(self.driver)
        self.driver.refresh()  #refreshes browser

        # ACTION
        home_page.get_email_input().send_keys(get_login_data["email"])
        home_page.get_password_input().send_keys(get_login_data["password"])
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), get_login_data["gender"])
        home_page.get_double_check_text_box().send_keys("aloha")
        home_page.get_student_radio_btn().click()
        home_page.get_submit_btn().click()
        log.info("email:" + get_login_data["email"])

        observed_msg = home_page.get_alert().text
        log.info("Alert text:" + observed_msg)

        # ASSERT
        assert expected_msg in observed_msg


"""
    # @pytest.fixture(params=[("fake@gmail.com", "aloha123!", "Female"), ("4fake1@gmail.com", "aloha123!", "Male")])
    # Let's use Dictionary
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    # {"email":"4fake4@gmail.com", "password":"aloha123!", "gender":"Male"}
    def get_login_data(self, request):
        return request.param
"""


@pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
# {"email":"4fake4@gmail.com", "password":"aloha123!", "gender":"Male"}
def get_login_data(request):
    return request.param
