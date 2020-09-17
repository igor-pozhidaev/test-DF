import unittest
import sys, os
from selenium import webdriver
from src.pageObjects import loginPage
from src.pageObjects import cartPage
from src.pageObjects import deliveryPage
from src.pageObjects import pricePage
from src.pageObjects import summaryPage
from src.pageObjects import uploadPage
from src.data import userData

class TestDF(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        login_page = loginPage.LoginPage(self.driver)
        login_page.open_login_page()
        login_page.login(userData.EMAIL, userData.PASSWORD)

    def test_make_an_order(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.join(os.path.sep, ROOT_DIR, 'src/stl-models/example.stl')

        upload_page = uploadPage.UploadPage(self.driver)
        price_page = pricePage.PricePage(self.driver)
        cart_page = cartPage.CartPage(self.driver)
        delivery_page = deliveryPage.DeliveryPage(self.driver)
        summary_page = summaryPage.SummaryPage(self.driver)

        upload_page.upload_file(filePath)
        upload_page.click_next_step()

        price_page.add_to_cart()
        price_page.proceed_to_cart()

        cart_page.increase_in_startup_cost()
        cart_page.click_next_step()

        delivery_page.fill_delivery_form(userData)
        delivery_page.get_shipping_rates()
        delivery_page.click_next_step()

        summary_page.confirm_order_button_is_clickable()



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
   unittest.main()