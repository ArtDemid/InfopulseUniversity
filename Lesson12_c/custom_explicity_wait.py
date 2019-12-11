
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait




# def presence_of_N_elements_located(driver, N, locator):
#     def func(driver):
#         elements = driver.find_elements(*locator)
#         if len(elements) == N:
#             return elements
#     return func
class presence_of_N_elements_located:
    def __init__(self, count, locator):
        self.count = count
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        print(len(elements))
        if len(elements) == self.count:
            return elements


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "http://demo.oxwall.com"
    driver.get(base_url)
    wait = WebDriverWait(driver, 5)

    els = wait.until(
        presence_of_N_elements_located(8, (By.CLASS_NAME, "ow_newsfeed_body")),
        message="Not 10 elements located"
    )
    #
    print(els)

    driver.quit()



# class presence_of_num_elements:
#     def __init__(self, locator, number):
#         self.locator = locator
#         self.number = number
#
#     def __call__(self, driver):
#         els = driver.find_elements(*self.locator)
#         if len(els) == self.number:
#             return els
#
#
# wait = WebDriverWait(driver, 10)
# buttons = wait.until(presence_of_num_elements((By.CLASS_NAME, "ow_console_item"), 2))
#
# buttons[1].click()
#




# def presence_of_num_elements(number):
#     def func(driver):
#         els = driver.find_elements_by_class_name("ow_console_item")
#         if len(els) == number:
#             return els
#     return func



#
#
# presence_of_3_elements(driver, By.CLASS_NAME, "ow_console_item")
#
#
# class presence_of_3_elements:
#     def __init__(self, by, value):
#         self.by = by
#         self.value = value
#
#     def __call__(self, wd):
#         buttons = wd.find_elements(self.by, self.value)
#         if len(buttons) == 3:
#             return buttons
#         else:
#             return False
#
#
# class number_of_elements_equals_to:
#     def __init__(self, locator, number):
#
#
# WebDriverWait(driver, 10).until(
#     presence_of_3_elements(By.CLASS_NAME, "ow_console_item")
# )
#
#
#
#
class MyClass:
    def __init__(self, const):
        self.const = const

    def __call__(self, a, b):
        print((a + b)*self.const)


obj = MyClass(123)
obj2 = MyClass(1111)

obj(1, 0)
obj2(1, 0)