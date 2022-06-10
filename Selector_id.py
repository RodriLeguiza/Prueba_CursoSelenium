import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\DRIVERS\geckodriver.exe")
driver=webdriver.Firefox(service=s)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID,"userName").send_keys("Rodrigo Leguiza")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("grl0969@gmail.com")
time.sleep(2)
driver.find_element(By.ID,"currentAddress").send_keys("Francisco Moyano")
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys("Sexta Seccion - Ciudad")
time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element(By.ID,"submit").click()
time.sleep(2)

driver.close()
