#import webdriver module from selenium package
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximize browser window
driver.maximize_window()

# Navigate to  saucedemo website - open url
driver.get("https://www.saucedemo.com")
time.sleep(2) #wait for 2 second to let the page load

#locate username web element
username = driver.find_element(By.ID, "user-name")

#enter username
username.send_keys("standard_user")

#locate password web element
password = driver.find_element(By.ID, "password")

#enter password
password.send_keys("secret_sauce")
time.sleep(5)


#close browser
driver.quit()
