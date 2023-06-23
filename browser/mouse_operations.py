from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# this option forces selenium not to close browser after script execution
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(10)
driver.maximize_window()


# mouse hover action
driver.get("https://demo.automationtesting.in/Register.html")
interactions = driver.find_element(
    By.XPATH, "//a[contains(text(),'Interactions')]")
drag_n_drop = driver.find_element(
    By.XPATH, "//a[contains(text(),'Drag and Drop')]")
static = driver.find_element(By.XPATH, "//a[contains(text(),'Static')]")
actions = ActionChains(driver)
actions.move_to_element(interactions).move_to_element(
    drag_n_drop).move_to_element(static).click().perform()


# right click action
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# btn = driver.find_element(By.XPATH, "//span[text()='right click me']")
# actions = ActionChains(driver)
# actions.context_click(btn).perform()


# double click action
# driver.get(
#     "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# driver.switch_to.frame("iframeResult")
# txt_field = driver.find_element(By.ID, "field1")
# txt_field.clear()
# txt_field.send_keys("Try!!!")
# btn = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
# actions = ActionChains(driver)
# actions.double_click(btn).perform()


# drag and drop action
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# rome = driver.find_element(By.ID, "box6")
# italy = driver.find_element(By.ID, "box106")
# actions = ActionChains(driver)
# actions.drag_and_drop(rome, italy).perform()


# slider operation
# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
# sliders = driver.find_elements(By.CSS_SELECTOR, ".ui-slider-handle")
# left = 0
# right = 1

# # left x: 59, right x: 510
# print(sliders[left].location, sliders[right].location)
# actions = ActionChains(driver)
# actions.drag_and_drop_by_offset(sliders[left], 200, 0).perform()
# actions.drag_and_drop_by_offset(sliders[right], -200, 0).perform()


# scrolling page
# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scrolling by pixel number
# driver.execute_script("window.scrollBy(0,3000)", "")
# y_offset = driver.execute_script("return window.pageYOffset;")
# print(y_offset)


# scrolling till element is visible
# india_flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", india_flag)
# y_offset = driver.execute_script("return window.pageYOffset;")
# print(y_offset)


# scrolling till the end of the page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# y_offset = driver.execute_script("return window.pageYOffset;")
# print(y_offset)


# scrolling up to the starting position
# sleep(3)
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
