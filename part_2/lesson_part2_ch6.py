import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def get_result(value:str)->str:
	return str(math.log(abs(12*math.sin(int(value)))))


# Работа с окнами алертами
with webdriver.Chrome() as driver:
	driver.get("http://suninjuly.github.io/alert_accept.html")
	driver.find_element(By.CSS_SELECTOR, "button").click()
	driver.switch_to.alert.accept()
	value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
	result_math = get_result(value)
	driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result_math)
	driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
	print(driver.switch_to.alert.text.split(": ")[-1])
# driver = webdriver.Chrome()
# driver.get("http://google.com")
# alert = driver.switch_to.alert
# case = alert.text
# alert.accept()
# alert.dismiss()
