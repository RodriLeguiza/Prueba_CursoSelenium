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

driver.get("https://demoqa.com/")
driver.maximize_window()

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1 = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Existe la imagen")
else:
    print("no existe la imagen")

time.sleep(2)
driver.close()