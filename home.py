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
driver.execute_script("window.scrollBy(0, 800);")
click_seleniumImg = driver.find_element_by_css_selector("img[alt='Selenium Ruby']")
click_seleniumImg.click()
driver.execute_script("window.scrollBy(0, 600);")
click_reviewButton = driver.find_element_by_css_selector("[href='#tab-reviews']")
click_reviewButton.click()
click_star = driver.find_element_by_css_selector(".star-5")
click_star.click()
commentArea = driver.find_element_by_id("comment")
commentArea.send_keys("Nice book!")
nameArea = driver.find_element_by_id("author")
nameArea.send_keys("Roman")
nameArea = driver.find_element_by_id("email")
nameArea.send_keys("testtt11@gmail.com")
submit = driver.find_element_by_id("submit")
submit.click()
time.sleep(2)
driver.quit()