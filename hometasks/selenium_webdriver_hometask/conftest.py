import pytest
import url_provider
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.expected_conditions import element_to_be_clickable
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="session")
def add_driver_to_path():
    sys.path.append(r"D:\SeleniumDrivers")

@pytest.fixture()
def _driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def _wait(_driver):
    wait = WebDriverWait(_driver, 10)
    return wait

@pytest.fixture(scope="session")
def _implicit_wait(_driver):
    _driver.implicitly_wait(3)

@pytest.fixture()
def _url_provider():
    provider = url_provider.UrlProvider()
    return provider

@pytest.fixture()
def tear_down():
    pass