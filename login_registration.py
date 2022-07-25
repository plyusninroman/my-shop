###Задание 1
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# myAccount_button = driver.find_element_by_link_text("My Account")
# myAccount_button.click()
# regName = driver.find_element_by_id("reg_email")
# regName.send_keys("nitet33492@leupus.com")
# regPass = driver.find_element_by_id("reg_password")
# regPass.send_keys("Qwerfdsazxcv!@#$")
# regButton = driver.find_element_by_css_selector("input[name='register']")
# regButton.click()
# time.sleep(3)
# driver.quit()

### Задание 2

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
myAccount_button = driver.find_element_by_link_text("My Account")
myAccount_button.click()
userName = driver.find_element_by_id("username")
userName.send_keys("nitet33492@leupus.com")
userPass = driver.find_element_by_id("password")
userPass.send_keys("Qwerfdsazxcv!@#$")
loginButton = driver.find_element_by_css_selector("input[name='login']")
loginButton.click()
element = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation li:last-child a")
element_get_text = element.text
assert element_get_text == "Logout"
time.sleep(2)
driver.quit()