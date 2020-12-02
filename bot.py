from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import partial
import time
#from constants import email_notification
import smtplib
from email.message import EmailMessage
import random

class Bot():
    def __init__(self, driver, url=""):
        self.driver = driver
        self.url = url
        self.out_of_stock_element = (By.ID, "")
        self.in_stock_element = (By.ID, "")

        # Prevents actual purchases while testing the bot
        self.purchase_failsafe = True

    def __goto_page(self, url):
        try:
            self.driver.get(url)
            print("URL successfully opened.")
        except Exception as exception_message:
            print("URL could not be opened. Exception: %s" % exception_message)

    # Checks if an item is in stock, returns True if so
    def check_in_stock(self, url):
        if not url == self.driver.current_url:
            self.__goto_page(url)

        try:
            self.driver.find_element(*self.in_stock_element)
            print("Item is available for purchase.")
            return True
        except Exception as exception_message:
            print("Could . Exception: %s" % exception_message)
            return False

    # Continuously refreshes page until an item is available
    def wait_availability(self):
        while not self.check_in_stock(self.url):
            refresh_time = self.random_refresh_sleep()
            print("Item isn't available. Refreshing in %s..." % refresh_time)
            time.sleep(refresh_time)
            self.driver.navigate().refresh()

    def do_checkout(self):
        # Check for purchase failsafe, skips purchase button @ end
        pass


    def is_signed_in(self):
        return False

    def sign_in(self):
        if self.is_signed_in == False:
            # do sign in
            pass
        pass

    def get_price(self):
        price_element = self.driver.find_element(By.CLASS_NAME,
                                                 "price-characteristic")
        price = price_element.get_attribute("content")
        print("Product price: %s" % price)
        return price

    def enter_data(self):
        pass

    def is_404(self):
        pass


    #def send_email_notification(self, message):
    #    server = smtplib.SMTP_SSL(*EMAIL_SERVER)
    #    server.login(*EMAIL_LOGIN)
    #    server.sendmail(
    #          EMAIL_LOGIN[0],
    #          DESTINATION_EMAIL,
    #          message)
    #    server.quit()"""

    ## "Turing test" functions--to prevent websites from detecting the bot 

    # I'm randomizing the time before refreshes just in case the servers
    #  can predict a bot based on consistent timing between refreshes
    def random_refresh_sleep(self, seconds_range=[1*60,3*60]):
        return random.randint(*seconds_range)

    # I don't actually know if we'll need this:
    def random_click_sleep(self, seconds_range=[1,4]):
        # TODO: make this return a decimal value instead of an int.
        return random.randint(*seconds_range)

    # Check if google's recaptcha popped up.
    def recaptcha_check(self):
        # Page recaptcha:
        if "www.walmart.com/blocked" in self.driver.current_url:
            return True
        # Embedded recaptcha
        else:
            # iframe src="https://www.google.com/recaptcha
            try:
                self.driver.find_element_by_xpath(
                    "//*[contains(@class, 're-captcha')]")
                return True
            except:
                return False
        return False

    # Wait for human to process recaptcha:
    def recaptcha_wait(self):
        while self.recaptcha_check() == True:
            time.sleep(10)
            print("Stuck in reCaptcha.")


    # Yeah, this one will be a freaking mess:
    def do_recaptcha(self):
        pass

    # Keeps attempting a funtion a predefined number of times until success
    def log_and_retry(self, func, attempts=10):
        def func_wrapper(*args, **kwargs):
            for attempt in range(attempts):
                time.sleep(self.random_click_sleep())
                try:
                    self.recaptcha_wait()
                    return func(*args, **kwargs)
                except Exception as exception_message:
                    print("Function %s failed! Attempt #%s. Exception: %s" %
                          (func.__name__, exception_message))
        return func_wrapper

    def run(self, url):
        # Add log and retry function wrapper to selenium functions
        self.driver.find_element = self.log_and_retry(self.driver.find_element)
        self.driver.find_element_by_id = self.log_and_retry(
            self.driver.find_element_by_id)
        self.driver.find_element_by_xpath = self.log_and_retry(
            self.driver.find_element_by_xpath)

        # Set url
        self.url = url
        self.__goto_page(self.url)

        # How to pass arguments with do_step:
        # self.do_step(partial(function, param1, param2)

        # Wait for product to become available
        self.wait_availability()

        # Check price
        self.get_price()

        # Ensure we're signed in so we can go through checkout!
        self.sign_in()

        # Run through checkout for product
        self.do_checkout()

