from selenium.webdriver.common.by import By
from pythonProject.PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    """phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for phone in phones:
        phoneName = phone.find_element(By.XPATH, "div/h4/a").text
        if phoneName == "Blackberry":
            phone.find_element(By.XPATH, "div/button").click()"""

    phones = (By.XPATH, "//div[@class='card h-100']")
    phone_names = (By.XPATH, "div/h4/a")
    phone_to_basket = (By.XPATH, "div/button")

    def __init__(self, driver):
        self.driver = driver

    def get_phones(self):
        return self.driver.find_elements(*CheckoutPage.phones)

    def get_phone_name(self, phone):
        return phone.find_element(*CheckoutPage.phone_names).text

    def add_phone_to_basket(self, phone):
        return phone.find_element(*CheckoutPage.phone_to_basket)

    def select_checkout_btn_on_top_bar(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")

    def select_checkout_btn_to_proceed(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page


"""
self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
"""
