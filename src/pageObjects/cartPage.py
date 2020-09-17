from selenium.webdriver.common.by import By
from src.pageObjects import basePage

class CartPage(basePage.BasePage):

    def increase_in_startup_cost(self):
        increaseLink = self.driver.find_element(By.CSS_SELECTOR, 'span[class="increase-startup-price-link"]')
        increaseLink.click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[id="additional_cost_msg"]')

    def click_next_step(self):
        nextStepBttn = self.driver.find_element(By.XPATH, '//a[contains(text(),"Next step")]')
        nextStepBttn.click()