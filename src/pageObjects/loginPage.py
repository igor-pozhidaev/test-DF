from selenium.webdriver.common.by import By
from src.pageObjects import basePage


class LoginPage(basePage.BasePage):

    def open_login_page(self):
        self.driver.get('https://digifabster.com/4taps/login/')

    def set_email(self, email):
        emailField = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        emailField.send_keys(email)

    def set_password(self, pwd):
        emailField = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        emailField.send_keys(pwd)

    def click_log_in(self):
        logInBttn = self.driver.find_element(By.XPATH, '//button[.="Log in"]')
        logInBttn.click()

    def login(self, email, pwd):
        self.set_email(email)
        self.set_password(pwd)
        self.click_log_in()