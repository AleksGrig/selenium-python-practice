from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker")

driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

# send date directly if possible
# driver.find_element(By.ID, "datepicker").send_keys("10/20/2021")

months = {
  "January":  0,
  "February": 1,
  "March":    2,
  "April":    3,
  "May":      4,
  "June":     5,
  "July":     6,
  "August":   7,
  "September":8,
  "October":  9,
  "November": 10,
  "December": 11
}

year = "2023"
month = "October"
day = "20"

driver.find_element(By.ID, "datepicker").click()

# if int(driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text) > int(year):
#   while driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text != year:
#     driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-w").click()
# elif int(driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text) < int(year):
#   while driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text != year:
#     driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-e").click()

# if months.get(driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text) > months.get(month):
#   while driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text != month:
#     driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-w").click()
# elif months.get(driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text) < months.get(month):
#   while driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text != month:
#     driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-e").click()

# driver.find_element(By.LINK_TEXT, day).click()

while True:
  year_picker = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
  month_picker = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
  previous = driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-w")
  next = driver.find_element(By.CSS_SELECTOR, ".ui-icon.ui-icon-circle-triangle-e")

  if year == year_picker and month == month_picker:
    break
  else:
    if int(year_picker) > int(year):
      previous.click()
    elif int(year_picker) < int(year):
      next.click()
    else:
      if months.get(driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text) > months.get(month):
        previous.click()
      else:
        next.click()

driver.find_element(By.LINK_TEXT, day).click()
