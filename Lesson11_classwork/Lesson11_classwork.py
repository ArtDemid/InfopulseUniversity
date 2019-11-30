pass
'''
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append(r"D:\SeleniumDrivers")
_driver = webdriver.Chrome()
wait = WebDriverWait(_driver, 5)

def window_task():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    
    driver.get('http://google.com')
    element = driver.find_element_by_xpath('//*[@id="SIvCob"]/a')
    print(type(element))
    
    (webdriver.ActionChains(driver)
    .move_to_element(element)
    .key_down(Keys.CONTROL)
    .click()
    .key_up(Keys.CONTROL)
    .perform()
    )

    window = driver.current_window_handle
    print(driver.window_handles)
    print(driver.current_window_handle)
    driver.switch_to_window(driver.window_handles[1])
    element = driver.find_element_by_xpath('//*[@id="SIvCob"]/a')

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="SIvCob"]/a'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print ("Timed out waiting for page to load")
    
    (webdriver.ActionChains(driver)
    .move_to_element(element)
    .key_down(Keys.CONTROL)
    .click()
    .key_up(Keys.CONTROL)
    .perform()
    )
    driver.close()
    driver.switch_to.window(window)
    driver.close()


#window_task()
#"ow_newsfeed_body"

'''
'''
Task 2

def wiat_of_N_elements_located(driver, numbers = None, locator = None):
    def internal_func(driver):
        elements = driver.find_elements(*locator) #pair METHOD + STRING (BY.CLASSNAME + "ow_newsfeed_body") "*" - unpack tuple!!!
        #print(len(elements))
        if len(elements) == numbers:
            return elements
    return internal_func

class presence_of_N_elements_located:
    def __init__(self, count, locator):
        self.count = count
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        #print(len(elements))
        if len(elements) == self.count:
            return elements

#_driver.get('https://demo.oxwall.com')
#els = wait.until(wiat_of_N_elements_located(_driver, 10, (By.CLASS_NAME, "ow_newsfeed_body")), message = "Not 3 elements")
#print(els)

_driver.get('https://demo.oxwall.com')
els = wait.until(presence_of_N_elements_located(8, (By.CLASS_NAME, "ow_newsfeed_body")), message = "Not 10 elements")
print(els)

***********************************************************************'''

'''

'''

'''
_continue = input("Press any key to continue")