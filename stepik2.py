from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
browser.execute_script("window.scrollBy(0,150);")

input = browser.find_element(By.CLASS_NAME, "form-control")
input.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()

button.click()

