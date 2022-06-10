import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\DRIVERS\geckodriver.exe")
driver = webdriver.Firefox(service=s)

driver.get("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
driver.maximize_window()
driver.implicitly_wait(10)
t = 1
time.sleep(t)

driver.find_element(By.XPATH, "//input[@placeholder='Nombre:']").send_keys("Rodrigo")
time.sleep(t)
driver.find_element(By.XPATH, "//input[@placeholder='Apellidos']").send_keys("Leguiza")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@type,'email')]").send_keys("grl0969@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@type,'tel')]").send_keys("2616610784")
time.sleep(t)
driver.find_element(By.XPATH, "//textarea[@placeholder='Email']").send_keys("Francisco Moyano")
time.sleep(t)
driver.execute_script("window.scrollTo(0,800)")
time.sleep(t)
driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Submit')]").click()
time.sleep(t)

driver.close()
