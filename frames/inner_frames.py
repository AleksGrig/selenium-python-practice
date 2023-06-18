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

driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()

# switch to outer frame
driver.switch_to.frame(driver.find_element(
    By.XPATH, "//iframe[@src='MultipleFrames.html']"))

# switch to inner frame
driver.switch_to.frame(driver.find_element(
    By.XPATH, "//iframe[@src='SingleFrame.html']"))

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Hi there!")

# switch back to parent frame, only from selenium4
driver.switch_to.parent_frame()
