from selenium.webdriver.common.by import By
from pythonProject.PageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    double_check_text_box = (By.CSS_SELECTOR, "input[name='name']")
    student_radiobtn = (By.CSS_SELECTOR, "#inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    gender = (By.ID, "exampleFormControlSelect1")


    def __init__(self, driver):
        self.driver = driver

    def get_shop_page(self):
        self.driver.find_element(*HomePage.shop).click()  # it's the same as driver.find_element(By.LINK_TEXT, "Shop")
        # HomePage.shop because it's a class variable, not instance
        # *HomePage.shop - would be read this variable as tuple and deserialize it!
        checkout_page = CheckoutPage(
            self.driver)  # we've already clicked Shop page, so we can create instance of the class CheckoutPage here
        return checkout_page

    def get_email_input(self):
        return self.driver.find_element(*HomePage.email)

    def get_password_input(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_double_check_text_box(self):
        return self.driver.find_element(*HomePage.double_check_text_box)

    def get_student_radio_btn(self):
        return self.driver.find_element(*HomePage.student_radiobtn)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)

