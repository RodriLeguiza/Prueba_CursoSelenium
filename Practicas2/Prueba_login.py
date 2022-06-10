import time
import unittest
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class pruebalogin(unittest.TestCase):
    def setUp(self):
        s = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.t = 2
        warnings.simplefilter('ignore' , ResourceWarning)

    def test_login1(self):
        t = self.t
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba uno OK")
            time.sleep(t)


    def test_login2(self):
        t = self.t
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba dos OK")
            time.sleep(t)

    def test_login3(self):
        t = self.t
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("rodrigo")
        clave.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(.,'Epic sadface: Password is required')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Password is required"):
            print("Falta el password")
            print("Prueba tres OK")
            time.sleep(t)

    def test_login4(self):
        t = self.t
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta el usuario y el password")
            print("Prueba cuatro OK")
            time.sleep(t)

    def test_login5(self):
        t = self.t
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        btn.click()
        elemento = driver.find_element(By.XPATH,"//div[contains(@class,'app_logo')]")
        elemento.is_enabled()
        print("El elemento es: " +str(elemento))
        print("Prueba cinco Ok")
        '''error = driver.find_element(By.XPATH,
                                    "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        # print(error)
        if (error == "Epic sadface: Username is required"):
            print("Falta el usuario y el password")
            print("Prueba cuatro OK")'''

        time.sleep(t)

    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()