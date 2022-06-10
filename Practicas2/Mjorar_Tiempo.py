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


t = .2
class mejorandotiempos(unittest.TestCase):

    def setUp(self):
        s = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        time.sleep(t)
        warnings.simplefilter('ignore', ResourceWarning)

    def testTiempo(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demoqa.com/text-box", t)
        f.Texto_Mixto("id", "userName", "Rodrigo", t)
        f.Texto_Mixto("id", "userEmail", "aselectronica2000@gmail.com", t)
        f.Texto_Mixto("id", "currentAddress", "Francisco Moyano", t)
        f.Texto_Mixto("id", "permanentAddress", "Mendoza - Argentina", t)
        f.Click_Mixto("id", "submit", t)