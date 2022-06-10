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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

btn2 = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
print(btn2.is_enabled())

if(btn2.is_enabled()==True):
    print("Puedes dar clic")
else:
    print("No puedes dar click")

time.sleep(2)
driver.close()