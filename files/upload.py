from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


current_directory = os.getcwd()

service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.monsterindia.com/")
driver.find_element(By.XPATH, "//span[text()='Upload Resume']").click()
driver.find_element(By.ID, "file-upload").send_keys("{}\downloads\\file-sample_100kB.doc".format(current_directory))