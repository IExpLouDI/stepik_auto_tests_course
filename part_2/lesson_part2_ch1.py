import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math


def calculate(value):
	return str(math.log(abs(12*math.sin(int(value)))))


link = "https://suninjuly.github.io/math.html"
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	driver.get(link)
	value = driver.find_element(By.CSS_SELECTOR, "#input_value").text
	input = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calculate(value))
	check_label = driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()
	check_box = driver.find_element(By.CSS_SELECTOR, ".form-radio-custom > .form-check-input").click()
	button = driver.find_element(By.CSS_SELECTOR, ".btn-default")
	button.click()
	time.sleep(8)
