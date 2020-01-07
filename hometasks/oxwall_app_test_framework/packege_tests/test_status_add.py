from pages.internal_pages import DashboardPage
import pytest

# TODO read data from file + add random data
data = [
    ("Hello, sun!", "Hello, sun!"),
    # ("АОЛТЛОТЛОТ", "АОЛТЛОТЛОТ"),
    # ("#^&&**(())( :-)", "#^&&**(())( ")
]

# TODO delete mark xfail after test fix
@pytest.mark.xfail
@pytest.mark.webtest
@pytest.mark.regression
@pytest.mark.parametrize("input_text, expected_text", data)
def test_status_create(driver, logged_user, input_text, expected_text, db):
    dash_page = DashboardPage(driver)

    status_elements = dash_page.status_elements
    dash_page.create_status(input_text)
    dash_page.wait_new_status(status_elements)
    status_elements = dash_page.status_elements
    assert status_elements[0].text == expected_text
    assert status_elements[0].user == logged_user
    assert status_elements[0].time == "within 1 minute"
    assert db.get_last_text_status() == status_elements[0].text