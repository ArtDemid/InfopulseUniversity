import pytest
import json
import os.path

from selenium import webdriver

from oxwall_manager import OxwallManager
from pages.internal_pages import MainPage
from value_models.user_model import User
from database.db_connector import DbConnector

'''
user_data.append(    
    {
      "username": random_string(),
      "password": random_string(),
      "full_name": random_string(),
      "email": "test_mail@test.com",
      "is_admin": False
    })'''

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_DIR, "data", "user_data.json")) as f:
    user_data = json.load(f)

@pytest.fixture()
def driver(selenium, base_url):
    #TODO create pytest.ini config
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        config = json.load(f)
    return config

@pytest.fixture()
def db(config):
    db = DbConnector(**config["db"])
    yield db
    db.close()

@pytest.fixture(params=user_data, ids=[str(user) for user in user_data])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)

@pytest.fixture
def logged_user(driver, user):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    dashboard_page = sign_in_page.fill_form(user)
    yield user
    # TODO: app.logout_as(user)