import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\DRIVERS\geckodriver.exe")
driver = webdriver.Firefox(service=s)

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()
# driver.implicitly_wait(10)
t = 3
boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#at-cv-lightbox-close"))
boton.click()
time.sleep(20)

driver.close()
