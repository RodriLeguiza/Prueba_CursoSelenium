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
    a = 18
    b = 28
    c = 17

    assert a<=b or a<=c, "A no es menor o igual que B o A no es menor o igual que C"

