from selenium.webdriver.common.by import By


class ConfirmPage:
    text_box = (By.ID, "country")
    country = (By.LINK_TEXT, "Poland")
    terms_checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase_btn = (By.CSS_SELECTOR, "input[class*='btn-success']")
    purchase_status = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def input(self):
        return self.driver.find_element(*ConfirmPage.text_box)

    def select_poland(self):
        return self.driver.find_element(*ConfirmPage.country)

    def apply_terms_and_conditions(self):
        return self.driver.find_element(*ConfirmPage.terms_checkbox)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def get_purchase_status(self):
        return self.driver.find_element(*ConfirmPage.purchase_status)