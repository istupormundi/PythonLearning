from selenium.webdriver.common.by import By

from pythonProject.utilities.BaseClass import BaseClass
from pythonProject.PageObjects.HomePage import HomePage


class TestPurchase(BaseClass):
    # link = "https://rahulshettyacademy.com/angularpractice"

    def test_e2e(self):
        # ARRANGE
        expected_msg = "Success!"

        # ACTION
        log = self.get_logger()
        log.error("OHH NO")
        home_page = HomePage(self.driver)
        checkout_page = home_page.get_shop_page()
        phones = checkout_page.get_phones()
        text = "Poland"

        for phone in phones:
            phone_name = checkout_page.get_phone_name(phone)
            log.warning(phone_name)
            if phone_name == "Blackberry":
                checkout_page.add_phone_to_basket(phone).click()

        checkout_page.select_checkout_btn_on_top_bar().click()
        confirm_page = checkout_page.select_checkout_btn_to_proceed()
        log.info("Selecting a country..")

        confirm_page.input().send_keys("Po")
        self.wait_for_dropdown_data(text)
        confirm_page.select_poland().click()
        confirm_page.apply_terms_and_conditions().click()
        confirm_page.purchase().click()

        observed_msg = confirm_page.get_purchase_status().text
        log.info(observed_msg)

        # ASSERT
        assert observed_msg.__contains__(expected_msg)
        assert expected_msg in observed_msg
