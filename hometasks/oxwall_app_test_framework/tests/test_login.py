from oxwall_manager import OxwallManager as manager
from pages.internal_pages import MainPage, SignInPage, DashboardPage
from value_models.user_model import User
import pytest


@pytest.mark.webtest
@pytest.mark.smoke
@pytest.mark.nondestructive
def test_login(driver, user):  # TODO post-condition - logout
    app = manager(driver)
    # main_page = MainPage(driver)
    app.main_page.sign_in_click()

    # sign_in_window = SignInPage(driver)
    # assert app.sign_in_window.sign_in_form
    assert app.sign_in_window.username_field.placeholder == "Username/Email"
    app.sign_in_window.username_field.input(user.username)
    app.sign_in_window.password_field.input(user.password)
    app.sign_in_window.sign_in_button.click()
    assert app.sign_in_window.message.text == "AUTHENTICATION SUCCESS, PLEASE WAIT..."
    app.sign_in_window.wait_dashboard_page()

    # dashboard_page = DashboardPage(driver)
    assert app.dashboard_page.active_menu.text == "DASHBOARD"
    assert app.dashboard_page.user_menu.text == user.full_name
    # TODO logout test