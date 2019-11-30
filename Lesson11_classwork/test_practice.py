import pytest
import sys
import presence_of_N_elements_located
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def _driver():
    sys.path.append(r"D:\SeleniumDrivers")
    driver = webdriver.Chrome()
    return driver


def test_login_and_put_text(_driver):

    #_driver = webdriver.Chrome()
    #_driver.implicitly_wait(3)

    _driver.get('https://demo.oxwall.com/')
    wait = WebDriverWait(_driver, 5)
    
    sign_bt = wait.until(presence_of_element_located((By.ID, 'loginAsUser')))
    sign_bt.click()
    sign_form = wait.until(presence_of_element_located((By.XPATH, '//*[@id="base_cmp_floatbox_ajax_signin"]/div')))

    login_editbx = _driver.find_element_by_name("identity")
    login_editbx.clear()
    password_editbx = _driver.find_elements_by_name("password")
    password_editbx.clear()

    login_editbx.send_keys("demo")
    password_editbx.send_keys("demo")


    