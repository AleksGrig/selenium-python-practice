from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)
driver.find_element(By.NAME,'username').send_keys('Admin')
time.sleep(3)
driver.find_element(By.NAME,'password').send_keys('admin123')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()

if driver.find_element(By.CSS_SELECTOR,"img[alt='client brand banner']"):
  print("Login Test passed")
else:
  print("Login Test failed")

time.sleep(5)
driver.close()