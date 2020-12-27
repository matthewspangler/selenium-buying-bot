from walmart_bot import WalmartBot
# chromedriver that avoids triggering bot detection:
import undetected_chromedriver as uc
# Since undetected_chromedriver requires Chromium 87:
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver
# Contains login credentials, credit card info, and such:
import personal_info
# Listener class
from event_listeners import BotListener

options = Options()
# I have the latest build of Chromium in my selenium bot's directory:
options.binary_location = "./chrome-linux/chrome"

# Get the latest chromium build for Linux here: 
# https://chromium.woolyss.com/#linux

if __name__ == "__main__":
    # Create instance of webdriver
    bot_driver = uc.Chrome(chrome_options=options)
    bot_driver.implicitly_wait(10)
    event_driver = EventFiringWebDriver(bot_driver, BotListener())
    # Create instance of bot
    bot = WalmartBot(event_driver, personal_info.walmart_profile)
    # Run bot on product page:
    bot.run("https://www.walmart.com/ip/For-Raspberry-Pi-4-B-Touch-Screen-with-Case-EEEkit-3-5-inch-Touchscreen-Support-320x480-Monitor-TFT-LCD-Game-Display-for-Raspberry-Pi-4-B/430357329")
