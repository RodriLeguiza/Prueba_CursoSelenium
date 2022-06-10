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


@pytest.mark.validarif
def test_validar_if():
    nom1 = "Rodrigo"
    nom2 = "Juan"

    assert nom1 == nom2, " Los nombres no son iguales"


