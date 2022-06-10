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

def setup_function(function):
    print("Esto va al inicio de cada test \n")
def teardown_function(function):
    print("Esto va al final de cada test \n")



def test_uno():
    print("test uno")

def test_dos():
    print("test dos")

def test_tres():
    print("test tres")

def test_cuatro():
    print("test cuatro")