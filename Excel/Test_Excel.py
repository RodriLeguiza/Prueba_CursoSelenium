import time
import unittest
import warnings

from Excel.Funciones_Excel import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_globales

t = .01

class base_test(unittest.TestCase):


    def setUp(self):
        s = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.t = t
        warnings.simplefilter('ignore', ResourceWarning)

    def test1(self):
        driver = self.driver
        f = Funciones_globales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box", t)
        ruta = "C://Users//RODRIGO//PycharmProjects//PrjectMV//Maquina_uno//MV1//Excel//Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")
        print("La cantidad de filas son: " + str(filas))



        for c in range(2, filas + 1):
            nombre = fe.readData(ruta, "Hoja1", c, 1)
            email = fe.readData(ruta, "Hoja1", c, 2)
            dir1 = fe.readData(ruta, "Hoja1", c, 3)
            dir2 = fe.readData(ruta, "Hoja1", c, 4)

            f.Texto_Mixto("id", "userName", nombre, t)
            f.Texto_Mixto("id", "userEmail", email, t)
            f.Texto_Mixto("id", "currentAddress", dir1, t)
            f.Texto_Mixto("id", "permanentAddress", dir2, t)
            f.Click_Mixto("id", "submit", t)

            e = f.Existe("id", "name", t)
            if(e == "Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta, "Hoja1", c, 5, "insertado")

            else:
                print("No se inserto")
                fe.writeData(ruta, "Hoja1", c, 5, "Error")



    def tearDown(self):
            t = self.t
            driver = self.driver
            driver.close()

if __name__ == '__main__':
        unittest.main()