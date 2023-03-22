#Facebook Site Access

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("Dhaval")

driver.find_element(By.NAME,"lastname").send_keys("Khatri")

driver.find_element(By.ID, "password_step_input").send_keys("abc@gmail.com")

driver.find_element(By.XPATH,"//input[@value='-1']").click()
time.sleep(5)
