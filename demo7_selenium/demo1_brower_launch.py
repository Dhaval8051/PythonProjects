import timer
from selenium import webdriver
d =webdriver.Chrome()
d.get("https://google.com/")
print(d.title)
time.sleep(100)