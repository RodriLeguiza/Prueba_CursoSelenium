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

class Pagina_Login():

    def __init__(self,driver):
        self.driver = driver

    def Login_Master(self, url,tipon,selectn, name,tipoc, selectc, clave, tipoe, selecte, t):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar(url, t)
        f.Texto_Mixto(tipon, selectn, name, t)
        f.Texto_Mixto(tipoc,selectc, clave, t)
        f.Click_Mixto(tipoe,selecte, t)
