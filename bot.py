from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from constants import email_notification
import smtplib
from email.message import EmailMessage
import random

class Bot():
    def __init__(self, driver):
        self.driver = driver
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

    # Checks if an item is out of stock, returns True if so
    def check_out_of_stock(self, url):
        if not url == self.driver.current_url:
            self.__goto_page(url)

        try:
            self.driver.find_element(*self.out_of_stock_element)
            print("Item is not available for purchase.")
            return True
        except Exception as exception_message:
            print("Could not find element. Exception: %s" % exception_message)
            return False

    # Checks if an item is in stock, returns True if so
    def check_in_stock(self, url):
        if not url == self.driver.current_url:
            self.__goto_page(url)

        try:
            self.driver.find_element(*self.in_stock_element)
            print("Item is available for purchase.")
            return True
        except Exception as exception_message:
            print("Could not find element. Exception: %s" % exception_message)
            return False

    # Continuously refreshes page until an item is available
    def wait_availability(self, url, refresh_time):
        while not self.check_in_stock(url):
            print("Item isn't available. Refreshing in %s..." % refresh_time)
            time.sleep(refresh_time)
            self.driver.navigate().refresh()

    def do_checkout(self):
        # Check for purchase failsafe, skips purchase button @ end
        try:
            pass
        except Exception as ex:
            pass

    def is_login(self):
        return False

    def do_login(self):
        pass

    def get_price(self):
        try:
            price_element = self.driver.find_element(By.CLASS_NAME,
                                                 "price-characteristic")
            price = price_element.get_attribute("content")
            print("Product price: %s" % price)
            return price
        except Exception as exception_message:
            print("Failed to get price. Exception: %s" % exception_message)


    def click_button(self, element):
        try:
            self.driver.find_element(element).click()
        except Exception as exception_message:
            print("Could not click button. Exception: %s" % exception_message)

    def enter_data(self):
        pass

    def is_404(self):
        pass

    def send_email_notification(self, message):
        server = smtplib.SMTP_SSL(*EMAIL_SERVER)
        server.login(*EMAIL_LOGIN)
        server.sendmail(
              EMAIL_LOGIN[0],
              DESTINATION_EMAIL,
              message)
        server.quit()

    # I'm randomizing the time before refreshes just in case the servers
    #  can predict a bot based on consistent timing between refreshes
    def random_refresh_sleep(self, seconds_range=[1*60,3*60]):
        return random.randint(*seconds_range)

    def run(self, url):
        self.wait_availability(url, self.random_refresh_sleep)
        #self.send_email_notification("Product available!")

        self.get_price()

        # Ensure we're signed in so we can go through checkout!
        if not self.is_login():
            self.do_login()

        self.do_checkout()
        #self.send_email_notification("Product purchased!")


