import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily/groupall")

# driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td").click()

# self //tag[@attribute='value']/self::tag
# driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/self::td").click()

# parent //tag[@attribute='value']/parent::tag
#driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/parent::td").click()

# children and ancestor //tag[@attribute='value']/child::tag
# children = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/child::td")
# for child in children:
#   print(child.text)

# ancestor //tag[@attribute='value']/ancestor::tag
# text_msg = driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr").text
# print(text_msg) # Tourism Finance B 71.15 81.40 + 14.41

# descendant //tag[@attribute='value']/descendant::tag
# elements = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/descendant::*")
# for element in elements:
#   print(element.text)

# following //tag[@attribute='value']/following::tag
# elements = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/following::tr")
# print(len(elements))

# following //tag[@attribute='value']/following-sibling::tag
# elements = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/following-sibling::tr")
# print(len(elements))

# preceding //tag[@attribute='value']/preceding::tag
# elements = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/preceding::tr")
# print(len(elements))

# preceding //tag[@attribute='value']/preceding-sibling::tag
# elements = driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr[11]/td/a/ancestor::tr/preceding-sibling::*")
# print(len(elements))

time.sleep(5)
driver.quit()