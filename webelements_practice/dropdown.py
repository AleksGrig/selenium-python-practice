from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")

country_dropdown = driver.find_element(By.CSS_SELECTOR, "#input-country")
country_select = Select(country_dropdown)

# select an option from dropdown
# country_select.select_by_visible_text("Thailand")
# country_select.select_by_value("14")
country_select.select_by_index(14)

# capture all the options and print them
all_options = country_select.options
print("total number of options:", len(all_options))