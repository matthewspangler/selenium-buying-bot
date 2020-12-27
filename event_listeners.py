from selenium import webdriver as wb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.keys import Keys
import random
import time
import datimetime

class BotListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

    def before_find(self, by, value, driver):
        # Random sleep (float) to prevent bot detection!
        print("Sleeping to avoid bot detection...")
        time.sleep(random.uniform(1.0, 2.0))
        # Check for recaptcha
        recaptcha_tries = 10
        recaptcha_sleep = 10
        for attempt in range(recaptcha_tries):
            try:
                # recaptcha element
                driver.find_element_by_xpath(
                    "//*[contains(@class, 're-captcha')]")
                # Wait 10 seconds for user to process captcha
                print("Recaptcha found on attempt #%s" % attempt)
                print("Waiting 10 seconds for recaptcha")
                time.sleep(recaptcha_sleep)
            except:
                print("No recaptcha found!")
                # break from attempt loop
                break

    def before_click(self, element, driver):
        pass

    def after_click(self, element, driver):
        pass

    def after_navigate_forward(self, driver):
        print("after_navigate_forward")

    def before_navigate_forward(self, driver):
        print("before_navigate_forward")

    def after_navigate_back(self, driver):
        print("after_navigate_back")

    def before_navigate_back(self, driver):
        print("before_navigate_back")

    def before_change_value_of(self, element, driver):
        print("before_change_value_of")

    def on_exception(self, exception, driver):
        screenshot_name = "%s-exception.png" % datetime.now()
        driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot of exception captured: %s" % screenshot_name)
