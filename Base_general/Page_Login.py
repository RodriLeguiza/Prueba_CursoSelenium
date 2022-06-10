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
from selenium.webdriver import ActionChains
from Funciones import Funciones_globales

t = .5

class Funciones_Login():
    def __init__(self, driver):
        self.driver = driver

    def L1(self, email, clave, mensaje, t=.5):
        s = Service('C:\Drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        warnings.simplefilter('ignore', ResourceWarning)
        f = Funciones_globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[contains(@type,'submit')]", t)
        e1 = f.SEX("/html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]")
        e1 = e1.text
        print(e1)
        if (e1 == mensaje):
            print("La prueba de validacion es exitosa")
        else:
            print("la prueba de validacion es incorrecta")
        driver.close()

    def L2(self, email, clave, mensaje, t =.5):
        s = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        warnings.simplefilter('ignore', ResourceWarning)
        f = Funciones_globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[contains(@type,'submit')]", t)
        e1 = f.SEX("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        print(e1)
        if (e1 == mensaje):
            print("Prueba de email vacio es exitosa")
        else:
            print("Prueba de email no exitosa")

        driver.close()

    def L3(self, email, clave, mensaje, t =.5):
        s = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        warnings.simplefilter('ignore', ResourceWarning)
        f = Funciones_globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[contains(@type,'submit')]", t)
        e1 = f.SEX("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        print(e1)

        if (e1 == mensaje):
            print("Prueba de email no valido es exitosa")
        else:
            print("Prueba de email no valido es incorrecta")

        driver.close()

    def L4(self, email, clave, mensaje, t =.5):
        global driver
        s = Service("C:\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        warnings.simplefilter('ignore', ResourceWarning)
        f = Funciones_globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[contains(@type,'submit')]", t)
        e1 = f.SEX("//h1[contains(.,'Dashboard')]")
        e1 = e1.text
        print(e1)

        if (e1 == mensaje):
            print("Login exitoso")
        else:
            print("Prueba no exitosa")
        driver.close()
