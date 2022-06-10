import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

s = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
t = .5
try:
    bus = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    bus = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    bus.send_keys("C://Users//RODRIGO//PycharmProjects//Curso_Selenium//Imagenes//Gato.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    time.sleep(t)
    driver.find_element(By.XPATH,"//input[@name='upload']").click()
    time.sleep(t)



except TimeoutException as ex:
    print(ex.msg)

time.sleep(t)
driver.close()
