from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

xpath_syntax = "//*[contains(text(), 'English')]"
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# 0. Wait for language to pop up, select the language
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, xpath_syntax))
)

language = driver.find_element(By.XPATH, xpath_syntax)
language.click()

# 1. Find the big cookie on the page
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)


# 2. Find the cookie count on the page and print it every time you press the cookie button
while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text
    cookies_count = cookies_count.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", "")) # might have commas in the number
    print(cookies_count)
    
    # 3. Look for the possible upgrades
    num_products = 4
    for i in range(num_products):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        # make sure product price is a string (it might not be...)
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count > product_price:
            product = driver.find_element(By.ID, product_prefix + str(i)) # find the button so we can click on that (clicking on price does nothing)
            product.click()
            break # break for loop so that we go back