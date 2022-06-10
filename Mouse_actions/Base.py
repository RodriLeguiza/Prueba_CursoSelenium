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

t = .01

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
        f.Navegar("https://opensource-demo.orangehrmlive.com/", t)
        f.Texto_Mixto("id", "txtUsername", "Admin", t)
        f.Texto_Mixto("id", "txtPassword", "admin123", t)
        f.Click_Mixto("id", "btnLogin", t)

        admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        sub1 = driver.find_element(By.ID, "menu_admin_UserManagement")
        sub2 = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()

    def test2(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://demoqa.com/buttons", t)

        '''
        elemnto = driver.find_element(By.ID, "doubleClickBtn")
        act2 = ActionChains(driver)
        act2.double_click(elemnto).perform()
        time.sleep(4)
        '''
        f.Mouse_Doble("id", "doubleClickBtn")
        f.Mouse_Derecho("id", "rightClickBtn")



    def test3(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", t)
        f.Upload_Mixto("xpath", "//input[contains(@id,'fileinput')]", "C://Users//RODRIGO//PycharmProjects//Curso_Selenium//Imagenes//Gato.jpg", t)
        f.Check_Xpath("xpath", "//input[@id='itsanimage']",t)
        f.Click_Mixto("xpath", "//input[@type='submit']", t)


    def test4(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/drag-drop-javascript.html", t)
        f.Mouse_DragDrop("xpath", "//div[contains(@id,'draggable1')]", "//div[@id='droppable1']", 3)

    def test5(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://jqueryui.com/draggable/", t)
        f.Mouse_DragDropXY("id", "draggable", "150", "180", t)


    def test6(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://jqueryui.com/draggable/", t)
        #f.Mouse_DragDropXY("id", "draggable", "150", "180", 3)
        f.ClickXY("xpath", "//a[@href='https://jqueryui.com/demos/'][contains(.,'Demos')]", 500, 0, t)


    def test7(self):
        driver = self.driver
        f = Funciones_globales(driver)
        f.Navegar("https://www.google.com.ar/", t)
        f.Texto_Mixto("xpath", "//input[@title='Buscar']", "ferra", t)
        f.ClickXY("xpath", "//input[@title='Buscar']", 0, 200, t)


    def tearDown(self):
        t = self.t
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()


