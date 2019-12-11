import pytest
from selenium import webdriver
from pages.internal_pages import MainPage
from oxwall_app import OxwallApp
from value_models.user_model import User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.oxwall.com/")
    yield driver
    driver.quit()


'''@pytest.fixture()
def logged_user(driver):
    app = OxwallApp(driver)
    user = User(username="admin", password="pass", full_name="Admin")
    app.login_as(user)
    yield user
    app.logout_as(user="Admin")'''

@pytest.fixture()
def logged_user(driver):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    user = User(username="admin", password="pass", full_name="Admin")
    dashboard_page = sign_in_page.fill_form(user)
    yield user
    #app.logout_as(user="Admin")








# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture()
# def session(driver):
#     driver.get("http://127.0.0.1/oxwall/")
#     button = driver.find_elements_by_class_name("ow_console_item")
#     button[0].click()
#     username = driver.find_element_by_name("identity")
#     username.send_keys('admin')
#     passwd = driver.find_element_by_name('password')
#     passwd.send_keys('pass')
#     button = driver.find_element_by_name('submit')
#     button.click()
#     yield
#     buttons = driver.find_elements_by_css_selector('.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
#     action = webdriver.ActionChains(driver)
#     action.move_to_element(buttons[0]).perform()
#     action.move_to_element(driver.find_element_by_link_text('Sign Out')).click().perform()
#
#
#
# buttons = driver.find_elements_by_css_selector('.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
#
#
# action = ActionChains(driver)
# action.move_to_element(buttons[0]).perform()
# action.move_to_element(driver.find_element_by_link_text('Sign Out')).click().perform()
