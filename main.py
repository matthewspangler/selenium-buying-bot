from walmart_bot import WalmartBot
from selenium import webdriver

if __name__ == "__main__":
    bot_driver = webdriver.Chrome("chromedriver")
    bot = WalmartBot(bot_driver)
    bot.run("https://www.walmart.com/ip/For-Raspberry-Pi-4-B-Touch-Screen-with-Case-EEEkit-3-5-inch-Touchscreen-Support-320x480-Monitor-TFT-LCD-Game-Display-for-Raspberry-Pi-4-B/430357329")
