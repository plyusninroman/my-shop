### Задание 1

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
# userName = driver.find_element_by_id("username")
# userName.send_keys("nitet33492@leupus.com")
# userPass = driver.find_element_by_id("password")
# userPass.send_keys("Qwerfdsazxcv!@#$")
# loginButton = driver.find_element_by_css_selector("input[name='login']")
# loginButton.click()
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 500);")
# book = driver.find_element_by_css_selector(".post-181>a")
# book.click()
# textCheck = driver.find_element_by_css_selector(".entry-title")
# get_textCheck = textCheck.text
# assert get_textCheck == "HTML5 Forms"
# time.sleep(2)
# driver.quit()

### Задание 2

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
# userName = driver.find_element_by_id("username")
# userName.send_keys("nitet33492@leupus.com")
# userPass = driver.find_element_by_id("password")
# userPass.send_keys("Qwerfdsazxcv!@#$")
# loginButton = driver.find_element_by_css_selector("input[name='login']")
# loginButton.click()
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# htmlButton = driver.find_element_by_css_selector(".cat-item-19>a")
# htmlButton.click()
# items_count = driver.find_elements_by_css_selector(".masonry-done>li")
# if len(items_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
# driver.quit()

### Задание 3

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
# userName = driver.find_element_by_id("username")
# userName.send_keys("nitet33492@leupus.com")
# userPass = driver.find_element_by_id("password")
# userPass.send_keys("Qwerfdsazxcv!@#$")
# loginButton = driver.find_element_by_css_selector("input[name='login']")
# loginButton.click()
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# priceDefault = driver.find_element_by_css_selector("option[value='menu_order']")
# priceDefault_checked = priceDefault.get_attribute("selected")
# if priceDefault_checked is not None:
#     print("Стандартный фильтр установлен по умолчанию")
# else:
#     print("Ошибка: значение фильтра некорректно")
# price_highToLow = driver.find_element_by_css_selector("select>option:last-child")
# price_highToLow.click()
# time.sleep(2)
# price_highToLow = driver.find_element_by_css_selector("option[value='price-desc']")
# price_highToLow_checked = price_highToLow.get_attribute("selected")
# if price_highToLow_checked is not None:
#     print("Фильтр от большего к меньшему установлен по умолчанию")
# else:
#     print("Ошибка: значение фильтра некорректно")
# driver.quit()

### Задание 4

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
# userName = driver.find_element_by_id("username")
# userName.send_keys("nitet33492@leupus.com")
# userPass = driver.find_element_by_id("password")
# userPass.send_keys("Qwerfdsazxcv!@#$")
# loginButton = driver.find_element_by_css_selector("input[name='login']")
# loginButton.click()
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# androidBook = driver.find_element_by_css_selector(".post-169 a")
# androidBook.click()
# time.sleep(2)
# oldPrice = driver.find_element_by_css_selector("del>.woocommerce-Price-amount")
# oldPrice_text = oldPrice.text
# assert oldPrice_text == "₹600.00"
# newPrice = driver.find_element_by_css_selector("ins>.woocommerce-Price-amount")
# newPrice_text = newPrice.text
# assert newPrice_text == "₹450.00"
# check_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# check_img.click()
# check_X = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# check_X.click()
# driver.quit()

### Задание 5

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 600);")
# addBasket = driver.find_element_by_css_selector(".post-182>a[rel='nofollow']")
# addBasket.click()
# time.sleep(2)
# addItem = driver.find_element_by_css_selector("span[class='cartcontents']")
# addItem_text = addItem.text
# assert addItem_text == "1 Item"
# addCost = driver.find_element_by_css_selector("span[class='amount']")
# addCost_text = addCost.text
# assert addCost_text == "₹180.00"
# addItem.click()
# time.sleep(2)
# check_subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount "), "₹180.00"))
# check_total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount "), "₹183.60"))
# driver.quit()

### Задание 6

# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
# shopButton.click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 600);")
# addBasket = driver.find_element_by_css_selector(".post-182>a[rel='nofollow']")
# addBasket.click()
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 400);")
# addBasketToo = driver.find_element_by_css_selector(".post-180>a[rel='nofollow']")
# addBasketToo.click()
# basket = driver.find_element_by_css_selector("span[class='cartcontents']")
# basket.click()
# time.sleep(2)
# deleteStuff = driver.find_element_by_css_selector("tbody>tr:first-child .remove")
# deleteStuff.click()
# check_undo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-message>a")))
# undoButton = driver.find_element_by_css_selector(".woocommerce-message>a")
# undoButton.click()
# time.sleep(1)
# bookAmount = driver.find_element_by_css_selector("tbody>tr:first-child .quantity>input")
# bookAmount.clear()
# bookAmount.send_keys("3")
# updateBasket = driver.find_element_by_css_selector("input[name='update_cart']")
# updateBasket.click()
# time.sleep(2)
# bookAmount = driver.find_element_by_css_selector("tbody>tr:first-child .quantity>input")
# bookAmount_checked = bookAmount.get_attribute("value")
# assert bookAmount_checked == "3"
# time.sleep(1)
# couponButton = driver.find_element_by_css_selector(".coupon>.button")
# couponButton.click()
# time.sleep(1)
# couponCode_check = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
# driver.quit()

### Задание 7

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
shopButton = driver.find_element_by_css_selector("#menu-item-40 a")
shopButton.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
addBasket = driver.find_element_by_css_selector(".post-182>a[rel='nofollow']")
addBasket.click()
time.sleep(1)
basket = driver.find_element_by_css_selector("span[class='cartcontents']")
basket.click()
time.sleep(2)
checkoutButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
checkoutButton.click()
firstNameField_check = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")))
firstNameField = driver.find_element_by_id("billing_first_name")
firstNameField.send_keys("Roman")
lastNameField = driver.find_element_by_id("billing_last_name")
lastNameField.send_keys("Plus")
emailField = driver.find_element_by_id("billing_email")
emailField.send_keys("test11@gmail.com")
phoneField = driver.find_element_by_id("billing_phone")
phoneField.send_keys("89744564892")
selectorCountry = driver.find_element_by_id("select2-chosen-1")
selectorCountry.click()
findCountry = driver.find_element_by_css_selector("input[id='s2id_autogen1_search']")
findCountry.send_keys("Russia")
findCountryLine = driver.find_element_by_css_selector(".select2-results-dept-0")
findCountryLine.click()
driver.execute_script("window.scrollBy(0, 600);")
addressField = driver.find_element_by_id("billing_address_1")
addressField.send_keys("Lenina 1")
cityField = driver.find_element_by_id("billing_city")
cityField.send_keys("Syktyvkar")
countryField = driver.find_element_by_id("billing_state")
countryField.send_keys("Russia")
postcodeField = driver.find_element_by_id("billing_postcode")
postcodeField.send_keys("326736")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
paymentsRadiobutton = driver.find_element_by_id("payment_method_cheque")
paymentsRadiobutton.click()
time.sleep(2)
orderButton = driver.find_element_by_id("place_order")
orderButton.click()
time.sleep(2)
order_check = wait.until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_check = wait.until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table>tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()


