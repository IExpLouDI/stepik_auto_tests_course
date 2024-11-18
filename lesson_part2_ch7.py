from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def get_result(value:str)->str:
	return str(math.log(abs(12*math.sin(int(value)))))


# Работа с вкладками браузера
# first_window = browser.window_handles[0]
# new_window = browser.window_handles[1]
# browser.switch_to.window(window_name)

with webdriver.Chrome() as driver:
	driver.get("http://suninjuly.github.io/redirect_accept.html")
	driver.find_element(By.CSS_SELECTOR, "button.trollface").click()
	new_window = driver.window_handles[1]
	driver.switch_to.window(new_window)
	value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
	result_math = get_result(value)
	driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result_math)
	driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
	print(driver.switch_to.alert.text.split(": ")[-1])
