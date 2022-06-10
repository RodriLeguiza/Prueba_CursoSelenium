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
def setup_login_uno():
    print("empezando login del sitema uno")
    yield
    print("saliendo del sistema prueba ok")


@pytest.fixture(scope='module')
def setup_login_dos():
    print("inicio pruebas sistema dos")
    yield
    print("fin pruebas dos")



def test_uno(setup_login_uno):
    print("####### empezando pruebas####")


def test_dos(setup_login_dos):
    print("esta es para la prueba dos")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("print prueba 3 modulo 2")


