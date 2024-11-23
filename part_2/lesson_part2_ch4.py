import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def get_result(value:str)->str:
	return str(math.log(abs(12*math.sin(int(value)))))


link = "https://SunInJuly.github.io/execute_script.html"

with webdriver.Chrome() as driver:
	driver.get(link)
	value = get_result(driver.find_element(By.CSS_SELECTOR, "#input_value").text)
	button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
	driver.execute_script("window.scrollBy(0, 100);")
	driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(value)
	driver.execute_script("window.scrollBy(0, 100);")
	driver.find_element(By.CSS_SELECTOR, ".form-check-label").click()
	driver.execute_script("window.scrollBy(0, 100);")
	driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	driver.execute_script("window.scrollBy(0, 100);")
	button.click()
	time.sleep(5)
