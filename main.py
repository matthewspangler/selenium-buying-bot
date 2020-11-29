from walmart_bot import WalmartBot
# chromedriver that avoids triggering bot detection:
import undetected_chromedriver as uc
# Since undetected_chromedriver requires Chromium 87:
from selenium.webdriver.chrome.options import Options
# Contains login credentials, credit card info, and such:
import personal_info

options = Options()
# I have the latest build of Chromium in my selenium bot's directory:
options.binary_location = "./chrome-linux/chrome"

# Get the latest chromium build for Linux here: 
# https://chromium.woolyss.com/#linux

if __name__ == "__main__":
    # Change the following variable to your version of Chromium:
    uc.TARGET_VERSION = 87
    # Create instance of webdriver
    bot_driver = uc.Chrome(chrome_options=options)
    # Create instance of bot
    bot = WalmartBot(bot_driver, personal_info.walmart_profile)
    # Run bot on product page:
    bot.run("https://www.walmart.com/ip/For-Raspberry-Pi-4-B-Touch-Screen-with-Case-EEEkit-3-5-inch-Touchscreen-Support-320x480-Monitor-TFT-LCD-Game-Display-for-Raspberry-Pi-4-B/430357329")
