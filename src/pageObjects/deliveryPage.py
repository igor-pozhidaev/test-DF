from selenium.webdriver.common.by import By
from src.pageObjects import basePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time

class DeliveryPage(basePage.BasePage):

    def set_first_name(self, firstName):
        firstNameField = self.driver.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
        firstNameField.send_keys(firstName)

    def set_last_name(self, lastName):
        lastNameField = self.driver.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
        lastNameField.send_keys(lastName)

    def set_phone_number(self, phoneNumber):
        phoneNumberField = self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
        phoneNumberField.send_keys(phoneNumber)

    def set_address_line(self, addressLine):
        addressLineField = self.driver.find_element(By.XPATH, '//input[@data-form-id="delivery_address" and @name="street_address"]')
        addressLineField.clear()
        addressLineField.send_keys(addressLine)

    def set_city(self, city):
        cityField = self.driver.find_element(By.XPATH, '//input[@data-form-id="delivery_address" and @name="city"]')
        cityField.clear()
        cityField.send_keys(city)

    def set_postal_code(self, postcode):
        postcodeField = self.driver.find_element(By.XPATH, '//input[@data-form-id="delivery_address" and @name="postcode"]')
        postcodeField.clear()
        postcodeField.send_keys(postcode)

    def select_country(self, country):
        self.driver.find_element(By.XPATH, "//div[select[@data-form-id='delivery_address' and @name='country']]").click()
        selectedCountry = self.driver.find_element(By.XPATH, "//div[select[@data-form-id='delivery_address' and @name='country']]//li[@data-value='{}']".format(country))
        selectedCountry.click()

    def fill_delivery_form(self, data):
        self.set_first_name(data.FIRST_NAME)
        self.set_last_name(data.LAST_NAME)
        self.set_phone_number(data.PHONE_NUMBER)
        self.set_address_line(data.ADDRESS_LINE)
        self.set_city(data.CITY)
        self.set_postal_code(data.POSTAL_CODE)
        self.select_country(data.COUNTRY)

    def get_shipping_rates(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[id="shipping_rates"]')))

    def click_next_step(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.invisibility_of_element_located((By.XPATH, '//div[.="Loading delivery price..."]')))
        wait.until(ec.element_to_be_clickable((By.XPATH, '//button[@id="s4_submit" and //img[@class="hidden"]]'))).click()
