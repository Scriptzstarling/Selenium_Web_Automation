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
# username = driver.find_element(By.NAME, "user-name")

#relative xpath to locate username
username = driver.find_element(By.XPATH, "//input[@id='user-name']")

#enter username
username.send_keys("standard_user")

#locate password web element
# password = driver.find_element(By.ID, "password")
password = driver.find_element(By.XPATH, "//input[@id='password']")

#enter password
password.send_keys("secret_sauce")
time.sleep(5)

#locate login button
loginBtn = driver.find_element(By.XPATH, "//input[@id='login-button']")

#click on login button
loginBtn.click()
time.sleep(5)


#close browser
driver.quit()
