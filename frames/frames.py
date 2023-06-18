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

driver.get(
    "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# switch_to.frame(name of the frame)
# switch_to.frame(id of the frame)
# switch_to.frame(webelement)
# switch_to.frame(0) -> in case of a single frame

# tag could be:
#   - frame
#   - iframe
#   - form

# switch with frame name
driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

# switch back to the page
driver.switch_to.default_content()

# switch to second frame
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "Action").click()
