from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.pageObjects import basePage

class PricePage(basePage.BasePage):

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="product-preview"]//figure[@class="thumb_wrapper hidden"]')))
        addToCartBttn = self.driver.find_element(By.XPATH, '//div[.="Add to cart"]')
        addToCartBttn.click()

    def proceed_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//div[@class="add_btn_text_count"]//span[.="1"]')))
        proceedToCartBttn = wait.until(ec.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Proceed to Cart")]')))
        proceedToCartBttn.click()
