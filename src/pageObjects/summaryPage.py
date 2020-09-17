from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.pageObjects import basePage

class SummaryPage(basePage.BasePage):
    def confirm_order_button_is_clickable(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, '//button//span[contains(text(),"Confirm order")]')))
