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


class base_test(unittest.TestCase):
    def setUp(self):
        s = Service("C:\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.t = 2
        warnings.simplefilter('ignore', ResourceWarning)

    def test1(self):
        t = self.t
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        time.sleep(t)


    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()

if __name__=='__main__':
    unittest.main()







