#Site Access

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicity_wait(30)
driver.get("https://www.db4free.net/")
time.sleep(5)
driver.switch_to.winodow(driver.window_handles[0])
driver.find_element(By.PARTIAL_LINK_TEXT,"phpMyAdmin").click()
print(driver.window_handles)
time.sleep(5)

print(driver.window_hanldles)
for window in driver.driver.window_handles:
    print(window)
    driver.switch_to.window(window)
    print(driver.title)
    if driver.title=="phpMyAdmin"
