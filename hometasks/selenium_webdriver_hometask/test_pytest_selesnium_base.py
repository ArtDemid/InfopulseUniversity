from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_add_delete(_url_provider, _driver, _wait):
    test_item = 'add_remove'
    test_url = _url_provider.get_test_url(test_item)
    _driver.get(test_url)
    
    add_elem_path = '//*[@id="content"]/div/button'
    add_button = _driver.find_element_by_xpath(add_elem_path)

    for i in range(3):
        add_button.click()
  
    del_elem_path = '//*[@id="elements"]/button[3]'
    delete_button = _wait.until(element_to_be_clickable((By.XPATH, del_elem_path)))
    is_element_present =  delete_button.is_displayed()

    if is_element_present:
        for i in range(3):
            del_elem_path = f'//*[@id="elements"]/button[{3-i}]'
            delete_button = _driver.find_element_by_xpath(del_elem_path)
            delete_button.click()
    
    del_elem_path = '//*[@id="elements"]/button[1]'
    
    try:
        _driver.find_element_by_xpath(del_elem_path)
        isDeleted = False
    except Exception:
        isDeleted = True

    assert test_url == 'http://the-internet.herokuapp.com/add_remove_elements/'
    assert _driver.current_url == test_url
    assert is_element_present == True
    assert isDeleted == True

    _driver.quit()

def test_checkboxes(_url_provider, _driver, _wait):
    test_item = 'checkboxes'
    test_url = _url_provider.get_test_url(test_item)
    _driver.get(test_url)

    checkbox_1_locator = '//*[@id="checkboxes"]/input[1]'
    checkbox_2_locator = '//*[@id="checkboxes"]/input[2]'
    
    checkbox_1 = _wait.until(EC.presence_of_element_located((By.XPATH, checkbox_1_locator)))
    checkbox_1.click()

    checkbox_2 = _wait.until(EC.presence_of_element_located((By.XPATH, checkbox_2_locator)))
    checkbox_2.click()
    res_1 = checkbox_1.is_selected()
    res_2 = checkbox_2.is_selected()

    assert res_1 == True
    assert res_2 == False

