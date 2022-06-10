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

@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    s = Service('C:\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    f = Funciones_globales(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/", t)
    driver.maximize_window()
    driver.implicitly_wait(10)
    f.Texto_Mixto("xpath", "//input[@id='txtUsername']", "Admin", t)
    f.Texto_Mixto("xpath", "//input[@id='txtPassword']", "admin123", t)
    f.Click_Mixto("xpath", "//input[contains(@id,'btnLogin')]", t)
    print("Entrando en el sistema")


def teardown_function():
    print("Fin de etodos los test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    etiqueta = f.SEX("//h1[contains(.,'Dashboard')]").text
    print(etiqueta)
    assert etiqueta == "Dashboard", "No estas en la pagina de inicio"


