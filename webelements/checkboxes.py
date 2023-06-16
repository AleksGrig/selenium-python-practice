from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# selenium doesn't quit automaticly after script execution
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

# select specific checkbox
# driver.find_element(By.CSS_SELECTOR, "#monday").click()

# select multiple checkboxes(all days of the week)
# days_of_week = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
days_of_week = driver.find_elements(
    By.XPATH, "//input[@class='form-check-input' and contains(@id, 'day')]")
# for day in days_of_week:
#   day.click()

# select multiple checkboxes based on user choice
for day in days_of_week:
    if day.get_attribute('id') == 'saturday' or day.get_attribute('id') == 'sunday':
        day.click()
