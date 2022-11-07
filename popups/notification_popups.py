from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# disabling notification popups
options.add_argument("--disable-notifications") 

driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://whatmylocation.com/")