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
t = 2

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
time.sleep(t)
try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    Buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(2)

except TimeoutException as ex:
    print(ex.msg)
    print("el elemento no esta disponible")


time.sleep(2)
driver.close()