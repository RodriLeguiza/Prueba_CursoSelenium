import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\DRIVERS\geckodriver.exe")
driver=webdriver.Firefox(service=s)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

