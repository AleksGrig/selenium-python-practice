from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# this option forces selenium not to close browser after script execution
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application")

# Date of birth element
driver.find_element(By.ID, "dob").click()
year_select = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
year_select.select_by_visible_text("1966")
month_select = Select(driver.find_element(
    By.CLASS_NAME, "ui-datepicker-month"))
month_select.select_by_visible_text("Nov")
driver.find_element(By.LINK_TEXT, "22").click()
