from custom_explicity_wait import presence_of_N_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from oxwall_app import OxwallApp
import time


def test_status_create(driver, logged_user):
    app = OxwallApp(driver)

    test_text = "Hello!"
    expected_text = test_text

    text_elements = app.status_elements()
    app.create_status(test_text)
    app.wait_new_status(text_elements)
    text_elements = app.status_elements()
    assert text_elements[0].text == expected_text




