import time
import allure
import pytest
import warnings

from  allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t = .5



class base_test(unittest.TestCase):
    def setUp(self):
        #s = Service("C:\Drivers\geckodriver.exe")
        #self.driver = webdriver.Firefox(service=s)
        global driver, f
        s = Service('C:\Drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        warnings.simplefilter('ignore', ResourceWarning)
        f = Funciones_globales(driver)



    def test1(self):
        driver = self.driver
        f = Funciones_globales(driver)









    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()