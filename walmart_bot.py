from bot import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
import constants

constants.walmart_credentials()

class WalmartBot(Bot):
    def __init__(self, driver):
        Bot.__init__(self, driver)
        self.driver = driver
        self.in_stock_element = (By.XPATH,
                                 '//span[text()="Add to cart"]')

    def is_signed_in(self):
        pass

    def sign_in(self):
        self.driver.find_element_by_xpath("//*[text()='Account']").click()
        self.driver.find_element_by_xpath("//*[text()='Sign In']").click()
        email_field = self.driver.find_element_by_id("email")
        email_field.click()
        email_field.clear()
        email_field.send_keys(WALMART_USERNAME)
        pass_field = self.driver.find_element_by_id("password")
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(WALMART_PASSWORD)

