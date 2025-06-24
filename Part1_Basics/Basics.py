# 1. How to navigate Browser
#    a) Opening a browser
#    b) Navigating URLs

#import webdriver module from selenium package
from selenium import webdriver
import time



#instantiate webdriver and launch Chrome browser

driver = webdriver.Chrome()

# Navigate to google - open url
driver.get("https://www.google.com")
time.sleep(2) #wait for 2 second to let the page load

# Navigate to youtube - open url
driver.get("https://www.youtube.com/")
time.sleep(2) #wait for 2 second to let the page load

# go back to google
driver.back()

# go forward to youtube-
driver.forward()

# refresh the current page
driver.refresh()

#close the driver window
driver.quit()
