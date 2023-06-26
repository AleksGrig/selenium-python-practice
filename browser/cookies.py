from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# get all cookies from the browser
# cookies = driver.get_cookies()
# print(cookies)

# add new cookie to the browser
driver.add_cookie({
    "name": "my_cookie",
    "value": "13"
})
cookies = driver.get_cookies()
print(cookies)

# delete specific cookie from the browser
driver.delete_cookie("my_cookie")
cookies = driver.get_cookies()
print()
print(cookies)

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print()
print(cookies)
