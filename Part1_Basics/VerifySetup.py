#import webdriver module from selenium package
from selenium import webdriver

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#open google.com webpage
driver.get("https://www.google.com")

#close the driver window
driver.quit()