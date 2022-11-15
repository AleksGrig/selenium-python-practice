from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.facebook.com/")

# tag & id -> tag#id_value or #id_value
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("by_id")

# tag & class -> tag.class_value or .class_value
# driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy").send_keys("by_class")

# tag[attribute=value] or [attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("by tag[attribute=value]")

# tag class attribute 
driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy[name=email]").send_keys("by tag class attribute")
