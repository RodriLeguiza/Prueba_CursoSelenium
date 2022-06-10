import time
from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\DRIVERS\geckodriver.exe")
driver=webdriver.Firefox(service=s)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(By.ID,"userName")
nom.send_keys("RodrigoLeguiza")
nom.send_keys(Keys.TAB + "grl0969@gmail.com" + Keys.TAB + "Francisco Moyano" + Keys.TAB + "sexta seccion" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,500)")

time.sleep(4)

driver.close()
