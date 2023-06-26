from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service("drivers/chromedriver_win32/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service_obj, options=options)
    return driver


def headless_edge():
    from selenium.webdriver.edge.service import Service
    service_obj = Service("drivers/edgedriver_win64/msedgedriver.exe")
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Edge(service=service_obj, options=options)
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    service_obj = Service("drivers/geckodriver-v0.32.0-win32/geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.binary_location = 'C:\Program Files\Mozilla Firefox\\firefox.exe'
    options.headless = True
    driver = webdriver.Firefox(service=service_obj, options=options)
    return driver


driver = headless_firefox()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
driver.close()
