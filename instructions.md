# Selenium

Selenium is a simple yet powerful tool used to create bots, web automation, & more using Python.

## 0. Project Setup

Download a text editor, such as VSCode or Sublime Text. (I prefer VSCode)

[Link to Download VSCode](https://code.visualstudio.com/download)

[Link to Download Sublime Text](https://www.sublimetext.com/)

In the VSCode Terminal/Command Prompt, setup the local project directory:

```sh
mkdir selenium
cd selenium
```

Head to [Github](https://github.com/) and create a new remote repository named `selenium`.

Following the creation of your new remote repository, create a new local repository on the command line:

```sh
echo "# selenium" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/selenium.git
git push -u origin main
```

Save this file as a markdown file `/selenium/instructions.md`, then open up a new VSCode instance and Open folder > `selenium`.

Next, setup a virtual Python environment:

```sh
cd selenium
py -m venv env
```

You should now see a folder 'env' with a python.exe program in the /Scripts directory.

Create a .gitignore file for the Python project and save it in the root directory `selenium`:

```sh
cd selenium
echo > .gitignore
```

Code for .gitignore: [Link to file](https://github.com/github/gitignore/blob/main/Python.gitignore)

Activate the virtual environment in the terminal, and update pip while you're at it:

```sh
where python
.\env\Scripts\activate

python.exe -m pip install --upgrade pip
pip list
```

Note: You can leave the virtual environment with this call:

```sh
deactivate
```

Install the necessary packages into your virtual environment:

```sh
pip install selenium
```

Create a requirements.txt file to ensure that you have the necessary dependencies to run this code:

```sh
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Note:
- 1st line of code: Creates a requirements.txt file
- 2nd line of code: Download the necessary libraries again (Optional)

Create a main Python file, which we will be working from:

```sh
echo > main.py
```

Begin with the necessary imports:

```py
# main.py
import selenium
```

Ensure this runs by heading into the terminal with the virtual environment running:

```sh
python main.py
```

Note: In Sublime, you can run the code with the following command: Ctrl-B

Save these files and update git before beginning the project:

```sh
cd selenium

git status
git add .
git commit -m "Completed project setup"
git push -u origin main
git status
git log --oneline
q
```

## 1. Installing Selenium

Instructions:
1. Download Google Chrome
- Link: https://www.google.com/chrome/
    - If you already have google chrome, I would suggest updating to the latest version.
- After downloading, make sure that you write down which version you have:
    - Open Chrome
    - Click the three-dot icon in the top right corner of the browser window
    - Click or hover over Help
    - Click 'About Google Chrome'
    - Look for the Version number just under the Google Chrome heading and icon
        - I am currently using the most up to date version (as of 3/12/2024): Version 122.0.6261.112 (Official Build) (64-bit)

2. Download Chrome WebDriver
- Link: [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/)
    - Click on 'Stable' version for the most recent version of Chrome (probably will be at the top)
    - Now that you are in the Stable Links page (https://googlechromelabs.github.io/chrome-for-testing/#stable), find the link for the following:
        - Binary: chromedriver
        - Platform: win64
    - Copy and paste that link into your browser
        - Download the .zip into /Downloads -> Extract All...
        - Cut/paste the chromedriver.exe file into /selenium
        - Delete the folders you just brought into /Downloads

3. Import the Chrome WebDriver into Python

Here is a quick example:

```py
# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()

```

Run the file to test it out:

```
python main.py
```

We now have ChromeDriver setup and can navigate to any website we would like!

## 2. Locating & Interacting With Elements

How to search for elements in HTML:
- Find an HTML element on the page
    - Google Chrome -> Right Click on an element ie. search bar -> Inspect
    - You can take down an identifier ie. the element's CLASS/ID/etc.
- 

Our example:
- Find google search field
- Click into it
- Type something
- Press enter

Example of Searching for something on Google:

```py
# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf") # find the element for the search bar
input_element.clear() # clear text box, just in there is already text inside
input_element.send_keys("tech with tim" + Keys.ENTER) # keyboard types into search box + presses enter


time.sleep(10)

driver.quit()

```

## 3. Potential Problems & Getting Blocked

Common issues:
- Banned IP address
- Booted off website
- CAPTCHA's

Why does this happen: Companies today are pretty smart and can automatically detect bots

Remedy: Push the tasks out to the cloud so that you can run multiple instances of your browser, all at once!
- Allows you to do a task 100,000's of times

## 4. Brightdata Unblocking Solution

Sponsor for the video/potential solution: [BrightData](https://brightdata.com/)
- Product: Scraping Browser API
    - What it does: Runs in the cloud, has automatic unlocking tools ie. rotates IP address/solves CAPTCHA's for you

## 5. Clicking Links & Navigating Pages

More advanced version of the example:

```py
# main.py
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

```

## 6. Automating Cookie Clickers - Sample Project

Site: https://orteil.dashnet.org/cookieclicker/

Point of game: Collect as many cookies as possible!
- Click on cookie to get more cookies
- Buy upgrades with cookies so that you can earn more via automation of cookie collection process

How we will automate this site:
- Navigate to the site
- Locate classes that we want access to when automating this site
    - How to find quickly: Right click on page -> Inspect -> Click on the arrow in the dotted square at the top left corner of the inspection window (it'll turn blue) -> Click on the element on the webpage you want to find in the html
        - The inspection window will then take you straight to the html where the element is at
    - HTML we are interested in:
        - XPATH `contains('English')`
        - button `id=bigCookie`
        - text `id=cookies`
        - text `id=productPrice{i}`
        - text `id=product{i}`

- Click on the cookie infinite times
- Iterate over upgrades to purchase them when we can afford it

Instructions:
0. Select a Language for the Webpage
- XPATH `contains('English')`
- Use XPATH to syntax to search for "English" and click on it
- How to find correct XPATH (XML Path Language):
    - Using Chrome's Developer Tools:
        - Open Chrome Developer Tools: Ctrl-Shift-I, or Right-click -> Inspect
        - Locate the Element in Developer Tools: Click element on screen -> Ctrl-Shift-C
        - Get the XPath: Right click on code -> Copy -> Click on Copy XPath or Copy full XPath.
            - This will copy the XPath expression to your clipboard, which you can then use in your Selenium scripts to locate the element.
    - Use ChatGPT:
        - About XPATH: Remember, XPaths can be brittle if the web page structure changes, so it's often wise to use more robust locators if possible, such as IDs, class names, or CSS selectors, whenever they're available and unique.

- Note: This may or may not pop up, depending on if you have already selected a language

1. Find the cookie button
- button `id=bigCookie`

2. Find the cookies count
- text `id=cookies`

3. Look for the possible upgrades
- 4 total:
    - text `id=productPrice{i}`
    - text `id=product{i}`

- Note: The product's all have id of ProductPrice0, ProductPrice1, etc.
- We will iterate through the products
    - If we have enough to purchase the product, we will click on it

```py
# cookieClickers.py
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
```

Note: Caching issues can lead to Stale element errors, you will just have to try re-running your code.

4. Repeat as long as you'd like!

---

### References

References:
1. [Python Selenium Tutorial - Automate Websites and Create Bots](https://www.youtube.com/watch?v=NB8OceGZGjA)
2. [$15 of free credit when you create a new BrightData account](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0VTNlFIeV9yWFNMbGdMNHVsYWZJSjBuM0tNQXxBQ3Jtc0ttczRMVm9YS0I3Mk40cnl5MDFQazlYQkNLdURaX0FaY08zRnNIaFJYekxxdExlN1FfWkF4enpsbUJfZFg1SjJuNmRTZUtva09vdjQtdTlHbEg5MVhGRExKRVFNcGVHbjVsa3U4Q2JqdURYVGc3MENsOA&q=https%3A%2F%2Fbrdta.com%2Ftechwithtim-selenium&v=NB8OceGZGjA)
3. [Github - SeleniumTutorial](https://github.com/techwithtim/SeleniumTutorial)
4. [Know Everything About Finding XPath In Chrome For Selenium](https://testgrid.io/blog/xpath-in-chrome-for-selenium/)
