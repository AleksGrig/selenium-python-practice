from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# this option forces selenium not to close browser after script execution
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# driver.switch_to.window(window_id) -> switching to another window
# current_window_handle -> window_id of a single browser window
# window_handles -> window_ids of multiple browser windows

# window_id = driver.current_window_handle
# print(window_id)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
window_ids = driver.window_handles
print(window_ids)

# switching to child window
driver.switch_to.window(window_ids[1])
print(driver.title)

# switching back to parent window
driver.switch_to.window(window_ids[0])
print(driver.title)
