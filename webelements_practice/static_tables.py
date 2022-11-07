from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

# count number of rows and columns of a table
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable'] //tr")
rows_count = len(rows)
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
columns_count = len(columns)
print("rows:", rows_count, "columns:", columns_count)

# read data from specific row and column(row:5, column:1)
data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
print(data)

# read all rows and columns data
print("----------all data from the table----------")
for row in range(2, rows_count+1):
  for column in range(1, columns_count+1):
    data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[{}]/td[{}]".format(row, column)).text
    print(data, " | ", sep="", end="")
  print()

# read data based on condition(author is Mukesh)
for row in range(2, rows_count+1):
  author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[{}]/td[2]".format(row)).text
  if author == 'Mukesh':
    title = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[{}]/td[1]".format(row)).text
    print(title, author)
