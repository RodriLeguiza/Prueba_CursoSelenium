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
driver = ""

def setup_function(function):
    global driver,f
    s = Service('C:\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    f = Funciones_globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    driver.maximize_window()
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit']", t)
    print("iniciando nuestros test")

def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Texto_Mixto("xpath", "//input[@id='SearchProductName']", "Computer", t)
    f.Click_Mixto("xpath", "//button[@id='search-products']", t)

def test_dos():
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath", "//a[@href='/Admin/Product/Create']", t)
    f.Texto_Mixto("xpath", "//input[@id='Name']", "Computadora de tipo dell", t)
    f.Texto_Mixto("xpath", "//textarea[@id='ShortDescription']", "descripcion corta", t)
    f.Click_Mixto("xpath", "//span[contains(.,'File')]", t)
    f.Click_Mixto("xpath", "//div[@class='tox-collection__item-label'][contains(.,'New document')]", t)
    driver.switch_to.frame("FullDescription_ifr")
    #f.Texto_Mixto("id", "tinymce", "descripcion larga", t)
    #f.Texto_Mixto("xpath", "//INPUT[@id='Sku']", "se escribio en skf", 2)
    campo = driver.find_element(By.ID, "tinymce")
    campo.send_keys("descripcion larga" + Keys.TAB + "se llenos skf")
    time.sleep(2)








