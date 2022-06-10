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
from selenium.webdriver import ActionChains


t = 2
class base_test(unittest.TestCase):
    def setUp(self):
        #s = Service("C:\Drivers\geckodriver.exe")
        #self.driver = webdriver.Firefox(service=s)
        s = Service("C:\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.t = t
        warnings.simplefilter('ignore', ResourceWarning)


    def test1(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", t)

        f.Texto_Mixto("xpath", "//input[@id='firstName']", "Rodrigo", t)

        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(t)
        act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        time.sleep(t)
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(t)
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys("@gmail.com").perform()
        time.sleep(t)









    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()