import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\DRIVERS\geckodriver.exe")
driver=webdriver.Firefox(service=s)

driver.get("https://www.elit.com.ar/index.html")
driver.maximize_window()
t = 1

driver.find_element(By.XPATH,"//a[contains(.,'Usuario')]").click()
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@name,'username')]").send_keys("12338")
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@type,'password')]").send_keys("elit2")
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@type,'submit')]").click()
time.sleep(t)

driver.close()
