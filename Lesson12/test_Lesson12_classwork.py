import time
from selenium.webdriver.support.wait import WebDriverWait


def test_status_create(driver, login_as):
    status_input = driver.find_element_by_name("status")

    test_text = "Something"
    expected_text = test_text
    time.sleep(2)
    status_input.send_keys(test_text)

    send_button = driver.find_element_by_name("save")
    send_button.click()

    time.sleep(5)

    text_element = driver.find_elements_by_class_name("ow_newsfeed_content")
    print(text_element[0].text)

    assert text_element[0].text == expected_text
    





