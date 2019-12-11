import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://demo/oxwall.com")
    
    yield driver # return driver first time
    driver.quit() # quit when call second time

@pytest.fixture()
def login_as(driver, username = "demo", password="demo"):
    sign_in_menu = driver.find_element_by_class_name("ow_sign_login")
    sign_in_menu.click()

    user_name_field = driver.find_element_by_name("identity")
    user_name_field.clear()  
    user_name_field.send_keys(username)

    password_field = driver.find_element_by_name("password")
    password_field.clear()
    password_field.send_keys(password)

    sign_in_button = driver.find_element_by_name("submit")
    sign_in_button.click()
    wait = WebDriverWait(driver, 5)
    wait.until(visibility_of_element_located((By.CLASS_NAME, "base_dashboard")), 
                message=f"NO visible element located {(By.CLASS_NAME, 'base_dashboard')}")

    yield

