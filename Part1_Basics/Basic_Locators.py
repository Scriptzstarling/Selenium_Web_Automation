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
# username = driver.find_element(By.XPATH, "//input[@id='user-name']")

#locate username using AND method
# username = driver.find_element(By.XPATH, "//input[@type='text' and @id='user-name']")

#locate username using Index
username = driver.find_element(By.XPATH, "(//input)[1]")
#enter username
username.send_keys("standard_user")

#locate password web element
# password = driver.find_element(By.ID, "password")
password = driver.find_element(By.XPATH, "//input[@id='password']")

#enter password
password.send_keys("secret_sauce")
time.sleep(5)

#locate login button
# loginBtn = driver.find_element(By.XPATH, "//input[@id='login-button']")

#locate login button using OR method
loginBtn = driver.find_element(By.XPATH, "//input[@id='login-button' or @id='wrong-id']")

#click on login button
loginBtn.click()
time.sleep(2)

#contains() - locate add to cart button
# addToCart = driver.find_element(By.XPATH, "//button[contains(@id,'sauce-labs-bolt-t-shirt')]")
# addToCart.click()

#text() - locate web element sauce lab fleece jacket and perform click action
product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
product.click()
time.sleep(5)

#close browser
driver.quit()
