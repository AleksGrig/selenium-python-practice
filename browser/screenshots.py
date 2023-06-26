from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


current_directory = os.getcwd()

service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# driver.save_screenshot("{}\screenshot.png".format(current_directory))
driver.get_screenshot_as_file(f"{current_directory}\screenshot.png")

# driver.get_screenshot_as_png() # driver.get_screenshot_as_base64 saves in binary format
