import time
import allure
import pytest
import warnings

from  allure_commons.types import AttachmentType
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


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    s = Service('C:\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    f = Funciones_globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit']", t)
    print("Entrando al sistema")


@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, f
    s = Service('C:\Drivers\geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    warnings.simplefilter('ignore', ResourceWarning)
    f = Funciones_globales(driver)
    f.Navegar("https://www.facebook.com/", t)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.Texto_Mixto("id", "email", "aselectronica2000@gmail.com", t)
    f.Texto_Mixto("id", "pass", "empezamos0909", t)
    f.Click_Mixto("xpath", "//button[@data-testid='royal_login_button']", 4)
    print("Entrando al sistema dos")

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[2]", t)
    f.Texto_Mixto("xpath", "//input[@id='SearchFirstName']", "victoria", t)
    f.Click_Mixto("xpath", "//button[@id='search-customers']", t)
    #Tomar captura del momento
    allure.attach(driver.get_screenshot_as_png(),name= "Customers", attachment_type= AttachmentType.PNG)
    #creando nuevo usuario
    f.Click_Mixto("xpath", "//a[@href='/Admin/Customer/Create']", t)
    email = driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.send_keys("juan@gmail.com" + Keys.TAB + "12345" + Keys.TAB + "Juan" + Keys.TAB + "Perez")
    time.sleep(5)
    f.Click_Mixto("xpath", "//input[contains(@id,'Gender_Male')]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'DateOfBirth')]", "02/20/2019", 4)
    allure.attach(driver.get_screenshot_as_png(), name="Fecha de nacimiento", attachment_type=AttachmentType.PNG)
    #assert 1 == 2

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")
    f.Click_Mixto("xpath", "(//i[contains(@data-visualcompletion,'css-img')])[3]", 3)
    f.Texto_Mixto("xpath", "(//INPUT[@dir='ltr'])[2]", "Rodrigo", 3)
    allure.attach(driver.get_screenshot_as_png(), name="Buscando Rodrigo", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5'][contains(.,'Busca rodrigo')]", t)
    #assert 1 == 2


def teardown_function(function):
    print("saliendo de los test")
    driver.close()

    # from  allure_commons.types import AttachmentType (libreria)
    # allure.attach(driver.get_screenshot_as_png(), name="description", attachment_type=AttachmentType.PNG)

