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

def get_Datos():
    return [
        ("Rodrigo@gmail.com", "1234"),
        ("Juan@gmail.com", "1233334"),
        ("Pedro@gmail.com", "12567734"),
        ("Erica@gmail.com", "123435534"),
        ("Carlos@gmail.com", "123dfhuk4"),
        ("admin@yourstore.com", "admin")
    ]



@pytest.mark.login
@pytest.mark.parametrize("user,clave", get_Datos())
def test_login(user,clave):
    global driver, f
    s = Service('C:\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    f = Funciones_globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "Email", user, t)
    f.Texto_Mixto("id", "Password", clave, t)
    f.Click_Mixto("xpath", "//button[@type='submit']", t)
    print("Entrando al sistema")

def teardown_function(function):
    print("salida del test")
    driver.close()



