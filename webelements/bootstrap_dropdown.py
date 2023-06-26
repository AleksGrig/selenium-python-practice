from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(
    By.CSS_SELECTOR, "#select2-billing_country-container").click()
countries = driver.find_elements(
    By.XPATH, "//ul[@class='select2-results__options']/li")

for country in countries:
    if country.text == "India":
        country.click()
        break
