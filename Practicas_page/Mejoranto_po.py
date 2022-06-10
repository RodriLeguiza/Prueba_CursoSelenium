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
from selenium.common.exceptions import InvalidSessionIdException
from Funciones.Funciones import Funciones_globales
from Funciones.Page_Login import Pagina_Login


t = 5
class mejorandofunciones(unittest.TestCase):

    def setUp(self):
        s = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        time.sleep(t)
        warnings.simplefilter('ignore', ResourceWarning)

    def testTexto(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://testingqarvn.com.es/prueba-de-campos-checkbox/", t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'wsf-1-field-29')]", "RODRIGO", t)
        f.Texto_Mixto("id", "wsf-1-field-30", "LEGUIZA", t)
        f.Click_Mixto("xpath", "//label[contains(@id,'wsf-1-label-36-row-1')]", t)
        f.Click_Mixto("id", "wsf-1-label-36-row-3", t)

    def testSelect(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://testingqarvn.com.es/combobox-dependiente/", t)
        f.Select_Mixto_Type("xpath", "//select[contains(@id,'wsf-1-field-61')]", "texto", "Linux", t)
        f.Select_Mixto_Type("id", "wsf-1-field-64", "texto", "Debian", t)





