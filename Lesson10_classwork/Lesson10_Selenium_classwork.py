import sys
import pynput
from pynput.keyboard import Key, Controller
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
keyboard = Controller()
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 10)
driver.get('http://google.com')
element = driver.find_element_by_name("q")
#element = wait.until()
#button = wait.until(element_to_be_clickable((By.NAME, "btnK")))
element.send_keys("python")
#button = driver.find_element_by_xpath(r"//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()
#button = driver.find_element_by_name("btnK").click()

element.send_keys(Keys.ENTER)
#time.sleep(2)
#element.send_keys(keyboard.press(Key.enter))

links = driver.find_elements_by_partial_link_text("python")
print(links)
print(type(links))
print(len(links))

links = driver.find_elements_by_partial_link_text("Download")
print (len(links))

for l in links:
    print(l.size)
    print(l.location)


action = webdriver.ActionChains(driver)

(webdriver.ActionChains(driver)
.move_to_element(drag) #define element
.key_down(Keys.CONTROL)
.click_and_hold()
.move_to_element(drop)
.release()
.key_up(Keys.CONTROL)
.perform() #run chain
)

#element.send_keys(keyboard.press(Key.enter))
#element.send_keys(keyboard.press("enter"))
#driver.find_element_by_id(_id)
time.sleep(10)
driver.quit()
#driver.close()

#driver = webdriver.Firefox(executable_path=r"C:\Users\Desktop\Drivers\geckodriver.exe")
#good practice is create separete folder for all drivers like - D:\Selenium\drivers.

'''Commands: 
driver.get()
driver.quit()
driver.close()
driver.refresh()
driver.back()
driver.forward()
'''
'''css selectors
form#loginForm
input[name="username"]
#loginForm input[type="text"] - space here means that look in class LoginForm and child element input with text
check selector in the console - $$('*[name="btnK"')
'''
