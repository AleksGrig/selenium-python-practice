from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")

# requests package needed
broken_links = 0
links = driver.find_elements(By.TAG_NAME, 'a')
print("link number is ", len(links))

for link in links:
  url = link.get_attribute('href')
  try:
    response = requests.head(url)
  except:
    None
  if response.status_code >= 400:
    broken_links += 1
    print(url, "is broken")

print("broken links number is: ", broken_links)
driver.quit()
