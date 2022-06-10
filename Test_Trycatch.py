import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

s = Service("C:\DRIVERS\geckodriver.exe")
driver = webdriver.Firefox(service=s)

driver.get("https://testingqarvn.com.es/combobox/")
driver.maximize_window()
driver.implicitly_wait(10)
t = .5

driver.find_element(By.XPATH, "//input[@placeholder='Nombre:']").send_keys(
    "Rodrigo" + Keys.TAB + "Leguiza" + Keys.TAB + "grl0969@gmail.com" + Keys.TAB + "2616610785" + Keys.TAB + "Francisco Moyano")
time.sleep(t)
driver.execute_script("window.scrollTo(0,800)")
btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'PHP')]")))
btn1.click()
time.sleep(t)
btn2 = driver.find_element(By.XPATH, "//label[contains(.,'PYTHON')]")
btn2.click()
time.sleep(t)
btn3 = driver.find_element(By.XPATH, "//label[contains(.,'WebdriverIO')]")
btn3.click()
time.sleep(t)

try:
    sisSelect = driver.find_element(By.XPATH, "//select[contains(@id,'wsf-1-field-53')]")
    ss = Select(sisSelect)
    ss.select_by_visible_text("Linux")
    time.sleep(t)
    ss.select_by_index(1)
    time.sleep(t)
    ss.select_by_value("Windows")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(t)
driver.close()
