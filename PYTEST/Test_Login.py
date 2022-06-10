import time
import pytest
import warnings

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

def test_login_uno():
    s = Service("C:Drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    fl = Funciones_Login(driver)
    fl.L1("rodri@gmail.com", "admin", """Login was unsuccessful. Please correct the errors and try again.
No customer account found""", t )
    fl.L2("", "admin", "Please enter your email",)
    fl.L3("Rodrigo", "admin", "Wrong email",)
    fl.L4("admin@yourstore.com", "admin", "Dashboard")













