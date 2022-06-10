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
from Funciones.Funciones import Funciones_globales
from Funciones.Page_Login import Pagina_Login

t = 2

class base_test(unittest.TestCase):
    def setUp(self):
        s = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.t = 2
        warnings.simplefilter('ignore', ResourceWarning)

    def test2(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Mixto("id", "user-name", "Rodrigo", t)
        f.Texto_Mixto("id", "password", "1234", t)
        f.Click_Mixto("xpath", "//input[@id='login-button']", t)
        f.Click_Mixto("id", "login-button", t)


    def test3(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://www.saucedemo.com/", t)
        f.Texto_Xpath("//input[@id='user-name']", "Rodrigo", t)
        f.Texto_Xpath("//input[@id='password']", "1234", t)
        f.Click_Xpath("//input[@id='login-button']", t)

    def test4(self):
        driver = self.driver
        f = Funciones_globales(driver)
        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/", "standard_user", "secret_sauce", t)
        f.Salida()

    def test5(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", t)
        #f.Select_Xpath_Text("//select[@id='select-demo']", "Tuesday", t)
        f.Select_Xpath_Type("//select[@id='select-demo']", "index", "4", t)

    def test6(self):
            driver = self.driver
            f = Funciones_globales(driver)
            f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", t)
            f.Upload_Xpath("//input[@id='fileinput']", "D:\PROGRAMACION\CURSOS\Master Selenium con Python Test Qa Automation (ESPAÑOL)\Curso_selenium\Imagenes\Gato.jpg", t)
            f.Salida()

    def test7(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", t)
        f.Upload_ID("fileinput", "D:\PROGRAMACION\CURSOS\Master Selenium con Python Test Qa Automation (ESPAÑOL)\Curso_selenium\Imagenes\Gato.jpg", t)
        f.Salida()


    def test7(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", t)
        f.Check_Xpath("//input[@id='isAgeSelected']", t)
        f.Salida()


    def test8(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", t)
        f.Check_ID("isAgeSelected",t)
        f.Salida()


    def testReto(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", t)
        for n in range(2,6):
            f.Check_Xpath_Multiples(t, "(//input[@type='checkbox'])["+str(n)+"]")

        f.Salida()



    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()