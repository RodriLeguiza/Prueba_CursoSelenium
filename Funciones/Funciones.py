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
from selenium.webdriver import ActionChains


class Funciones_globales():
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    # FUNCION NAVEGADOR
    def Navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina abierta: " + str(url))
        t = time.sleep(tiempo)
        return t

 # FUNCION MEJORAR SELECTORES

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH,(elemento))
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID,(elemento))
        return val


 # FUNCION TEXTO MIXTO

    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

 # FUNCION CLICK MIXTO
    def Click_Mixto(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("Damos click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("Damos click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

 # FUNCION SELECCIONAR MIXTO

    def Select_Mixto_Type(self,tiposelect, selector, tipo, dato, tiempo):
        if(tiposelect == "xpath"):
            try:
                val = self.SEX(dato)
                val = Select(val)
                if (tipo == "texto"):
                    val.select_by_visible_text(dato)
                elif (tipo == "valselector"):
                    val.deselect_by_value(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                print("El campos Seleccionado es {} ".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
        elif(tiposelect == "id"):

            try:
                val = self.SEI(dato)
                val = Select(val)
                if (tipo == "texto"):
                    val.select_by_visible_text(dato)
                elif (tipo == "valselector"):
                    val.deselect_by_value(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                print("El campos Seleccionado es {} ".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

 # FUNCION EXISTE MIXTO

    def Existe(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"

    # FUNCION DOBLECLICK MIXTO

    def Mouse_Doble(self, tipo, selector,tiempo =.2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

    # FUNCION CLICK DERECHO MIXTO

    def Mouse_Derecho(self, tipo, selector,tiempo =.2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

    # FUNCION MOUSE ARRASTRAR Y SOLTAR MIXTO

    def Mouse_DragDrop(self, tipo, selector, destino, tiempo =.2):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val2 = self.SEX(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val2 = self.SEI(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

    # FUNCION ARRASTRAR Y SOLTAR CON CORDENADAS MIXTO

    def Mouse_DragDropXY(self, tipo, selector, X, Y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, X, Y).perform()
                print("Se solto el elemento en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, X, Y).perform()
                print("Se solto el elemento en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

    # FUNCION CLICK X-Y MIXTO

    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo == "xpath"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} cordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)

        elif (tipo == "id"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento{} cordenada {}, {}".format(selector, x, y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)




    # FUNCION SUBIR ARCHIVO MIXTO

    def Upload_Mixto(self, tipo, selector, ruta, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.send_keys(ruta)
                print("Se carga la imagen {} ".format(ruta))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + ruta)

        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.send_keys(ruta)
                print("Se carga la imagen {} ".format(ruta))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + ruta)

    # FUNCION MARCAR CASILLA MIXTO

    def Check_Xpath(self, tipo, xpath, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(xpath)
                val.click()
                print("Click en el elemento {} ".format(xpath))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + xpath)

        elif (tipo == "id"):
            try:
                val = self.SEI(id)
                val.click()
                print("Click en el elemento {} ".format(id))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + id)



    # FUNCION MARCAR CASILLA MULTIPLE (EN RANGO)
    def Check_Xpath_Multiples(self, tiempo, *args):
        try:
            for num in args:
                val = self.SEX(num)
                val.click()
                print("Click en el elemento {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el Elemento" + num)



    # FUNCION SALIDA
    def Salida(self):
        print("Se termina la prueba Exitosamente")
