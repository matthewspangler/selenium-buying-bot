from bot import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By


class WalmartBot(Bot):
    def __init__(self, driver):
        Bot.__init__(self, driver)
        self.driver = driver
        self.out_of_stock_element = (By.XPATH, "outOfStock")
        self.in_stock_element = (By.XPATH,
                                 '//span[text()="Add to cart"]')

