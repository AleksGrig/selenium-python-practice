from selenium import webdriver
from selenium.webdriver.common.by import By
import os


current_directory = os.getcwd()

def chrome_setup():
  from selenium.webdriver.chrome.service import Service
  service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")

  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])

  # download file to desired folder
  preferences = {
    "download.default_directory": "{}\downloads".format(current_directory),
    "plugins.always_open_pdf_externally": True # to download pdf file instead of open it
  }
  options.add_experimental_option("prefs", preferences)

  driver = webdriver.Chrome(service=service_obj,options=options)
  driver.implicitly_wait(10)
  driver.maximize_window()
  return driver

def edge_setup():
  from selenium.webdriver.edge.service import Service
  service_obj = Service("drivers/edgedriver_win64/msedgedriver.exe")

  options = webdriver.EdgeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])

  # download file to desired folder
  preferences = {
    "download.default_directory": "{}\downloads".format(current_directory),
    "plugins.always_open_pdf_externally": True
  }
  options.add_experimental_option("prefs", preferences)

  driver = webdriver.Edge(service=service_obj,options=options)
  driver.implicitly_wait(10)
  driver.maximize_window()
  return driver

def firefox_setup():
  from selenium.webdriver.firefox.service import Service
  service_obj = Service("drivers/geckodriver-v0.32.0-win32/geckodriver.exe")

  # firefox settings
  options = webdriver.FirefoxOptions()

  # removing download dialog window
  options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") # !!!!!!!!
  options.set_preference("browser.download.manager.showWhenStarting", False)

  # setting path to firefox
  options.binary_location = 'C:\Program Files\Mozilla Firefox\\firefox.exe'

  # download file to desired location
  options.set_preference("browser.download.folderList", 2) # 0->desktop, 1->default, 2->desired location
  options.set_preference("browser.download.dir", "{}\downloads".format(current_directory))

  # download pdf instead of open it
  options.set_preference("pdfjs.disabled", True)

  driver = webdriver.Firefox(service=service_obj,options=options)
  driver.implicitly_wait(10)
  driver.maximize_window()
  return driver

# driver = chrome_setup()
# driver = edge_setup() # bug in selenium with download pdf files using edge browser
driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
download_link = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a")

# download_link.click()
driver.execute_script("arguments[0].click();", download_link) # works for firefox

driver.switch_to.frame("aswift_3")
driver.switch_to.frame("ad_iframe")
close_btn = driver.find_element(By.XPATH, "//span[@dir='auto']")

# # close_btn.click()
driver.execute_script("arguments[0].click();", close_btn) # works for firefox