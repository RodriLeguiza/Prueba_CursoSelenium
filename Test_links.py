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

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

#obeniendo todos los links de la pagina

links = driver.find_elements(By.TAG_NAME, "a")
print("el numero de links que hay en la pagina es: ",len(links))

for num in links:
    print(num.text)
driver.find_element(By.LINK_TEXT, "Date pickers").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Others").click()
time.sleep(t)



driver.close()