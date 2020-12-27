from bot import Bot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WalmartBot(Bot):
    def __init__(self, driver, walmart_profile):
        Bot.__init__(self, driver)
        self.profile = walmart_profile
        self.driver = driver
        self.in_stock_element = (By.XPATH,
                                 '//span[text()="Add to cart"]')

    # Check if signed into walmart account:
    def is_signed_in(self):
        pass

    # Sign into walmart account:
    def sign_in(self):
        profile = self.profile
        self.driver.find_element_by_xpath(
            "//button[@id='hf-account-flyout']/span/span/span[2]").click()
        self.driver.find_element_by_xpath(
            "//div[@id='vh-account-menu-root']/div[2]/div/a/div/span/div"
        ).click()
        self.driver.find_element_by_id("email").click()
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id(
            "email").send_keys(profile["email"])
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id(
            "password").send_keys(profile["password"])
        self.driver.find_element_by_id("sign-in-widget").click()
        #self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def do_checkout(self):
        profile = self.profile
        # Add to cart button
        self.driver.find_element_by_xpath(
            "//div[@id='add-on-atc-container']" \
            "/div/section/div/div[3]/button/span/span").click()
        # Check out button
        self.driver.find_element_by_xpath(
            "//button[@data-tl-id='IPPacCheckOutBtnBottom']").click()
        # data-tl-id="IPPacCheckOutBtnBottom"
        self.driver.find_element_by_xpath("//div[3]/button/span").click()

        self.driver.find_element_by_xpath(
            "//div[3]/div/div/div[2]/button/span").click()
        self.enter_shipping_info()

    def enter_shipping_info(self):
        # Shipping address section
        self.driver.find_element_by_id("firstName").click()
        self.driver.find_element_by_id("firstName").clear()
        self.driver.find_element_by_id(
            "firstName").send_keys(profile["firstname"])
        self.driver.find_element_by_id("addressLineOne").click()
        self.driver.find_element_by_id("addressLineOne").clear()
        self.driver.find_element_by_id(
            "addressLineOne").send_keys(profile["street"])
        self.driver.find_element_by_id("lastName").click()
        self.driver.find_element_by_id("lastName").clear()
        self.driver.find_element_by_id(
            "lastName").send_keys(profile["lastname"])
        self.driver.find_element_by_id("phone").click()
        self.driver.find_element_by_id("phone").clear()
        self.driver.find_element_by_id("phone").send_keys(profile["phone"])
        self.driver.find_element_by_id("city").click()
        self.driver.find_element_by_id("city").clear()
        self.driver.find_element_by_id("city").send_keys(profile["city"])
        self.driver.find_element_by_id("postalCode").click()
        self.driver.find_element_by_id("postalCode").clear()
        self.driver.find_element_by_id("postalCode").send_keys(profile["zip"])
        self.driver.find_element_by_id("state").click()
        self.driver.find_element_by_xpath(
            "//option[@value='%s']" % profile["state"]).click()

        # Continue button
        self.driver.find_element_by_xpath("//div[2]/div[2]/button/span").click()

