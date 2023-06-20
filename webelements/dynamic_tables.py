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

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//span[text()='Admin']").click()

rows = driver.find_elements(
    By.XPATH, "//div[@class='oxd-table-body']/div")
print("Total number of rows:", len(rows))

columns = driver.find_elements(
    By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div")
last_column = len(columns) - 1
print("Number of last column:", last_column)
enabled = 0
disabled = 0

for index in range(1, len(rows)+1):
    status = driver.find_element(
        By.XPATH, f"//div[@class='oxd-table-body']/div[{index}]/div/div[{last_column}]").text
    if status == 'Enabled':
        enabled = enabled + 1
    if status == 'Disabled':
        disabled = disabled + 1

print("Total number of enabled users:", enabled)
print("Total number of disabled users:", disabled)
