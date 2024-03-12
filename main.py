from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

search_bar_class_name = "gLFyf"
google_result_text = "Tech With Tim"

# wait for 5 seconds, until we find a class name with the given class name (useful if it doesn't exist right away)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, search_bar_class_name)) # notice use of tuple
)

input_element = driver.find_element(By.CLASS_NAME, search_bar_class_name) # find the element for the search bar
input_element.clear() # clear text box, just in there is already text inside
input_element.send_keys("tech with tim" + Keys.ENTER) # keyboard types into search box + presses enter

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, google_result_text))
)

# if "Tech With Tim" in this capitalization exists in an anchor tag or link tag, then we access it
link = driver.find_element(By.PARTIAL_LINK_TEXT, google_result_text)
# use 'By.LINK_TEXT' for first element with exact text
# use links = driver.find_elements() to get an array of all results, you can iterate over it

link.click() # redirect me to wherever this first link goes

time.sleep(3)

driver.quit()
