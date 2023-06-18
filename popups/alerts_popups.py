from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# this option forces selenium to close browser after script execution
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# open alert window
driver.find_element(By.XPATH, "//button[contains(text(), 'Prompt')]").click()

# switch to alert window
alert = driver.switch_to.alert

print(alert.text)  # text from alert window
alert.send_keys("welcome")  # sending text to input box
alert.accept()  # click OK button, dismiss() -> cancel button
