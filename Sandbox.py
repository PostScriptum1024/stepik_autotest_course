from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

number1 = browser.find_element(By.ID, "num1")
number_1 = number1.text
number2 = browser.find_element(By.ID, "num2")
number_2 = number2.text
summ = int(number_1) + int(number_2)
summ_str = str(summ)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(summ_str)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
option2.click()

button.click()