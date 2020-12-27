from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys
import random
import time
import datetime

class BotListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        # Random sleep to prevent bot detection!
        print("Sleeping to avoid bot detection...")
        #time.sleep(random.uniform(1.0, 2.0))
        time.sleep(random.randint(1, 3))
        recaptcha_sleep = 10
        find_tries = 10
        for find_try in range(find_tries):
            try:
                driver.find_element(by, value)
                break
            except:
                print("Couldn't find element, checking for recaptcha")
                while True:
                    try:
                        # recaptcha element
                        driver.find_element_by_xpath(
                            "//*[contains(@class, 're-captcha')]")
                        # Wait 10 seconds for user to process captcha
                        print("Recaptcha found!")
                        print("Waiting for human intervention!")
                        time.sleep(recaptcha_sleep)
                    except:
                        print("No recaptcha found!")
                        # break from attempt loop
                        break

    def on_exception(self, exception, driver):
        screenshot_name = "%s-exception.png" % datetime.now()
        driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot of exception captured: %s" % screenshot_name)
