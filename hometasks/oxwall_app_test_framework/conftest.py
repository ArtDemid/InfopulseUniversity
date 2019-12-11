import pytest
from selenium import webdriver
from oxwall_app import OxwallApp
from pages.internal_pages import MainPage
from value_models.user_model import User
import json
import os.path

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)

user_data.append(    {
      "username": random_string(),
      "password": random_string(),
      "full_name": random_string(),
      "email": "test1223@test.com",
      "is_admin": False
    })

@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(request):
    user = User(**request.param)
    return user


@pytest.fixture
def logged_user(driver, user):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    dashboard_page = sign_in_page.fill_form(user)
    yield user
    # TODO: app.logout_as(user)