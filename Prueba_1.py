import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

s = Service('C:\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
t = 1

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("German Rodrigo")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("Leguiza Reinoso")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'email')]").send_keys("grl0969@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("2616610784")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("Francisco Moyano 2825")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Mendoza")
time.sleep(t)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(t)
stateSelect=driver.find_element(By.XPATH, "//select[contains(@name,'state')]")
ss=Select(stateSelect)

ss.select_by_index(33)
time.sleep(t)
# debe seleccionar New York

driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("5500")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys(
    "https://www.facebook.com/german.leguiza.52/")
time.sleep(t)
driver.find_element(By.XPATH, "//input[contains(@value,'no')]").click()
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@class,'form-control')]").send_keys("Este proyecto cuenta con la idea de realizar la primera prueba")
time.sleep(t)
driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]").click()
time.sleep(t)

driver.close()