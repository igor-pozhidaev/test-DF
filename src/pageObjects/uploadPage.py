from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.pageObjects import basePage


class UploadPage(basePage.BasePage):

    def upload_file(self, file):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="qqfile"]').send_keys(file)
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[class="status_label _ready"]')))

    def click_next_step(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, '//a[@id="next_step_btn" and contains(@class,"btn-success")]')))
        nextStepBttn = self.driver.find_element(By.XPATH, '//a[contains(text(),"Next step")]')
        nextStepBttn.click()
