import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\DRIVERS\geckodriver.exe")
driver = webdriver.Firefox(service=s)

driver.get("https://testingqarvn.com.es/combobox/")
driver.maximize_window()
driver.implicitly_wait(10)
t = 2

driver.find_element(By.XPATH, "//input[@placeholder='Nombre:']").send_keys(
    "Rodrigo" + Keys.TAB + "Leguiza" + Keys.TAB + "grl0969@gmail.com" + Keys.TAB + "2616610785" + Keys.TAB + "Francisco Moyano")
time.sleep(3)
driver.execute_script("window.scrollTo(0,800)")
btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'PHP')]")))
btn1.click()
time.sleep(3)
btn2 = driver.find_element(By.XPATH, "//label[contains(.,'PYTHON')]")
btn2.click()
time.sleep(3)

sisSelect = driver.find_element(By.XPATH, "//select[contains(@id,'wsf-1-field-53')]")
ss = Select(sisSelect)
ss.select_by_visible_text("Linux")
time.sleep(2)
ss.select_by_index(2)
time.sleep(2)
ss.select_by_value("Windows")
time.sleep(2)
driver.close()
