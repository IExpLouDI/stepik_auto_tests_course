import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calculate(value):
	return str(math.log(abs(12*math.sin(int(value)))))


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
	driver.get(link)
	value = driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
	driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calculate(value))
	driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
	driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
	driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
	time.sleep(7)
