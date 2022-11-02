# application commands
# conditional commands
# browser commands
# navigational commands
# wait commands

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait # explicit wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.maximize_window()

# application commands
driver.get("https://demo.nopcommerce.com/register")
print(driver.title)
print(driver.current_url)
print(driver.page_source)


# conditional commands
search_box = driver.find_element(By.NAME,'q')
print("search_box is_displayed:",search_box.is_displayed())
print("search_box is_enabled:",search_box.is_enabled())
female_radiobtn = driver.find_element(By.CSS_SELECTOR,"#gender-female")
print("female_radiobtn is_selected",female_radiobtn.is_selected())
newsletter_chkbx = driver.find_element(By.CSS_SELECTOR, "input[id='Newsletter']")
print("newsletter_chkbx is_selected",newsletter_chkbx.is_selected())


# browser commands
# close() -> closes single browser window(where driver is focused)
# quit() -> closes all browser windows associated with a driver(internally kills browser's process)


# navigational commands
# driver.get("https://www.snapdeal.com/")
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()


# wait commands
# time.sleep(sec) -> reduced performance bc sleeps exact number of secs even if element is available,
#                 -> works only once,
#                 -> exception if element is not available after time mentioned
# implicit wait   -> driver.implicitly_wait(sec), 
#                 -> works everywhere in the code after declaration,
#                 -> performance is not reduced, 
#                 -> exception if element is not available after time mentioned
# explicit wait   
# explicit_wait = WebDriverWait(driver, 10) # simple declaration
explicit_wait = WebDriverWait(driver,
                              10,
                              poll_frequency=2,
                              ignored_exceptions=[NoSuchElementException,
                                                  ElementNotVisibleException]) 
reg_btn = explicit_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#register-button")))


# find_element & find_elements
# find_element  -> returns single webelement,
#               -> if locator matches multiple webelement -> it returns first match on the page
#               -> if locator matches no webelements -> NoSuchElementException exception is thrown
# find_elements -> returns list of webelements
#               -> if locator matches no webelements -> empty list is returned


# text vs get_attribute('value')
# text returns inner text of an element
# get_attribute('value') returns whatever is assigned to 'value' attribute of an element


driver.quit()