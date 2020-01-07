import pytest
import time
from selenium import webdriver

def test_qwe():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")
    time.sleep(2)

