#pdf to word converter

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.ilovepdf.com/pdf_to_word")
driver.find_element(By.XPATH,"").send_keys("C:\Users\PM Essentials - slides.pdf")