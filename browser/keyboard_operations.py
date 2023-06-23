from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# this option forces selenium not to close browser after script execution
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com/")
text_box = driver.find_element(By.NAME, "q")
text_box.send_keys("welcome to selenium")

actions = ActionChains(driver)

# Ctrl+A -> select text
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


# Ctrl+C -> copy text
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

text_box.clear()
text_box.send_keys("Hey user, ")

# Ctrl+V -> paste text
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
